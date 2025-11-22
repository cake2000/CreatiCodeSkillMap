# T34 (Computing History) - Optimization Summary

## Quick Status

- **Total Skills**: 27 (3 per grade K-8, perfectly balanced)
- **Overall Quality**: HIGH
- **Critical Issues**: 0
- **Medium Priority Issues**: 7
- **Low Priority Issues**: 3

---

## Action Items

### 1. Description Improvements (MEDIUM Priority)

#### T34.G1.03 - Make more specific and actionable

**Current**:
```
Skill: Explain that technology choices shape games/apps
Description: Learners state that creators pick characters, rules, and visuals, highlighting human design decisions.
```

**Recommended**:
```
Skill: Identify design choices in games/apps
Description: Learners examine 2-3 simple games or apps and identify specific design choices creators made (character selection, color scheme, sound effects, game rules). They explain one choice they would make differently and why, demonstrating that technology reflects human decisions.
```

**Rationale**: More actionable, specific deliverable, clearer assessment.

---

#### T34.G2.02 - Add structure for better clarity

**Current**:
```
Skill: Identify communities impacted by inventions
Description: Learners analyze a case (screen readers, online maps) and list groups that gained access.
```

**Recommended**:
```
Skill: Identify communities impacted by inventions
Description: Learners analyze a case study (screen readers, online maps, or video captioning) and create a simple chart showing: (1) what problem existed before the invention, (2) which communities were affected by this problem, (3) how the invention helped these communities gain access.
```

**Rationale**: Chart structure makes expectations clearer, better assessment.

---

#### T34.G5.01 - Clarify scope (OR split)

**Current**:
```
Skill: Investigate social movements linked to computing
Description: Learners research how computing supported social causes (accessibility advocacy, community organizing, open-source movements) and analyze both historical movements and current initiatives.
```

**Option A - Clarify scope (keep as one skill)**:
```
Skill: Investigate social movements linked to computing
Description: Learners research how computing supported social causes (accessibility advocacy, community organizing, open-source movements) from the 1960s to present day. They create a timeline showing 3-4 movements and analyze how each used computing tools, then compare one historical movement to a current digital activism initiative.
```

**Option B - Split into two skills**:
```
T34.G5.01: Research historical social movements and computing (1960s-2000)
Description: Learners research how computing supported historical social causes (accessibility advocacy in the 1980s-90s, community organizing with early internet, early open-source movement) and create a timeline showing how each movement used technology.

T34.G5.01b: Connect historical movements to current digital activism
Description: Students compare one historical computing-supported movement to a current initiative (e.g., early accessibility advocacy vs modern #a11y movement, early BBSs vs Discord communities), analyzing similarities and differences in how technology enables organizing.
Dependencies: T34.G5.01
```

**Recommendation**: **Option A** (keep as one skill) with clarified scope. Position as 2-3 week unit.

---

#### T34.G6.01 - Remove redundant prediction component

**Current**:
```
Skill: Analyze waves of computing (mainframe → mobile → AI)
Description: Students build comparison charts showing key characteristics (dominant hardware, typical users, limitations) for each computing era and make predictions about the next wave.
```

**Recommended**:
```
Skill: Analyze waves of computing (mainframe → mobile → AI)
Description: Students build comparison charts showing key characteristics (dominant hardware, typical users, limitations, societal impact) for each computing era (mainframe 1950s-70s, personal computing 1980s-2000s, mobile 2000s-2010s, AI/cloud 2010s-present), identifying patterns in how each wave emerged.
```

**Rationale**: "Make predictions" is redundant with T34.G8.01 which focuses entirely on forecasting. Keep G6.01 focused on analysis of past waves.

---

#### T34.G6.03 - Change passive verb to active

**Current**:
```
Skill: Learn from historical computing failures
Description: Students study famous software bugs and system failures (Ariane 5 rocket, Y2K problem, Therac-25) and explain what lessons these events taught the computing industry.
```

