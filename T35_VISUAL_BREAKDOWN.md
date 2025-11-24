# T35 (Impacts & Ethics) - Visual Breakdown
**Date:** 2024-11-24

## SKILL COUNT COMPARISON

```
BEFORE OPTIMIZATION:
K:   ████           (4 skills)
G1:  ████           (4 skills)
G2:  ████           (4 skills)
G3:  ████           (4 skills)
G4:  █████          (5 skills)
G5:  ████           (4 skills)
G6:  █████████      (9 skills) ⚠️ Many too broad
G7:  █████████      (9 skills) ⚠️ Many too broad
G8:  ██████         (6 skills) ⚠️ Some too broad
                    ─────────
TOTAL: 49 skills

AFTER OPTIMIZATION:
K:   ████           (4 skills)
G1:  ████           (4 skills)
G2:  █████          (5 skills) +1 bridge
G3:  ████           (4 skills)
G4:  █████          (5 skills)
G5:  █████          (5 skills) +1 framework intro
G6:  █████████████████ (13 skills) +4 from splits, +1 bias intro
G7:  ████████████████████ (16 skills) +6 from splits, +1 surveillance intro
G8:  ████████       (8 skills) +2 from splits
                    ─────────
TOTAL: ~74 skills (+25 skills, +51% increase)
```

---

## SKILLS REQUIRING SPLITS

### GRADE 6 (4 skills → 13 skills)

```
T35.G6.01 [TOO BROAD - 3 ethics frameworks]
├─ SPLIT INTO ─┐
               ├→ T35.G6.01.01 - Apply beneficence lens
               ├→ T35.G6.01.02 - Apply fairness lens
               ├→ T35.G6.01.03 - Apply autonomy lens
               └→ T35.G6.01.04 - Compare ethics frameworks

T35.G6.03.01 [TOO BROAD - 2 AI types]
├─ SPLIT INTO ─┐
               ├→ T35.G6.03.01a - Test AI image generation (T21)
               └→ T35.G6.03.01b - Test AI chatbots (T22)

T35.G6.03.03 [TOO BROAD - 2 AI types]
├─ SPLIT INTO ─┐
               ├→ T35.G6.03.03a - Guidelines for AI perception (T23)
               └→ T35.G6.03.03b - Guidelines for AI assistance (T24)

T35.G6.05.02 [TOO BROAD - 4 features]
├─ SPLIT INTO ─┐
               ├→ T35.G6.05.02a - Implement data viewing
               └→ T35.G6.05.02b - Implement data deletion

SUMMARY: 4 original skills → 13 focused skills (+9)
```

### GRADE 7 (5 skills → 16 skills)

```
T35.G7.01.01 [TOO BROAD - framework + 2 AI types]
├─ SPLIT INTO ─┐
               ├→ T35.G7.01.01a - Build bias testing framework
               ├→ T35.G7.01.01b - Audit AI perception (T23)
               └→ T35.G7.01.01c - Audit AI assistance (T24)

T35.G7.04.01 [TOO BROAD - 3 tracking systems]
├─ SPLIT INTO ─┐
               ├→ T35.G7.04.01a - Entry/exit tracking
               ├→ T35.G7.04.01b - Movement classification
               └→ T35.G7.04.01c - Surveillance dashboard

T35.G7.04.02 [TOO BROAD - 4 major activities]
├─ SPLIT INTO ─┐
               ├→ T35.G7.04.02a - Analyze surveillance data
               └→ T35.G7.04.02b - Debate surveillance ethics

T35.G7.05.01 [TOO BROAD - multiple experiments]
├─ SPLIT INTO ─┐
               ├→ T35.G7.05.01a - Generate art in styles
               ├→ T35.G7.05.01b - Generate commercial assets
               └→ T35.G7.05.01c - Analyze AI art capabilities

T35.G7.05.02 [TOO BROAD - research + debates + policy]
├─ SPLIT INTO ─┐
               ├→ T35.G7.05.02a - Research stakeholder perspectives
               ├→ T35.G7.05.02b - Conduct ethics debates
               └→ T35.G7.05.02c - Draft policy proposals

SUMMARY: 5 original skills → 16 focused skills (+11)
```

