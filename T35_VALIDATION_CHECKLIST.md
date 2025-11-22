# T35 Optimization Validation Checklist

Use this checklist after applying all changes to verify the optimization is complete and correct.

---

## PHASE 1: Dependency Validation

### Same-Grade Dependencies (NONE should remain)
- [ ] Verify T35.G6.03.01 does NOT depend on T35.G6.03
- [ ] Scan entire T35 file for any remaining same-grade dependencies (use regex: `T35\.G(\d)\..*T35\.G\1\.`)

### X-2 Rule Compliance (Grade X can only depend on X, X-1, X-2)
- [ ] T35.G3.* dependencies: Only GK, G1, G2, G3 allowed ✓
- [ ] T35.G4.* dependencies: Only G1, G2, G3, G4 allowed ✓
- [ ] T35.G5.* dependencies: Only G2, G3, G4, G5 allowed ✓
- [ ] T35.G6.* dependencies: Only G3, G4, G5, G6 allowed ✓
- [ ] T35.G7.* dependencies: Only G4, G5, G6, G7 allowed ✓
- [ ] T35.G8.* dependencies: Only G5, G6, G7, G8 allowed ✓

### Removed Dependencies (verify these are GONE)
- [ ] T35.G4.02: NO T04.G2.01 dependency
- [ ] T35.G5.03: NO T04.G2.01 dependency
- [ ] T35.G6.03.01: NO T35.G6.03 dependency
- [ ] T35.G8.01: NO T04.G2.01 dependency

### Cross-Topic Dependencies (verify these are PRESERVED)
- [ ] T01 dependencies intact (everyday algorithms foundation)
- [ ] T03 dependencies intact (decomposition)
- [ ] T04 dependencies intact (patterns - where still valid)
- [ ] T06 dependencies intact (events)
- [ ] T07 dependencies intact (loops)
- [ ] T08 dependencies intact (conditionals)
- [ ] T09 dependencies intact (variables)
- [ ] T16 dependencies added/intact (widgets) ⭐ NEW
- [ ] T19 dependencies added/intact (data/cloud) ⭐ NEW
- [ ] T21 dependencies added/intact (AI image generation) ⭐ NEW
- [ ] T22 dependencies added/intact (ChatGPT) ⭐ NEW
- [ ] T23 dependencies added/intact (perception AI) ⭐ NEW
- [ ] T24 dependencies added/intact (coding assistants) ⭐ NEW

---

## PHASE 2: Content Validation

### K-2 Skills (Must remain unplugged/picture-based)
- [ ] T35.GK.01-03: NO block coding mentioned ✓
- [ ] T35.G1.01-03: NO block coding mentioned ✓
- [ ] T35.G2.01-03: NO block coding mentioned ✓

### Grade 3-8 Skills (Must specify CreatiCode blocks/features)

#### Grade 3 Checklist
- [ ] T35.G3.01: Mentions widgets + ChatGPT blocks
- [ ] T35.G3.02: Mentions variables, conditionals, table variables
- [ ] T35.G3.03: Mentions widgets + AI moderation blocks
- [ ] T35.G3.04 ⭐NEW: Mentions widgets + variables for data tracking

#### Grade 4 Checklist
- [ ] T35.G4.01: Mentions widgets + table variables
- [ ] T35.G4.02: Mentions widgets + sprite design
- [ ] T35.G4.03: Mentions AI Speaker (TTS), keyboard controls, sprite properties

#### Grade 5 Checklist
- [ ] T35.G5.01: (Can remain discussion/research based - OK)
- [ ] T35.G5.02: (Can remain debate based - OK)
- [ ] T35.G5.03: (Analysis skill - OK as is)
- [ ] T35.G5.04 ⭐NEW: Mentions widgets + Google Sheets + table variables

