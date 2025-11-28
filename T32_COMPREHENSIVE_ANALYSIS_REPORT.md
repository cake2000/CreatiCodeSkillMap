# T32 Digital Citizenship - Comprehensive Analysis Report

**Date:** 2025-11-28
**Total Skills:** 135 (GK:8, G1:8, G2:9, G3:9, G4:12, G5:13, G6:27, G7:27, G8:22)
**Actual Count:** 136 (includes T32.G8.04.01-03 as 3 separate skills)

---

## Executive Summary

The T32 (Digital Citizenship) topic is **generally well-designed** with strong AI ethics integration and modern topics. However, there are significant opportunities for improvement:

### Key Strengths
✓ Excellent AI ethics coverage (19 skills) with hands-on CreatiCode integration
✓ Strong accessibility focus (11 skills)
✓ Good progression from K-2 visual/unplugged to G3+ coding-based
✓ No X-2 rule violations
✓ Only 1 skill with vague verb ("understand")

### Key Issues
✗ **Grade imbalance:** G6-G7 are overloaded (27 skills each vs. 8-13 in other grades)
✗ **Consolidation opportunities:** 11-16 skills could be merged (8-12% reduction)
✗ **Missing modern topics:** Algorithmic literacy, filter bubbles, deepfakes, AI attribution
✗ **Description quality:** 32 skills have overly long/complex descriptions (600+ chars)
✗ **Career skills overload:** 31 career-related skills (23% of total)

---

## Priority 1: Critical Issues (Highest Impact)

### 1.1 Grade Distribution Imbalance (G6-G7 Overload)

**Problem:** G6 and G7 each have 27 skills, which is 2-3x more than other grades.

**Impact:**
- Teachers overwhelmed with too many skills per grade
- Students face learning overload
- Reduces time available for deeper mastery

**Distribution:**
```
K-2:  25 skills (8+8+9)     - 18% of total
3-5:  34 skills (9+12+13)   - 25% of total
6-8:  76 skills (27+27+22)  - 56% of total  ← PROBLEM
```

**Recommendation:**
- **Target:** Reduce G6-G7 to 18-20 skills each (same as G8)
- **Method:** Consolidate similar skills (see 1.2) and move some to G5 or G8
- **Specific moves:**
  - Move T32.G6.14-17 (career clusters) to G5 (builds on G5.09 interest mapping)
  - Move T32.G6.24-25 (job description analysis) to G8 (closer to resume/career prep)
  - Consolidate G6 ethics lens skills from 4 → 2

**Estimated reduction:** 7-10 skills from G6, 3-5 from G7

---

### 1.2 Consolidate Repetitive Skills

**Problem:** Multiple skills teach nearly identical content with minor variations.

#### A. Career Cluster Identification (G6.14-17) → **CONSOLIDATE TO 1 SKILL**

**Current (4 skills):**
- T32.G6.14: Identify software development careers
- T32.G6.15: Identify hardware engineering careers
- T32.G6.16: Identify data science careers
- T32.G6.17: Identify AI and machine learning careers

**Proposed (1 skill):**
```
T32.G6.14: Identify and compare computing career clusters
Description: Students research four computing career clusters: software development,
hardware engineering, data science, and AI/ML. For each cluster, they identify 2-3
example job titles, key skills needed, and typical tools used. Students create a
comparison chart showing similarities and differences across clusters.

Dependencies: [same as current G6.14]
```

**Rationale:** These four skills are structurally identical - just different domains. Teaching them as one skill with four examples is more efficient and allows comparison.

**Savings:** 3 skills

---

#### B. AI Displacement Analysis (G8.17-19) → **CONSOLIDATE TO 1 SKILL**

**Current (3 skills):**
- T32.G8.17: Identify jobs at risk of AI displacement
- T32.G8.18: Identify jobs augmented by AI
- T32.G8.19: Compare AI displacement vs augmentation patterns