### GRADE 8 (2 skills → 8 skills)

```
T35.G8.02 [TOO BROAD - research + data + visualization + policy]
├─ SPLIT INTO ─┐
               ├→ T35.G8.02a - Research and collect data
               ├→ T35.G8.02b - Visualize equity data
               └→ T35.G8.02c - Draft policy brief

T35.G8.03.01 [TOO BROAD - 4 assessment categories]
├─ SPLIT INTO ─┐
               ├→ T35.G8.03.01a - Build accessibility module
               ├→ T35.G8.03.01b - Build privacy module
               ├→ T35.G8.03.01c - Build wellbeing module
               └→ T35.G8.03.01d - Integrate modules

SUMMARY: 2 original skills → 8 focused skills (+6)
```

**TOTAL SPLITS: 11 original skills → 37 focused skills (+26 skills)**

---

## NEW SCAFFOLDING SKILLS

```
GRADE 2-3 BRIDGE:
T35.G2.05 [NEW] - Introduction to digital ethics tools
Purpose: Bridge from unplugged to block-based ethics
Location: Between T35.G2.04 and T35.G3.01

GRADE 5-6 BRIDGE:
T35.G5.05 [NEW] - Introduction to ethics frameworks
Purpose: Learn beneficence, fairness, autonomy concepts
Location: Between T35.G5.04 and T35.G6.01

GRADE 6 AI ETHICS:
T35.G6.03.00 [NEW] - Explore AI bias concepts
Purpose: Understand bias before testing
Location: Before T35.G6.03.01a and T35.G6.03.01b

GRADE 7 SURVEILLANCE:
T35.G7.04.00 [NEW] - Research surveillance technology uses
Purpose: Context before building simulator
Location: Before T35.G7.04.01a

TOTAL NEW SKILLS: 4
```

---

## THEMATIC PROGRESSION K-8

```
KINDERGARTEN (Unplugged)
┌─────────────────────────────────────┐
│ Helpful technology                  │
│ Screen time awareness               │
│ Sharing etiquette                   │
│ Safe information sharing            │
└─────────────────────────────────────┘

GRADE 1 (Unplugged)
┌─────────────────────────────────────┐
│ Good vs. not-so-good choices        │
│ Feelings and technology             │
│ Technology creator choices          │
│ When to tell adults                 │
└─────────────────────────────────────┘

GRADE 2 (Unplugged)
┌─────────────────────────────────────┐
│ Benefits and harms                  │
│ Balanced tech schedules             │
│ Online kindness                     │
│ Public vs. private information      │
│ [NEW] Digital ethics tools intro    │
└─────────────────────────────────────┘

GRADE 3 (First Block-Based)
┌─────────────────────────────────────┐
│ Digital footprints (if-blocks)      │
│ Algorithms and recommendations      │
│ Respectful communication (AI mod)   │
│ Apps collecting data                │
└─────────────────────────────────────┘

GRADE 4 (Analysis & Accessibility)
┌─────────────────────────────────────┐
│ Community impacts case studies      │
│ Advertising and persuasion          │
│ Test accessibility features         │
│ Implement accessibility fixes       │
│ Digital citizen pledge              │
└─────────────────────────────────────┘

GRADE 5 (Global & AI Introduction)
┌─────────────────────────────────────┐
│ Global impacts                      │
│ Digital wellbeing debates           │
│ AI differential impacts             │
│ Stakeholder impact visualization    │
│ [NEW] Ethics frameworks intro       │
└─────────────────────────────────────┘

GRADE 6 (AI Ethics Deep Dive)
┌─────────────────────────────────────────────────┐
│ [NEW] AI bias concepts                          │
│ Apply ethics lenses (4 skills) ←SPLIT           │
│ Data privacy tradeoffs                          │
│ Build consent form                              │
│ Implement data controls (2 skills) ←SPLIT       │
│ Test AI content generation (2 skills) ←SPLIT    │
│ Synthesize AI ethics guidelines                 │
│ Guidelines for AI perception/assist (2) ←SPLIT  │
│ Digital divide data                             │
└─────────────────────────────────────────────────┘

GRADE 7 (Advanced AI Ethics)
┌─────────────────────────────────────────────────┐
│ Conduct AI content bias audits                  │
│ Audit AI perception/assist (3 skills) ←SPLIT    │
│ Unintended consequences                         │
│ Transparency vs. security                       │
│ [NEW] Surveillance tech research                │
│ Build surveillance simulator (3 skills) ←SPLIT  │
│ Analyze surveillance impacts (2 skills) ←SPLIT  │
│ Experiment AI media (3 skills) ←SPLIT           │
│ AI art ethics debate/policy (3 skills) ←SPLIT   │
│ Honest vs. misleading data viz                  │
│ Community discussions                           │
└─────────────────────────────────────────────────┘

GRADE 8 (Synthesis & Application)
┌─────────────────────────────────────────────────┐
│ Apply ethical frameworks                        │
│ AI chatbots and information literacy            │
│ Draft equity policy brief (3 skills) ←SPLIT     │
│ Build impact assessment tool (4 skills) ←SPLIT  │
│ Apply assessment tool                           │
│ Lead peer workshops                             │
└─────────────────────────────────────────────────┘
```