#### Grade 6 Checklist
- [ ] T35.G6.01: Mentions widgets + table variables + ChatGPT
- [ ] T35.G6.02: Mentions widgets + cloud data blocks
- [ ] T35.G6.03: Mentions T21/T22 AI blocks + systematic testing
- [ ] T35.G6.03.01: (Guidelines can be document-based - OK)
- [ ] T35.G6.04: (Data interpretation - OK as is)
- [ ] T35.G6.05 ⭐NEW: Mentions widgets + cloud storage + conditional logic

#### Grade 7 Checklist
- [ ] T35.G7.01: Mentions T21/T22 blocks + table variables
- [ ] T35.G7.01.01: (Audit extension - OK)
- [ ] T35.G7.02: (Storyboard activity - OK as creative)
- [ ] T35.G7.03: (Position paper - OK as writing)
- [ ] T35.G7.04: Mentions T23 perception blocks + table logging
- [ ] T35.G7.05: Mentions T21 blocks + widgets for policy
- [ ] T35.G7.06: (Facilitation skill - OK)
- [ ] T35.G7.07 ⭐NEW: Mentions table variables + widgets + sprite graphics

#### Grade 8 Checklist
- [ ] T35.G8.01: (Comparative essay - OK as capstone analysis)
- [ ] T35.G8.01.01: (Impact analysis - OK)
- [ ] T35.G8.02: (Policy brief - OK as capstone writing)
- [ ] T35.G8.03: Mentions widgets + table variables + ChatGPT integration
- [ ] T35.G8.04: (Workshop design - OK as teaching skill)

---

## PHASE 3: Structural Validation

### New Skills Inserted Correctly
- [ ] T35.G3.04 exists after T35.G3.03 (before Grade 4 section)
- [ ] T35.G5.04 exists after T35.G5.03 (before Grade 6 section)
- [ ] T35.G6.05 exists after T35.G6.02 (before T35.G6.03)
- [ ] T35.G7.07 exists after T35.G7.06 (before Grade 8 section)

### Numbering and IDs
- [ ] All skill IDs follow format T35.G<grade>.<number>
- [ ] Sub-skills use .01 format (e.g., T35.G6.03.01, T35.G7.01.01, T35.G8.01.01)
- [ ] No duplicate IDs
- [ ] Sequence is logical within each grade