**Proposed (1 skill):**
```
T32.G8.17: Analyze AI impacts on employment (displacement vs augmentation)
Description: Students research how AI affects different jobs, identifying at least
3 job categories at risk of displacement (where AI might replace workers) and 3 where
AI augments human workers (making them more effective). They create a comparison chart
showing patterns: which tasks are most at risk, which skills remain valuable, and how
workers can prepare for AI-augmented careers. Students examine how these impacts vary
across communities based on education, income, and geography.

Dependencies: [combine deps from current G8.17-19, plus add T32.G8.20]
```

**Rationale:** These three skills form one coherent analysis. You can't meaningfully identify displacement without identifying augmentation - they're two sides of the same coin.

**Savings:** 2 skills

---

#### C. Ethics Lens Application (G6.04-07) → **CONSOLIDATE TO 2 SKILLS**

**Current (4 skills):**
- T32.G6.04: Apply beneficence lens
- T32.G6.05: Apply fairness lens
- T32.G6.06: Apply autonomy lens
- T32.G6.07: Build ethics evaluation tool combining all lenses

**Proposed (2 skills):**
```
T32.G6.04: Apply ethics lenses (beneficence, fairness, autonomy) to evaluate projects
Description: Students learn three ethics lenses for evaluating technology:
(1) Beneficence: Does it help? Who benefits? Who might be harmed?
(2) Fairness: Can everyone use it equally? Are there accessibility barriers?
(3) Autonomy: Do users have control and informed choice?
Students apply each lens to CreatiCode projects using ChatGPT blocks to analyze
project purpose and document evaluations in a table variable (columns: Project, Lens,
Evidence, Rating).

Dependencies: [same as current G6.04]

---

T32.G6.07: Build comprehensive ethics evaluation tool
Description: [Keep current description - this is the culminating project using widgets]

Dependencies: T32.G6.04 [modified], T32.G5.03
```

**Rationale:** Teaching the three lenses separately may be pedagogically valuable, but they're conceptually linked. Consolidating to 2 skills (learning + applying all three, then building the tool) reduces granularity while maintaining rigor.

**Savings:** 2 skills

---

#### D. Workshop Design & Delivery → **CONSOLIDATE 5 → 3 SKILLS**

**Current (5 skills across G7-G8):**
- T32.G7.24: Plan a lesson for younger coders
- T32.G7.25: Deliver a lesson to younger coders
- T32.G8.04.01: Design workshop curriculum for responsible tech
- T32.G8.04.02: Build interactive workshop tools
- T32.G8.04.03: Deliver workshop and iterate

**Proposed (3 skills):**
```
T32.G7.24: Plan and deliver lesson to younger coders
Description: Students plan a short lesson (10-15 minutes) to teach younger students
a coding concept or tech safety topic. After delivering the lesson, they reflect on
what went well, what was challenging, and what they would change next time.

Dependencies: [combine from current G7.24-25]

---

T32.G8.04: Design, build, and deliver interactive workshop on responsible tech
Description: Students design a workshop on a responsible tech topic (screen balance,
online kindness, privacy, AI ethics). They build interactive teaching tools using
widgets and blocks, pilot the workshop with younger grades, collect feedback using
surveys, and iterate based on results.

Dependencies: T32.G7.24 [modified], [other deps from current G8.04.01-03]

---

[Optional] T32.G8.10: Lead peer workshops on responsible tech use
[Keep if workshop content differs significantly from G8.04; otherwise merge]
```

**Rationale:** G7.24-25 already form a plan-deliver pair. G8.04.01-03 duplicate this pattern with added complexity. The 3-step G8 sequence is excessive granularity.

**Savings:** 2-3 skills

---

#### E. AI Testing Skills (G6-G7) → **REDUCE BY 2 SKILLS**

**Current (5 related skills):**
- T32.G6.01: Test AI image generation for bias
- T32.G6.02: Test AI chatbots for accuracy and inclusivity
- T32.G6.03: Build AI testing dashboard combining image and chatbot tests
- T32.G7.01: Build systematic testing framework for AI perception
- T32.G7.07: Conduct bias audits for AI content generation (T20-T21)

**Issue:** G6.01 and G6.02 are overly granular when followed immediately by G6.03 which combines them.

