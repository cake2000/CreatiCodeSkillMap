# T34 Computing History - Exact Changes Required

This document provides the exact text replacements needed to optimize T34.

---

## REQUIRED CHANGES (5 Skills)

### Change 1: T34.G1.03 Description

**FIND (line ~15756-15761):**
```
ID: T34.G1.03
Topic: T34 – Computing History
Skill: Explain that technology choices shape games/apps
Description: Learners state that creators pick characters, rules, and visuals, highlighting human design decisions.

Dependencies:
* T34.G1.01: Describe life before and after a technology
```

**REPLACE WITH:**
```
ID: T34.G1.03
Topic: T34 – Computing History
Skill: Identify design choices in games/apps
Description: Learners examine 2-3 simple games or apps and identify specific design choices creators made (character selection, color scheme, sound effects, game rules). They explain one choice they would make differently and why, demonstrating that technology reflects human decisions.

Dependencies:
* T34.G1.01: Describe life before and after a technology
```

---

### Change 2: T34.G2.02 Description

**FIND (line ~15774-15783):**
```
ID: T34.G2.02
Topic: T34 – Computing History
Skill: Identify communities impacted by inventions
Description: Learners analyze a case (screen readers, online maps) and list groups that gained access.

Dependencies:
* T34.G1.02: Recognize inventors from diverse backgrounds
* T01.G1.10: Match pictures to "if/then" rules
* T03.G1.03: List steps for a simple classroom routine
```

**REPLACE WITH:**
```
ID: T34.G2.02
Topic: T34 – Computing History
Skill: Identify communities impacted by inventions
Description: Learners analyze a case study (screen readers, online maps, or video captioning) and create a simple chart showing: (1) what problem existed before the invention, (2) which communities were affected by this problem, (3) how the invention helped these communities gain access.

Dependencies:
* T34.G1.02: Recognize inventors from diverse backgrounds
* T01.G1.10: Match pictures to "if/then" rules
* T03.G1.03: List steps for a simple classroom routine
```

---

### Change 3: T34.G5.01 Description

**FIND (line ~15853-15861):**
```
ID: T34.G5.01
Topic: T34 – Computing History
Skill: Investigate social movements linked to computing
Description: Learners research how computing supported social causes (accessibility advocacy, community organizing, open-source movements) and analyze both historical movements and current initiatives.

Dependencies:
* T34.G4.01: Analyze cause/effect chains in computing history
* T34.G4.02: Compare regional computing histories
```

**REPLACE WITH:**
```
ID: T34.G5.01
Topic: T34 – Computing History
Skill: Investigate social movements linked to computing
Description: Learners research how computing supported social causes (accessibility advocacy, community organizing, open-source movements) from the 1960s to present day. They create a timeline showing 3-4 key movements and analyze how each used computing tools, then compare one historical movement (e.g., 1980s accessibility advocacy) to a current digital activism initiative.

Dependencies:
* T34.G4.01: Analyze cause/effect chains in computing history
* T34.G4.02: Compare regional computing histories
```

---

### Change 4: T34.G6.01 Description

**FIND (line ~15883-15891):**
```
ID: T34.G6.01
Topic: T34 – Computing History
Skill: Analyze waves of computing (mainframe → mobile → AI)
Description: Students build comparison charts showing key characteristics (dominant hardware, typical users, limitations) for each computing era and make predictions about the next wave.

Dependencies:
* T34.G5.01: Investigate social movements linked to computing
* T34.G5.02: Compare invention timelines across industries
```

**REPLACE WITH:**
```
ID: T34.G6.01
Topic: T34 – Computing History
Skill: Analyze waves of computing (mainframe → mobile → AI)
Description: Students build comparison charts showing key characteristics (dominant hardware, typical users, limitations, societal impact) for each computing era (mainframe 1950s-70s, personal computing 1980s-2000s, mobile 2000s-2010s, AI/cloud 2010s-present), identifying patterns in how each wave emerged and evolved.

Dependencies:
* T34.G5.01: Investigate social movements linked to computing
* T34.G5.02: Compare invention timelines across industries
```

---

### Change 5: T34.G6.03 - Skill Name AND Description

**FIND (line ~15903-15911):**
```
ID: T34.G6.03
Topic: T34 – Computing History
Skill: Learn from historical computing failures
Description: Students study famous software bugs and system failures (Ariane 5 rocket, Y2K problem, Therac-25) and explain what lessons these events taught the computing industry.

Dependencies:
* T34.G5.01: Investigate social movements linked to computing
* T34.G5.02: Compare invention timelines across industries
```

**REPLACE WITH:**
```
ID: T34.G6.03
Topic: T34 – Computing History
Skill: Analyze historical computing failures and extract lessons
Description: Students study famous software bugs and system failures (Ariane 5 rocket, Y2K problem, Therac-25), explain what went wrong in each case, and identify specific lessons these events taught the computing industry (importance of testing, documentation, fail-safes, diverse teams).

Dependencies:
* T34.G5.01: Investigate social movements linked to computing
* T34.G5.02: Compare invention timelines across industries
```

---

## RECOMMENDED ADDITION (1 New Skill)

### Addition 1: T34.G5.04 - Programming Language Evolution

**INSERT AFTER T34.G5.03 (after line ~15881):**