### Required Fields Present
For EACH skill verify:
- [ ] Skill ID (### T35.G#.##)
- [ ] Dependencies section (_Dependency:_ with bullet list)
- [ ] Short name (- **Short name:**)
- [ ] Description (- **Description:**)
- [ ] Challenge format (- **Challenge format:**)
- [ ] CSTA code (- **CSTA:**)
- [ ] AI4K12 code where appropriate (for AI-focused skills)

---

## PHASE 4: Coherence Validation

### Progression Check (Does each grade build on previous?)
- [ ] K→1: Helpful tech → categorizing choices (logical ✓)
- [ ] 1→2: Feelings about tech → comparing benefits/harms (logical ✓)
- [ ] 2→3: Balanced use → digital footprints & data collection (logical ✓)
- [ ] 3→4: Personal impact → community impact (logical ✓)
- [ ] 4→5: Community analysis → global/differential impacts (logical ✓)
- [ ] 5→6: Impact analysis → ethical frameworks + AI ethics (logical ✓)
- [ ] 6→7: Ethics guidelines → systematic bias audits (logical ✓)
- [ ] 7→8: Evidence gathering → framework application & policy (logical ✓)

### Scaffolding Check (Are dependencies logical?)
Sample dependency chains to verify:

**Digital Footprints Chain:**
- [ ] GK→G1→G2 (tech awareness)
- [ ] G2.01 → G3.01 → G3.04 (benefits/harms → footprints → data collection)

**Ethics Chain:**
- [ ] G4.01 → G5.01 → G6.01 (case studies → global impacts → ethics lenses)
- [ ] G6.01 → G7.02 → G8.01 (lenses → consequences → frameworks)

**AI Ethics Chain:**
- [ ] G5.03 → G6.03 → G7.01 (AI impacts → ethics guidelines → bias audits)
- [ ] G6.03 → G6.03.01 (content generation → perception/assistance)
- [ ] G7.01 → G7.01.01 (content audit → perception audit)

**Data Privacy Chain:**
- [ ] G5.01 → G6.02 → G6.05 (global impacts → privacy tradeoffs → consent)

### Coverage Check (Are all important topics covered?)
- [ ] Screen time & wellbeing (GK.02, G1.01, G2.02, G5.02)
- [ ] Online kindness & communication (GK.03, G2.03, G3.03)
- [ ] Digital footprints & privacy (G3.01, G3.04, G6.02, G6.05)
- [ ] Algorithms & persuasion (G3.02, G4.02)
- [ ] Accessibility & inclusion (G4.03)
- [ ] Global & differential impacts (G5.01, G5.03)
- [ ] Ethical frameworks (G6.01, G8.01)
- [ ] AI content generation ethics (G6.03, G7.01, G7.05)
- [ ] AI perception ethics (G6.03.01, G7.01.01, G7.04)
- [ ] Data visualization ethics (G7.07) ⭐NEW
- [ ] Impact assessment (G8.03)
- [ ] Digital divide (G6.04)

---

## PHASE 5: Technical Validation

### Assumed T16 Dependencies (Widgets)
Verify these T16 skills exist and are grade-appropriate:
- [ ] T16.G3.01: Add a label widget to display text
- [ ] T16.G4.01: Create interactive displays with widgets
- [ ] T16.G5.01: Build a simple survey using widgets
- [ ] T16.G6.01: Create forms with multiple widget types
- [ ] T16.G7.01: Build interactive data displays with widgets
- [ ] T16.G8.01: Build complex multi-widget applications

### Assumed T19 Dependencies (Data/Cloud)
Verify these T19 skills exist and are grade-appropriate:
- [ ] T19.G5.01: Store data in a Google Sheet using blocks
- [ ] T19.G6.01: Store and retrieve data from cloud tables
- [ ] T19.G7.01: Create data visualizations using table variables

### Assumed T21-T24 Dependencies (AI blocks)
Verify these AI topic skills exist and are grade-appropriate:
- [ ] T21.G6.01: Generate images with AI (DALL-E blocks)
- [ ] T21.G7.01: Generate complex images with AI
- [ ] T22.G3.01: Use ChatGPT blocks for simple queries
- [ ] T22.G4.01: Use AI Speaker for text-to-speech
- [ ] T22.G6.01: Use ChatGPT for complex conversations (or analysis tasks)
- [ ] T22.G8.01: Use ChatGPT for advanced analysis
- [ ] T23.G6.01: Use AI perception tools (hand/body tracking)
- [ ] T23.G7.01: Use hand and body tracking for interactive projects
- [ ] T24.G6.01: Use AI coding assistants

**If any of these don't exist:** Note which T35 skills need dependency adjustments.

---

## PHASE 6: Documentation Validation

### Challenge Formats Are Clear
- [ ] Each challenge format describes WHAT students produce
- [ ] Rubrics mention specific elements to assess
- [ ] Grade 3-8 challenge formats mention code artifacts where appropriate

### Descriptions Are Actionable
- [ ] K-2: Descriptions use observable behaviors (sort, match, pick, circle)
- [ ] Grade 3-8: Descriptions specify building/coding actions (create, build, test, implement)
- [ ] No vague verbs like "discuss" or "analyze" without context

### CSTA Codes Are Appropriate
- [ ] K-2: EK/E1/E2 codes (elementary)
- [ ] Grade 3-5: E3/E4/E5 codes (elementary)
- [ ] Grade 6-8: MS codes (middle school)
- [ ] AI skills include AI4K12 codes

---

## PHASE 7: Final Sanity Checks

### No Orphaned Skills
- [ ] Every skill (except GK/G1 entry skills) has at least one dependency
- [ ] Every skill is a dependency for at least one later skill (check using reverse lookup)

### No Circular Dependencies
- [ ] No skill depends on itself through any chain
- [ ] Dependencies always point to earlier grades (never forward)

### No Broken References
- [ ] All T## codes in dependencies reference real topics
- [ ] All T##.G#.## codes reference real skills (or reasonably expected skills)

### Reasonable Scope
- [ ] No skill tries to do too much (descriptions <150 words)
- [ ] Challenge formats are achievable in 1-3 class periods
- [ ] Grade level is appropriate for complexity

---

## PHASE 8: Spot Check - Read Through

Read these specific skills end-to-end to verify quality:

### Sample K-2 Skill
- [ ] T35.GK.02: Clear picture-based activity? Age appropriate?

### Sample Grade 3 Skill
- [ ] T35.G3.01: Transition to coding? Uses widgets + ChatGPT appropriately?

### Sample Grade 4-5 Skill
- [ ] T35.G4.02: Concrete demonstration of persuasion? Clear comparison?

### Sample Grade 6 Skill
- [ ] T35.G6.02: Working privacy demo? Uses cloud blocks appropriately?

### Sample Grade 7 Skill
- [ ] T35.G7.04: Uses T23 blocks? Connects to ethics meaningfully?

### Sample Grade 8 Skill
- [ ] T35.G8.03: Capstone-appropriate? Integrates multiple tools?

---

## COMPLETION CHECKLIST

- [ ] All Phase 1 checks complete (Dependencies)
- [ ] All Phase 2 checks complete (Content)
- [ ] All Phase 3 checks complete (Structure)
- [ ] All Phase 4 checks complete (Coherence)
- [ ] All Phase 5 checks complete (Technical)
- [ ] All Phase 6 checks complete (Documentation)
- [ ] All Phase 7 checks complete (Sanity)
- [ ] All Phase 8 checks complete (Spot checks)

---

## SIGN-OFF

**Date validated:** __________

**Validated by:** __________

**Issues found:** (list any problems discovered)

**Issues resolved:** (list how problems were fixed)

**Ready for integration:** [ ] YES [ ] NO

---

## NOTES FOR FUTURE OPTIMIZATION

(Use this space to note any additional improvements that could be made in future iterations)

-
-
-

---

## QUICK GREP COMMANDS FOR VALIDATION

```bash
# Find all T35 skills
grep "^### T35\." skillsv4/skills_T35_impacts.md

# Find all dependencies in T35
grep -A 10 "^### T35\." skillsv4/skills_T35_impacts.md | grep "  \* T"

# Check for same-grade dependencies (should return NOTHING)
grep -E "T35\.G(\d+)\..*T35\.G\1\." skillsv4/skills_T35_impacts.md

# Check for T04.G2.01 dependencies (should return NOTHING)
grep "T04\.G2\.01" skillsv4/skills_T35_impacts.md

# Count skills per grade
grep "^### T35\.GK\." skillsv4/skills_T35_impacts.md | wc -l  # Should be 3
grep "^### T35\.G1\." skillsv4/skills_T35_impacts.md | wc -l  # Should be 3
grep "^### T35\.G2\." skillsv4/skills_T35_impacts.md | wc -l  # Should be 3
grep "^### T35\.G3\." skillsv4/skills_T35_impacts.md | wc -l  # Should be 4 (was 3)
grep "^### T35\.G4\." skillsv4/skills_T35_impacts.md | wc -l  # Should be 3
grep "^### T35\.G5\." skillsv4/skills_T35_impacts.md | wc -l  # Should be 4 (was 3)
grep "^### T35\.G6\." skillsv4/skills_T35_impacts.md | wc -l  # Should be 5 (was 4)
grep "^### T35\.G7\." skillsv4/skills_T35_impacts.md | wc -l  # Should be 7 (was 6)
grep "^### T35\.G8\." skillsv4/skills_T35_impacts.md | wc -l  # Should be 4

# Check for widget mentions in Grade 3-8
grep -A 5 "^### T35\.G[3-8]" skillsv4/skills_T35_impacts.md | grep -i "widget"

# Check for AI block mentions in Grade 6-8
grep -A 5 "^### T35\.G[6-8]" skillsv4/skills_T35_impacts.md | grep -i "chatgpt\|T21\|T22\|T23\|T24"
```