**Proposed:**
```
Option A - Consolidate G6.01-03:
  T32.G6.01: Build AI testing dashboard for bias and accuracy
  Description: [Combine G6.01-03 into one project that tests image generation AND
  chatbots, building the dashboard from the start rather than testing separately first]

  Keep: T32.G7.01 (systematic framework for perception - different AI types)
  Keep: T32.G7.07 (comprehensive audits - more advanced)

Option B - Make G6.01-02 sub-components:
  Keep G6.03 as main skill, list G6.01-02 as "sub-skills" or learning objectives
  within the dashboard project rather than separate skills
```

**Savings:** 1-2 skills

---

**Total Consolidation Savings: 10-13 skills** (reducing 135 → 122-125 skills)

---

## Priority 2: Missing Modern Topics

### 2.1 Critically Missing Topics

The following modern digital citizenship topics have **zero or minimal coverage** despite being highly relevant:

#### A. **Algorithmic Literacy & Transparency** (0 skills)

**Gap:** No skills explicitly teach "algorithmic literacy" - understanding how algorithms shape our experiences.

**Current coverage:**
- T32.G3.02 touches on algorithms influencing content
- But no skills on: transparency requirements, algorithmic accountability, challenging algorithmic decisions

**Proposed additions:**

```
T32.G5.XX: Explain how algorithms shape online experiences
Grade: 5
Description: Students research how algorithms determine what they see online
(search results, social media feeds, video recommendations, ads). They identify
3+ types of data algorithms use (past clicks, location, time of day, friend
connections) and explain how this creates personalized experiences. Students
discuss benefits (relevant content) and concerns (filter bubbles, manipulation).

Dependencies: T32.G3.02, T32.G4.03

---

T32.G7.XX: Analyze algorithmic transparency and accountability
Grade: 7
Description: Students compare transparent vs. opaque algorithms using case studies.
They evaluate: (1) When should algorithms be required to explain their decisions?
(2) Who should be able to challenge algorithmic decisions? (3) What happens when
algorithms make mistakes? Students build a widget-based tool that simulates
algorithmic decision-making (e.g., college admissions, loan approval) with varying
transparency levels, showing impact on trust and fairness.

Dependencies: T32.G7.09 (transparency tradeoffs), T32.G6.11
```

---

#### B. **Filter Bubbles & Echo Chambers** (0 skills)

**Gap:** No skills on how personalized algorithms create information isolation.

**Proposed addition:**

```
T32.G6.XX: Analyze filter bubbles and echo chambers
Grade: 6
Description: Students investigate how recommendation algorithms can create filter
bubbles (limited exposure to diverse viewpoints). They conduct an experiment: search
for a controversial topic using different "persona" profiles (different search histories,
locations, demographics) and document how results differ. Using widgets and table
variables, they build a comparison tool showing how different users see different
information. Students propose strategies to break out of filter bubbles (diverse
sources, incognito mode, fact-checking across perspectives).

Dependencies: T32.G3.02, T32.G5.08
```

---

#### C. **Deepfake Detection & Synthetic Media** (only 1 skill: T32.G7.17)

**Current:** T32.G7.17 covers deepfakes well
**Gap:** No skills on AI-generated text detection, synthetic voice detection

**Proposed expansion:**

```
T32.G7.17: Analyze deepfakes and synthetic media detection
[KEEP CURRENT - good coverage]

---

T32.G8.XX: Evaluate AI-generated content across media types
Grade: 8
Description: Students learn to identify AI-generated content across formats: text
(ChatGPT essays, fake reviews), images (DALL-E, Midjourney), audio (voice clones),
video (deepfakes). They build a detection checklist tool using widgets with criteria
for each media type. Students test the tool on mixed sets of human and AI content,
documenting detection accuracy and limitations. They discuss implications for trust,
attribution, and authentication in digital media.

Dependencies: T32.G7.17, T32.G6.03
```

---

#### D. **AI Content Attribution & Copyright** (0 skills)

**Gap:** No skills explicitly address attribution/copyright for AI-generated content.

**Current coverage:** T32.G7.04-06 touch on AI art creation but don't deeply address attribution/copyright

**Proposed addition:**