```
ID: T34.G5.04
Topic: T34 – Computing History
Skill: Trace the evolution of programming languages
Description: Students create a timeline showing the evolution of how humans communicate with computers: machine code (1940s), assembly language (1950s), early high-level languages (FORTRAN, COBOL in 1950s-60s), structured languages (C, Pascal in 1970s), visual languages (Logo 1967, Scratch 2000s), and modern languages (Python, JavaScript). They explain why each generation was created (solving what problem, making programming more accessible to whom) and connect this history to their own coding experiences in CreatiCode and other platforms.

Dependencies:
* T34.G4.01: Analyze cause/effect chains in computing history
* T34.G4.03: Link hardware evolution to modern software features


```

**NOTE**: This new skill will require updating downstream dependencies:
- T34.G6.01, T34.G6.02, T34.G6.03 may optionally reference T34.G5.04
- BUT not required - keep current dependencies as-is

---

## RECOMMENDED ENHANCEMENT (1 Existing Skill)

### Enhancement 1: T34.G6.02 - Expand for UI Evolution

**FIND (line ~15893-15901):**
```
ID: T34.G6.02
Topic: T34 – Computing History
Skill: Evaluate historical inclusion and exclusion in computing
Description: Learners examine who gained or lacked access to computing historically (by cost, geography, language, disability) and connect these patterns to current access barriers and inclusion efforts.

Dependencies:
* T34.G5.01: Investigate social movements linked to computing
* T34.G5.03: Conduct interviews about technology changes
```

**REPLACE WITH:**
```
ID: T34.G6.02
Topic: T34 – Computing History
Skill: Evaluate historical inclusion and exclusion in computing
Description: Learners examine who gained or lacked access to computing historically due to multiple factors: cost (mainframes vs personal computers), geography (urban vs rural, global digital divide), language (English-dominant early systems), disability (pre-accessibility features), and interface complexity (command-line vs GUI vs touchscreen vs voice). They connect these historical patterns to current access barriers and inclusion efforts.

Dependencies:
* T34.G5.01: Investigate social movements linked to computing
* T34.G5.03: Conduct interviews about technology changes
```

---

## OPTIONAL ADDITIONS (2)

### Optional 1: T34.GK.04 - Strengthen Grade K

**INSERT AFTER T34.GK.03 (after line ~15733):**

```
ID: T34.GK.04
Topic: T34 – Computing History
Skill: Sequence their own day using technology
Description: Students draw or place picture cards showing their day from morning to night (wake up, breakfast, school, play, dinner, bedtime) and circle or mark the times when they use technology (tablet, TV, computer, smart speaker). They count how many times they use technology and share one favorite technology moment.

Dependencies:
* T01.GK.01: Put pictures in order for getting ready for bed


```

**OPTIONAL CONSEQUENCE**: Could update T34.G1.01 to also depend on T34.GK.04, but NOT required.

---

### Optional 2: T34.G3.01 - Add CreatiCode Extension Mention

**FIND (line ~15796-15803):**
```
ID: T34.G3.01
Topic: T34 – Computing History
Skill: Sequence milestones on a timeline
Description: Learners order cards showing key computing milestones (first programmable loom, ENIAC, early personal computers, smartphones) chronologically and note each decade.

Dependencies:
* T34.G2.01: Build "then vs now" comparison charts
```

**REPLACE WITH:**
```
ID: T34.G3.01
Topic: T34 – Computing History
Skill: Sequence milestones on a timeline
Description: Learners order cards showing key computing milestones (first programmable loom, ENIAC, early personal computers, smartphones) chronologically and note each decade. Advanced extension: Students can create an interactive timeline in CreatiCode where clicking each milestone reveals additional details.

Dependencies:
* T34.G2.01: Build "then vs now" comparison charts
```

---

## IMPLEMENTATION ORDER

1. **Make required changes first** (5 description updates)
2. **Add recommended new skill** (T34.G5.04)
3. **Make recommended enhancement** (T34.G6.02 expansion)
4. **Decide on optional additions** (GK.04 and G3.01 CreatiCode mention)
5. **Validate** using T34_VALIDATION_CHECKLIST.md
6. **Create summary** of changes made

---

## VERIFICATION STEPS

After making each change:

1. **Check line numbers**: They may shift as you add/modify text
2. **Verify formatting**: Maintain consistent spacing and structure
3. **Check dependencies**: Ensure dependency lists remain intact
4. **Validate skill IDs**: Ensure no duplicates (especially if adding GK.04 or G5.04)
5. **Test X-2 rule**: New skills must follow grade gap rules

---

## FILES TO UPDATE

- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` - Main skill file
- Create: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T34_changes_summary.md` - Document what changed

---

## EXPECTED FINAL COUNT

**Current**: 27 T34 skills (3 per grade K-8)

**After Required + Recommended**: 28 T34 skills
- K: 3 skills
- 1: 3 skills
- 2: 3 skills
- 3: 3 skills
- 4: 3 skills
- 5: **4 skills** (added G5.04)
- 6: 3 skills
- 7: 3 skills
- 8: 3 skills

**After All Optional**: 29 T34 skills
- K: **4 skills** (added GK.04)
- Grades 1-8: same as above

---

## NOTES

- All line numbers are approximate based on original file read
- Always search for exact text to find correct location
- Maintain blank lines between skills (formatting consistency)
- Dependencies must be indented with `* ` (asterisk + space)
- Preserve all existing cross-topic dependencies (T01, T03)