**Recommended**:
```
Skill: Analyze historical computing failures and extract lessons
Description: Students study famous software bugs and system failures (Ariane 5 rocket, Y2K problem, Therac-25), explain what went wrong in each case, and identify specific lessons these events taught the computing industry (importance of testing, documentation, fail-safes, diverse teams).
```

**Rationale**: More active verb, adds "what went wrong" analysis, specifies types of lessons.

---

### 2. Add New Skill - Programming Language Evolution (MEDIUM Priority)

**Gap Identified**: T34 covers hardware evolution, social impact, and pioneers, but lacks explicit coverage of programming language history.

**Proposed New Skill**:

```
ID: T34.G5.04
Topic: T34 – Computing History
Skill: Trace the evolution of programming languages
Description: Students create a timeline showing the evolution of how humans communicate with computers: machine code (1940s), assembly language (1950s), early high-level languages (FORTRAN, COBOL), visual languages (Logo, Scratch), and modern languages (Python, JavaScript). They explain why each generation was created (solving what problem, making programming more accessible to whom) and connect this history to their own coding experiences in CreatiCode.

Dependencies:
* T34.G4.01: Analyze cause/effect chains in computing history
* T34.G4.03: Link hardware evolution to modern software features
```

**Rationale**:
- Programming languages are central to computing history
- Directly connects to students' own coding experiences
- Fits naturally in Grade 5 (between hardware evolution in G4 and social movements in G5)
- Provides foundation for understanding why Scratch/CreatiCode exists (visual programming revolution)

**Impact on other skills**: None - no existing dependencies need updating.

---

### 3. Optional Enhancement - Strengthen Grade K Foundation (LOW Priority)

**Proposed Addition**:

```
ID: T34.GK.04
Topic: T34 – Computing History
Skill: Sequence their own day using technology
Description: Students draw or place picture cards showing their day from morning to night (wake up, breakfast, school, play, dinner, bedtime) and circle or mark the times when they use technology (tablet, TV, computer, smart speaker). They count how many times they use technology and share one favorite technology moment.

Dependencies:
* T01.GK.01: Put pictures in order for getting ready for bed
```

**Rationale**:
- Builds foundational sequencing that supports later timeline work (G3.01, G5.02)
- Helps students recognize computing in their own lives (connects to GK.01)
- Age-appropriate (picture-based, personal reflection)
- Strengthens K foundation (currently only 3 skills vs 3+ in other grades)

**Impact**: Would require updating T34.G1.01 to optionally depend on this (not required).

**Recommendation**: OPTIONAL - current K skills are adequate, but this would enhance progression.

---

### 4. Consider UI Evolution Coverage (LOW Priority)

**Gap**: User interface evolution is only implicit (touchscreens mentioned in G4.03, but no comprehensive coverage).

**Option A - Add new skill**:
```
ID: T34.G6.04
Topic: T34 – Computing History
Skill: Analyze evolution of user interfaces
Description: Students research how people interacted with computers over time (punch cards 1960s, command line 1970s-80s, mouse+GUI 1980s-2000s, touchscreen 2000s-present, voice/gesture 2010s-present) and create a comparison showing how each change made computing more accessible. They connect UI evolution to accessibility and inclusion.

Dependencies:
* T34.G5.02: Compare invention timelines across industries
* T34.G4.03: Link hardware evolution to modern software features
```

**Option B - Integrate into existing skill**:
Expand T34.G6.02 (inclusion/exclusion) to explicitly include UI evolution as a factor in computing access.

**Recommendation**: **Option B** - Integrate into T34.G6.02 description rather than creating standalone skill.

**Updated T34.G6.02 description**:
```
Skill: Evaluate historical inclusion and exclusion in computing
Description: Learners examine who gained or lacked access to computing historically due to multiple factors: cost (mainframes vs personal computers), geography (urban vs rural, global digital divide), language (English-dominant early systems), disability (pre-accessibility features), and interface complexity (command-line vs GUI vs touchscreen). They connect these historical patterns to current access barriers and inclusion efforts.
```