```
T32.G7.XX: Analyze AI content attribution and copyright
Grade: 7
Description: Students investigate copyright questions around AI-generated content:
(1) Should AI art be copyrightable? Who owns it - the AI company, the prompter, or no one?
(2) Should training data sources be credited or compensated?
(3) When must AI generation be disclosed (academic work, commercial use, journalism)?
Students research legal cases and stakeholder perspectives (artists, AI companies,
users, legal experts). They conduct structured debates using a widget-based debate
tool and draft policy proposals with specific recommendations grounded in evidence.

Dependencies: T32.G7.06 (AI art gallery), T32.G5.08 (credibility evaluation)
```

**NOTE:** This partially overlaps with T32.G7.14 (debate ethics and propose policies), but T32.G7.14 is already very broad. Consider making this a specific focus of T32.G7.14 or splitting it out.

---

#### E. **Digital Footprint Management** (only 1 skill: T32.G3.01)

**Current:** T32.G3.01 introduces digital footprints at G3
**Gap:** No skills on managing existing footprints, right to deletion, reputation management

**Proposed addition:**

```
T32.G5.XX: Manage and minimize digital footprints
Grade: 5
Description: Students learn strategies for managing their digital footprint:
(1) Audit: Search for themselves online and document what's findable
(2) Minimize: Privacy settings, separate personal/public accounts, limit data sharing
(3) Curate: Build positive digital presence (portfolio, positive contributions)
(4) Delete: Right to be forgotten, account deletion, data removal requests
Students create a personal digital footprint management plan with specific actions
to take. They discuss why footprint management is harder for some groups (public
figures, marginalized communities).

Dependencies: T32.G3.01, T32.G2.04
```

---

#### F. **Dark Patterns & Persuasive Design** (minimal coverage)

**Current:** T32.G4.04 covers persuasive vs informative design
**Gap:** No explicit coverage of "dark patterns" (manipulative design)

**Proposed enhancement:**

```
T32.G4.04: Identify dark patterns and manipulative design
[EXPAND CURRENT SKILL]
Current description is good but could explicitly name "dark patterns"
Add examples: fake urgency, hidden costs, hard-to-cancel subscriptions,
misleading defaults, confirmshaming

Consider adding a G6-G7 follow-up:

T32.G6.XX: Analyze ethics of persuasive design
Description: Students analyze whether persuasive design techniques are ethical
using the G6 ethics lenses. They evaluate examples:
- Auto-play next episode (keeps you watching)
- Streaks/rewards (builds habits)
- Infinite scroll (removes stopping cues)
- Social proof ("Others bought this")
Students build a widget-based evaluation tool rating designs on ethics lenses,
then redesign a manipulative interface to be more transparent and respectful.

Dependencies: T32.G6.07, T32.G4.04
```

---

### 2.2 Emerging Topics to Consider

**Lower priority but worth considering:**

- **Biometric data ethics** (face recognition, fingerprints for school lunch)
- **IoT privacy** (smart home devices, wearables collecting data)
- **Cryptocurrency/blockchain ethics** (environmental impact, scams, speculation)
- **Gaming addiction mechanics** (loot boxes, gacha, in-app purchases targeting kids)
- **Online radicalization** (how algorithms can expose youth to extremism)

**Recommendation:** Monitor these topics. If they become more relevant to K-8 students in coming years, add skills at appropriate grades.

---

## Priority 3: Progression & Scaffolding Issues

### 3.1 Digital Footprint Progression Gap

**Current progression:**
- GK: T32.GK.04 - Choose safe sharing (role-play with yes/no cards)
- G1: [no footprint skills]
- G2: T32.G2.04 - Distinguish public vs. private information
- G3: T32.G3.01 - **[BIG JUMP]** Evaluate digital footprints (coding with widgets, if-blocks)

**Issue:** Jumping from G2 picture-card sorting to G3 coding-based evaluation is too steep.

**Recommendation:** Add unplugged G3 bridge skill before T32.G3.01:

```
T32.G3.0X: Trace a sample digital footprint
Grade: 3 (unplugged)
Description: Students trace a fictional character's digital footprint by following
their online activities (creating account → sharing photo → posting comment → joining
group). Using picture cards showing each activity, students map out what information
gets collected at each step and who can see it. They identify which shares are safe
vs. reveal too much, practicing the concepts before building the T32.G3.01 coding project.

Dependencies: T32.G2.04
```

Then keep T32.G3.01 as the coding implementation.

---

### 3.2 AI Ethics Progression

**Current progression:**
- G5: T32.G5.07 - Simple ethics questions (Does it help? Is it fair? Do users have control?)
- G6: **[BIG JUMP]** T32.G6.01-10 - Nine detailed AI ethics skills

**Issue:** G5 has one introductory ethics skill, then G6 has nine AI ethics skills. The progression is too steep.

**Recommendation:**
1. Move T32.G6.14-17 (career clusters) to G5, creating space in G6
2. Add a G5 skill applying simple ethics questions to AI tools specifically:

```
T32.G5.XX: Apply ethics questions to AI tools
Grade: 5
Description: Students apply the simple ethics framework from T32.G5.07 specifically
to AI tools they've used (ChatGPT blocks, image generation). For 3+ AI tools, they
evaluate: (1) Does it help? What are benefits and harms? (2) Is it fair? Can everyone
use it? Are outputs biased? (3) Do users have control? Do they know what data is used?
Students document findings in a comparison chart and identify which ethical question
is hardest to answer for AI.

Dependencies: T32.G5.07, T21.G5.01 [or whichever AI block skills exist at G5]
```

This creates smoother progression: G5 simple ethics → G5 AI-specific ethics → G6 formal lenses

---

### 3.3 Collaboration Progression (Generally Good)

**Current progression is smooth:**
- GK-G2: Basic turn-taking, listening, communication
- G3-G4: Team agreements, role-play conflict resolution
- G5: Feedback cycles, check-in meetings
- G6: Agile ceremonies (stand-ups, sprint reviews, task boards)
- G7: Cross-functional teams, inclusive collaboration, async tools
- G8: Capstone retrospectives

**No changes needed** - this progression is well-scaffolded.

---

## Priority 4: Description Quality Issues

### 4.1 Overly Long Descriptions (32 skills)

**Problem:** 32 skills have descriptions >600 characters or excessive parenthetical examples.

**Examples of problematic skills:**

**T32.G8.09** (1107 chars):
```
Using the impact assessment tool built in T32.G8.03, students conduct comprehensive
evaluations of real CreatiCode community projects. They: (1) Select 3+ diverse
community projects for evaluation (at least one using AI blocks T20-T23, at least
one game, at least one educational tool), (2) Systematically assess each project
using the tool, gathering evidence for each category: Test accessibility features,
Review data collection practices, Analyze potential wellbeing impacts, Evaluate
cultural representation, (3) Generate assessment reports: Use the tool's scoring
output, Review ChatGPT-generated recommendations, Add their own observations and
suggestions, (4) Create a comparative analysis using table variables: Which categories
had lowest scores across projects? What common issues emerged? Which projects
demonstrated best practices?, (5) Present findings to project creators with
constructive, evidence-based recommendations. Students reflect on assessment
challenges: How to score subjective categories consistently? When are tradeoffs
acceptable? How to balance thoroughness with practicality?
```

**Issue:** This reads like a project rubric, not a skill description. The numbered steps and questions make it hard to quickly grasp the core skill.

**Recommendation - Simplified:**
```
T32.G8.09: Apply tool to evaluate AI projects
Description: Using the impact assessment tool built in T32.G8.03, students evaluate
3+ CreatiCode community projects across all categories (accessibility, privacy,
wellbeing, cultural sensitivity). They generate assessment reports with scores and
recommendations, create comparative analysis showing common issues and best practices,
and present findings to project creators with evidence-based suggestions.
```

**General rule:** Descriptions should be 200-400 characters. If you need 600+ characters, the skill might be:
1. Too complex (break into sub-skills)
2. Too detailed (move implementation details to teacher guides)
3. Combining multiple skills (consolidate or split)

---

### 4.2 Skills with Many Parenthetical Examples