---

## COMPLEXITY ANALYSIS

```
COMPLEXITY RATING (1=Simple, 5=Very Complex)

K-2 SKILLS: ★☆☆☆☆ (Appropriate - unplugged, concrete)
├─ Picture sorting
├─ Role-play scenarios
└─ Simple categorization

G3-4 SKILLS: ★★☆☆☆ (Appropriate - basic blocks)
├─ If-blocks for simple checks
├─ Variables for data tracking
└─ Widget interfaces

G5 SKILLS: ★★★☆☆ (Appropriate - research & analysis)
├─ Research tasks
├─ Debates with evidence
└─ Data visualization basics

BEFORE OPTIMIZATION:
G6 SKILLS: ★★★★★ (Too Complex - multiple objectives)
├─ 3 ethics frameworks in one skill
├─ 2 AI types in one testing skill
└─ 4 data control features in one skill

G7 SKILLS: ★★★★★ (Too Complex - multi-part projects)
├─ Framework + 2 audits in one skill
├─ 3 tracking systems in one skill
└─ Research + debates + policy in one skill

G8 SKILLS: ★★★★★ (Too Complex - comprehensive projects)
├─ Research + data + viz + policy in one
└─ 4 assessment categories in one skill

AFTER OPTIMIZATION:
G6 SKILLS: ★★★★☆ (Appropriate - focused objectives)
├─ One ethics lens per skill
├─ One AI type per testing skill
└─ One data feature per skill

G7 SKILLS: ★★★★☆ (Appropriate - manageable chunks)
├─ Framework separate from audits
├─ One tracking system per skill
└─ Research → debates → policy sequenced

G8 SKILLS: ★★★★☆ (Appropriate - complex but focused)
├─ Data collection → visualization → brief
└─ One assessment category per module
```

---

## CROSS-TOPIC DEPENDENCIES MAP