---

## Implementation Checklist

### Must Do (Before finalizing T34)

- [ ] Update T34.G1.03 description (more specific)
- [ ] Update T34.G2.02 description (add chart structure)
- [ ] Update T34.G5.01 description (clarify scope - Option A recommended)
- [ ] Update T34.G6.01 description (remove prediction)
- [ ] Update T34.G6.03 skill name and description (active verb)

### Should Do (Recommended for completeness)

- [ ] Add T34.G5.04 (programming language evolution)
- [ ] Update T34.G6.02 description (integrate UI evolution)

### Optional Enhancements

- [ ] Add T34.GK.04 (sequencing day with technology)
- [ ] Add optional CreatiCode mention to T34.G3.01 (interactive timeline)

---

## Validation Checklist

After making changes, verify:

### Internal Coherence
- [ ] All 27 (or 28 with G5.04) skills have clear, actionable descriptions
- [ ] Skills progress logically K→8 with increasing complexity
- [ ] Each skill is appropriately scoped (not too broad/narrow)

### Dependencies
- [ ] No forward references (skills only depend on earlier grades or same grade)
- [ ] All follow X-2 rule (max 2-grade gap)
- [ ] New T34.G5.04 dependencies are valid (G4.01 and G4.03)
- [ ] If T34.GK.04 added, verify it doesn't create issues

### Grade Appropriateness
- [ ] K-2 remain picture-based/unplugged (no coding required)
- [ ] Grade 3+ appropriately leverage research and creation
- [ ] Complexity increases steadily K→8

### Cross-Topic Dependencies
- [ ] Existing 4 cross-topic dependencies (T01, T03) preserved
- [ ] No new cross-topic dependencies introduced (or if introduced, they're justified)

### Completeness
- [ ] Major computing history topics covered: hardware, software, languages, pioneers, social impact, failures, policies
- [ ] Diversity and inclusion emphasized throughout (pioneers from diverse backgrounds, access barriers, social movements)
- [ ] Balance of knowledge acquisition and creation/presentation skills

---

## Summary of Changes

### Required Changes (5)
1. T34.G1.03 description - more specific examples
2. T34.G2.02 description - add chart structure
3. T34.G5.01 description - clarify scope
4. T34.G6.01 description - remove prediction
5. T34.G6.03 name + description - active verb

### Recommended Additions (2)
1. T34.G5.04 - programming language evolution (NEW SKILL)
2. T34.G6.02 - expand to include UI evolution (ENHANCE EXISTING)

### Optional Additions (2)
1. T34.GK.04 - sequence day with technology (NEW SKILL)
2. T34.G3.01 - mention interactive timeline option (ENHANCE EXISTING)

---

## Expected Outcomes

After implementing required and recommended changes:

- **Clarity**: All skills have specific, actionable descriptions with clear deliverables
- **Completeness**: Programming language evolution gap filled
- **Consistency**: Active verbs throughout, consistent structure
- **Coverage**: All major computing history topics addressed
- **Coherence**: Clean progression K→8 with no dependency issues

**Total skills after optimization**: 27 (current) + 1 (G5.04) = **28 skills**

If optional GK.04 added: **29 skills** (4+3+3+3+4+3+3+3+3 across K-8)

---

## Notes for Phase 2

**Preserve these cross-topic dependencies**:
- T01.G1.01 (Sequencing) - used by G2.01, G2.03
- T01.G1.10 (Conditionals) - used by G2.02
- T03.G1.03 (Decomposition) - used by G2.02

These are foundational CT skills appropriately leveraged for historical analysis and timeline creation.

**Potential future connections** (not for Phase 1):
- T34 computing history could inform T35 (Impacts & Ethics) discussions
- T34 hardware evolution connects to T31 (Networks) and T32 (Hardware)
- T34 programming language evolution connects to early coding topics (T01-T03)

But these are conceptual connections, not hard dependencies. Keep T34 relatively self-contained.