**Examples:**
- T32.G4.05: 5+ sets of parentheses
- T32.G6.09: Excessive numbered lists within parentheses
- T32.G7.13: Multiple nested parenthetical clauses

**Recommendation:**
- Limit to 2-3 parenthetical clarifications per description
- Move detailed examples/criteria to separate documentation
- Use clearer structure: main description, then "Examples:" bullet list if needed

---

## Priority 5: Career Skills Imbalance

### 5.1 Overrepresentation of Career Content

**Data:** 31 of 135 skills (23%) are career-related - this is disproportionate for a Digital Citizenship topic.

**Career skills by grade:**
- K-2: 5 skills (jobs/tools)
- G3-G4: 5 skills (diverse careers, job requirements)
- G5: 3 skills (interest mapping, helping careers)
- G6: 10 skills (clusters, job descriptions, representation, skills mapping)
- G7: 5 skills (interviews, emerging careers, equity)
- G8: 7 skills (roadmaps, portfolios, resume, AI displacement)

**Issue:** While career awareness is important, 23% feels excessive. Some skills seem more appropriate for a dedicated "Computing Careers" topic (T34?) or general career counseling.

**Recommendations:**

1. **Keep essential digital citizenship career skills (13-15 skills):**
   - K-2: Basic job awareness (keep current 5)
   - G3-5: Diverse representation, interest mapping (keep 5-6)
   - G6: Career clusters overview (consolidated to 1), representation analysis (keep 2)
   - G7-8: AI impact on careers, equity (keep 3-4)

2. **Move or cut tactical career skills (6-8 skills):**
   - T32.G6.24-25: Job description analysis → Move to G8 near resume writing OR cut
   - T32.G7.18-19: Career interviews → Could be general career counseling, not DC-specific
   - T32.G8.11-13: Course planning, roadmaps → General career counseling, not DC-specific
   - T32.G8.14-16: Portfolio, resume, interview prep → General career counseling OR move to separate topic

3. **Focus digital citizenship career skills on:**
   - Representation and equity in tech
   - AI's impact on work (automation, augmentation)
   - Ethics in tech careers (responsible AI development, accessibility advocacy)
   - Connecting DC values (fairness, privacy, accessibility) to career choices

**Potential reduction:** 6-8 career skills

---

## Priority 6: Theme Distribution Analysis

**Current theme distribution:**
```
AI Ethics:                     19 skills (14%)
Tech Careers:                  26 skills (19%)  ← TOO HIGH
Collaboration:                 23 skills (17%)
Digital Safety & Well-being:   11 skills (8%)   ← COULD EXPAND
Accessibility:                 11 skills (8%)
Privacy & Data:                9 skills (7%)
Critical Thinking:             10 skills (7%)
Online Citizenship:            4 skills (3%)    ← UNDERREPRESENTED
Other:                         22 skills (16%)
```

**Observations:**

1. **Tech Careers overrepresented** (19%) - see Priority 5
2. **Online Citizenship underrepresented** (3%) - only 4 skills:
   - T32.G2.03: Practice online kindness scripts
   - T32.G3.03: Develop class guidelines for respectful communication
   - T32.G4.07: Create a digital citizen pledge project
   - [Others may be miscategorized]

3. **Digital Safety & Well-being** (8%) could expand to include:
   - Gaming addiction / compulsive use
   - Cyberbullying detection and response
   - Digital wellness tools (screen time trackers, focus apps)
   - Mental health impacts of social media

**Recommendations:**

### 6.1 Expand Online Citizenship (Currently 4 skills → Target 8-10 skills)

**Missing online citizenship topics:**
- Cyberbullying bystander intervention
- Respectful disagreement online
- Online reputation management (overlaps with digital footprint)
- Digital citizenship across cultures (norms vary globally)

**Proposed additions:**