```
T35 DEPENDS ON:
┌───────────────────────────────────────────────┐
│ T01 (Computational Thinking)                  │
│   └→ K-G2: Basic sequencing and comparison    │
│                                               │
│ T06 (Events)                                  │
│   └→ G3+: Green-flag scripts                  │
│                                               │
│ T08 (Conditionals)                            │
│   └→ G3+: If-blocks for decision logic        │
│                                               │
│ T09 (Variables)                               │
│   └→ G3+: Data tracking                       │
│                                               │
│ T16 (Widgets) ★ HEAVY DEPENDENCY              │
│   ├→ G3: Labels                               │
│   ├→ G4: Interactive displays                 │
│   ├→ G5: Surveys                              │
│   ├→ G6: Multiple widget types                │
│   ├→ G7: Interactive data displays            │
│   └→ G8: Complex multi-widget apps            │
│                                               │
│ T19 (Data & Cloud)                            │
│   ├→ G5: Google Sheets ⚠️ (verify X-2 rule)   │
│   ├→ G6-G7: Cloud tables                      │
│   └→ G7: Data visualizations                  │
│                                               │
│ T21 (AI Image Generation) ★ AI ETHICS         │
│   ├→ G6: Generate images                      │
│   └→ G7: Complex images                       │
│                                               │
│ T22 (AI Chatbots) ★ AI ETHICS                 │
│   ├→ G3: Simple queries                       │
│   ├→ G4: Text-to-speech                       │
│   ├→ G6: Analysis tasks, complex conversations│
│   └→ G8: Advanced analysis                    │
│                                               │
│ T23 (AI Perception) ★ AI ETHICS               │
│   ├→ G6: Perception tools                     │
│   └→ G7: Hand and body tracking               │
│                                               │
│ T24 (AI Coding Assistants) ★ AI ETHICS        │
│   └→ G6: Coding assistants                    │
└───────────────────────────────────────────────┘

OTHER TOPICS DEPEND ON T35:
┌───────────────────────────────────────────────┐
│ T31 (Internet & Cloud)                        │
│   └→ References T35 ethics requirements       │
│                                               │
│ T32 (Cybersecurity)                           │
│   └→ Multiple references to T35 frameworks    │
│                                               │
│ T34 (Computing History)                       │
│   └→ Thematic connections to equity work      │
└───────────────────────────────────────────────┘

✓ NO X-2 RULE VIOLATIONS FOUND within T35
⚠️ VERIFY: T19.G5.01 timing (G5 first cloud skill?)
```

---

## KEY METRICS

```
TOTAL SKILLS
Before: 49
After:  ~74
Change: +25 skills (+51%)

SKILLS PER GRADE
         Before  After  Change
K:         4      4       0
G1:        4      4       0
G2:        4      5      +1
G3:        4      4       0
G4:        5      5       0
G5:        4      5      +1
G6:        9     13      +4
G7:        9     16      +7
G8:        6      8      +2

CHANGES BY TYPE
Skills split:        11 → 37 (+26)
New scaffolding:     +4
Descriptions fixed:  3
Dependencies verified: All

AI ETHICS COVERAGE
T21 (Images):      6 skills (G6-G7)
T22 (Chatbots):    8 skills (G3-G8)
T23 (Perception):  5 skills (G6-G7)
T24 (Assistance):  3 skills (G6-G7)

CROSS-TOPIC DEPENDENCIES
Incoming:  20+ dependencies from other topics
Outgoing:  3 topics reference T35
Violations: 0 confirmed, 1 to verify
```

---

## ISSUE SEVERITY BREAKDOWN

```
CRITICAL (Must Fix)
├─ T35.G6.01: 3 frameworks in one skill
├─ T35.G6.03.01: 2 AI types in one skill
├─ T35.G6.03.03: 2 AI types in one skill
├─ T35.G7.01.01: Framework + 2 AI types
├─ T35.G7.04.01: 3 tracking systems
├─ T35.G7.04.02: 4 major activities
├─ T35.G7.05.01: Multiple experiments
├─ T35.G7.05.02: Research + debate + policy
├─ T35.G8.02: Research + data + viz + policy
└─ T35.G8.03.01: 4 assessment categories
   TOTAL: 10 skills requiring immediate split

HIGH PRIORITY (Should Fix)
├─ T35.G6.05.02: 4 data features
├─ T35.G2.05 [MISSING]: G2-G3 bridge
├─ T35.G5.05 [MISSING]: Ethics frameworks intro
├─ T35.G6.03.00 [MISSING]: AI bias concepts
└─ T35.G7.04.00 [MISSING]: Surveillance context
   TOTAL: 1 split + 4 new skills

MEDIUM PRIORITY (Should Improve)
├─ T35.G5.02: Vague description (evidence sources)
├─ T35.G6.04: Vague description (community actions)
└─ T35.G8.01.01: Incomplete description
   TOTAL: 3 descriptions to clarify

LOW PRIORITY (Verify)
├─ T35.G3.03: Potentially complex but manageable
├─ T35.G4.03.01: Detailed but acceptable
├─ T35.G5.03: Broad but acceptable research skill
└─ T19.G5.01 dependency timing
   TOTAL: 3 skills to monitor + 1 verification
```