```
T32.G4.XX: Respond to cyberbullying as a bystander
Grade: 4
Description: Students learn bystander strategies for responding to online meanness:
(1) Support the target (private message: "That was mean, are you OK?"), (2) Report
to trusted adult, (3) Don't share or like mean content, (4) Counter with kindness.
Students role-play scenarios using CreatiCode chat simulation and practice choosing
helpful responses. They discuss why bystanders matter and barriers to intervention.

---

T32.G6.XX: Practice respectful disagreement online
Grade: 6
Description: Students learn techniques for disagreeing respectfully in online spaces:
(1) Assume good intent, (2) Ask clarifying questions before criticizing, (3) Focus on
ideas not people, (4) Acknowledge valid points, (5) Know when to disengage. Students
build a discussion simulator using widgets where they practice responding to
controversial statements. They compare respectful vs. hostile responses and analyze
how tone affects outcomes.

Dependencies: T32.G3.03 (respectful communication guidelines)
```

---

### 6.2 Expand Digital Well-being (Currently 11 skills → Target 13-15 skills)

**Current coverage good but could add:**
- Recognizing compulsive/addictive patterns
- Using digital wellness tools
- Social media's impact on mental health and comparison

**Proposed additions:**

```
T32.G5.XX: Recognize compulsive technology use patterns
Grade: 5
Description: Students learn warning signs of compulsive tech use: checking phone
despite no notification, feeling anxious without device, neglecting responsibilities,
sleep loss, missing social activities. They analyze fictional case studies and identify
healthy vs. concerning patterns. Students design a self-monitoring tool (daily tracker
using widgets) to log their tech use and feelings, identifying personal triggers for
compulsive use.

Dependencies: T32.G2.02 (balanced schedules), T32.G5.04 (well-being debates)

---

T32.G7.XX: Analyze social media's impact on mental health
Grade: 7
Description: Students research correlations between social media use and mental health
(anxiety, depression, FOMO, social comparison, body image). They evaluate research
quality (correlation vs causation, sample size, conflicts of interest). Using data
from studies, they create visualizations (table variables, sprite graphics) showing
relationships. Students propose evidence-based strategies to mitigate harms while
preserving benefits.

Dependencies: T32.G5.04 (well-being debates), T32.G7.16 (data visualization ethics)
```

---

## Summary: Prioritized Action Plan

### Phase 1: Consolidation & Redistribution (Target: -10 to -15 skills)

**Immediate consolidations:**
1. ✅ Merge T32.G6.14-17 (career clusters) → 1 skill **(-3 skills)**
2. ✅ Merge T32.G8.17-19 (AI displacement) → 1 skill **(-2 skills)**
3. ✅ Consolidate T32.G6.04-06 (ethics lenses) → 1 skill **(-2 skills)**
4. ✅ Merge T32.G7.24-25 + T32.G8.04.01-03 (workshops) → 2-3 skills **(-2-3 skills)**
5. ✅ Simplify T32.G6.01-03 (AI testing) → consider making 01-02 sub-components **(-1-2 skills)**

**Grade redistributions:**
6. Move consolidated career clusters skill to G5 **(G6: -1)**
7. Move T32.G6.24-25 (job descriptions) to G8 **(G6: -2)**
8. Consider moving T32.G7.18-19 (career interview) to G8 or cutting **(G7: -1-2)**

**Estimated result:** 135 skills → 120-125 skills, G6-G7 reduced to ~20-22 each

---

### Phase 2: Add Missing Modern Topics (Target: +5 to +8 skills)

**Critical additions:**
1. ✅ T32.G5.XX: Explain algorithmic influence on experiences
2. ✅ T32.G6.XX: Analyze filter bubbles and echo chambers
3. ✅ T32.G7.XX: Analyze AI content attribution and copyright
4. ✅ T32.G8.XX: Evaluate AI-generated content across media types
5. ✅ T32.G5.XX: Manage and minimize digital footprints

**Important additions:**
6. ✅ T32.G7.XX: Analyze algorithmic transparency and accountability
7. ✅ Expand T32.G4.04 to explicitly cover dark patterns

**Consider adding:**
8. T32.G4.XX: Respond to cyberbullying as bystander
9. T32.G6.XX: Practice respectful disagreement online
10. T32.G5.XX: Recognize compulsive technology use
11. T32.G7.XX: Analyze social media's mental health impact

**Estimated result:** +5 to +8 skills (prioritize top 5 critical additions)

---

### Phase 3: Quality Improvements

**Description simplification (32 skills need editing):**
- Reduce descriptions from 600+ chars to 200-400 chars
- Limit parenthetical examples to 2-3 per description
- Move implementation details to teacher guides

**Priority skills to simplify:**
- T32.G8.09 (1107 chars)
- T32.G7.14 (1157 chars)
- T32.G7.13 (977 chars)
- T32.G8.10 (928 chars)
- T32.G8.08 (862 chars)

**Progression improvements:**
- Add T32.G3.0X bridge skill for digital footprints
- Add T32.G5.XX AI ethics bridge skill
- Verify smooth dependency chains after consolidations

**Weak verb review:**
- T32.G4.12 "Match skills to tech job requirements" → Consider "Analyze skills needed for tech jobs" or consolidate into career cluster skill

---

### Net Impact Projection

**Starting point:** 135 skills (GK:8, G1:8, G2:9, G3:9, G4:12, G5:13, G6:27, G7:27, G8:22)

**After Phase 1 (Consolidation):** ~120-125 skills
- G6: 27 → 20-22 skills
- G7: 27 → 20-22 skills
- G8: 22 → 21-23 skills
- Other grades: mostly unchanged

**After Phase 2 (Add topics):** ~125-130 skills
- G3: 9 → 10 skills (add footprint bridge)
- G4: 12 → 13 skills (add cyberbullying or expand dark patterns)
- G5: 13 → 15-16 skills (add algorithmic influence, digital footprint mgmt, compulsive use)
- G6: 20-22 → 21-23 skills (add filter bubbles, respectful disagreement)
- G7: 20-22 → 21-23 skills (add attribution, algorithmic transparency, social media mental health)
- G8: 21-23 skills (add AI content detection)

**After Phase 3 (Quality):** Same count, better quality
- 32 descriptions simplified
- Smoother progression with bridge skills
- Clearer dependency chains

**Final target:** ~125-130 high-quality skills with better distribution

---

## Appendix A: Skills with Quality Issues

### Vague Verbs (1 skill)
- T32.G3.05: "Interview classmates to **understand** project needs" → Change to "Interview classmates **to identify** project needs"

### Weak Verbs in G3+ (1 skill)
- T32.G4.12: "**Match** skills to tech job requirements" → Could strengthen but acceptable if consolidated into career cluster skill

### X-2 Rule Violations
- **NONE** ✅ Excellent compliance

### K-2 Visual/Unplugged Compliance
- **ALL K-2 skills use picture cards, sorting, role-play** ✅ Excellent compliance

---

## Appendix B: Detailed Consolidation Specifications

[See sections under Priority 1.2 for detailed before/after skill descriptions]

---

## Appendix C: Modern Topics Coverage

| Topic | Current Skills | Proposed Skills | Priority |
|-------|---------------|-----------------|----------|
| Deepfakes | 1 (G7.17) | 2 (add G8 AI content detection) | High |
| Algorithmic literacy | 0 | 2 (G5 influence, G7 transparency) | **Critical** |
| Filter bubbles | 0 | 1 (G6) | **Critical** |
| AI attribution | 0 | 1 (G7) | **Critical** |
| Digital footprint mgmt | 1 (G3.01) | 2 (add G5 management) | High |
| Dark patterns | 1 (G4.04) | 1 (expand current) | High |
| Cyberbullying response | 0 | 1 (G4 bystander) | Medium |
| Respectful disagreement | 0 | 1 (G6) | Medium |
| Compulsive use | 0 | 1 (G5) | Medium |
| Social media mental health | 0 | 1 (G7) | Medium |
| Biometric ethics | 0 | 0 (monitor) | Low |
| IoT privacy | 0 | 0 (monitor) | Low |
| Crypto ethics | 0 | 0 (monitor) | Low |

---

**End of Report**

**Next Steps:**
1. Review consolidation proposals with curriculum team
2. Prioritize which missing topics to add (recommend top 5 critical additions)
3. Assign writers to simplify long descriptions
4. Update dependency chains after consolidations
5. Pilot revised skills with teachers for feasibility feedback