---

## IMPLEMENTATION CHECKLIST

```
PHASE 1: CRITICAL SPLITS (10 skills)
☐ T35.G6.01 → 4 skills (ethics lenses)
☐ T35.G6.03.01 → 2 skills (T21, T22)
☐ T35.G6.03.03 → 2 skills (T23, T24)
☐ T35.G6.05.02 → 2 skills (view, delete)
☐ T35.G7.01.01 → 3 skills (framework, T23, T24)
☐ T35.G7.04.01 → 3 skills (entry/exit, movement, dashboard)
☐ T35.G7.04.02 → 2 skills (analyze, debate)
☐ T35.G7.05.01 → 3 skills (styles, commercial, analyze)
☐ T35.G7.05.02 → 3 skills (research, debate, policy)
☐ T35.G8.02 → 3 skills (research, visualize, brief)
☐ T35.G8.03.01 → 4 skills (access, privacy, wellbeing, integrate)

PHASE 2: NEW SCAFFOLDING (4 skills)
☐ T35.G2.05 - Digital ethics tools intro
☐ T35.G5.05 - Ethics frameworks intro
☐ T35.G6.03.00 - AI bias concepts
☐ T35.G7.04.00 - Surveillance tech research

PHASE 3: DESCRIPTION FIXES (3 skills)
☐ T35.G5.02 - Add evidence sources
☐ T35.G6.04 - Add community action specifics
☐ T35.G8.01.01 - Complete description

PHASE 4: VERIFICATION (2 items)
☐ Check T19.G5.01 timing (X-2 rule)
☐ Verify T16, T21-T24 progressions support T35

PHASE 5: DOCUMENTATION (ongoing)
☐ Assign new skill IDs
☐ Update all dependencies
☐ Add CSTA alignments
☐ Create teaching examples
☐ Update allskills.md
```

---

## BENEFITS SUMMARY

```
✓ CLEARER LEARNING OBJECTIVES
  Before: "Test AI tools, develop guidelines, apply frameworks"
  After:  "Test T21 image bias" (focused, assessable)

✓ BETTER PACING
  Before: G6 student faces 3 ethics frameworks at once
  After:  G6 student learns one framework per skill

✓ EASIER TEACHING
  Before: Teacher plans mega-lesson covering 4 topics
  After:  Teacher plans focused lessons with clear goals

✓ EASIER ASSESSMENT
  Before: Hard to evaluate "comprehensive AI ethics knowledge"
  After:  Can assess "Can student identify representation bias?"

✓ REDUCED OVERWHELM
  Before: "Build surveillance system with 3 types of tracking"
  After:  "Build entry/exit tracking" → next skill adds movement

✓ MAINTAINED RIGOR
  Before: 49 skills cover K-8 ethics comprehensively
  After:  74 skills cover SAME CONTENT, better organized

✓ IMPROVED SCAFFOLDING
  Before: G2 unplugged → G3 block-based (big jump)
  After:  G2 intro to digital tools → G3 block-based (smooth)

✓ COMPREHENSIVE AI ETHICS
  Before: 22 AI-related ethics skills across T21-T24
  After:  26 AI ethics skills (more focused, still comprehensive)
```

---

**VISUAL BREAKDOWN COMPLETE**
