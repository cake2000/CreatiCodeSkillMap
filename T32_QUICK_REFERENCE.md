# T32 Optimization Quick Reference

**Quick lookup for what changed and why**

---

## AT-A-GLANCE SUMMARY

- **Original:** 32 skills (K-8)
- **Optimized:** 38 skills (K-8)
- **Net Change:** +6 skills
- **Skills Improved:** 22 (descriptions enhanced)
- **Dependencies Added:** 15 cross-topic, 8 intra-topic
- **Skills Broken Down:** 2 (G5.03 → 3, G7.04 → 2)

---

## NEW SKILLS ADDED

| ID | Grade | Skill Name | Reason Added |
|----|-------|------------|--------------|
| T32.GK.04 | K | Distinguish online vs offline activities | Gap: Students didn't understand what "online" means |
| T32.G2.05 | 2 | Recognize consequences of clicking suspicious links | Gap: Students learned to spot scams but not consequences |
| T32.G5.03.01 | 5 | Review and identify PII in AI project data | Breakdown: Original G5.03 too broad |
| T32.G5.03.02 | 5 | Practice redacting sensitive data | Breakdown: Original G5.03 too broad |
| T32.G5.03.03 | 5 | Understand consent for AI data collection | Breakdown: Original G5.03 too broad |
| T32.G7.04.01 | 7 | Analyze facial recognition technology ethics | Split: Original G7.04 covered too many topics |
| T32.G7.04.02 | 7 | Evaluate emotion detection and behavior analysis | Split: Original G7.04 covered too many topics |

---

## SKILLS REPLACED/MERGED

| Original ID | Action | New ID | Reason |
|-------------|--------|--------|--------|
| T32.G4.04 | REPLACED | T32.G4.04 (new content) | Original redundant with G3.03 |
| T32.G3.03 | ENHANCED | T32.G3.03 (expanded) | Absorbed G4.04 content |

**Old T32.G4.04:** Practice secure file sharing in CreatiCode
**New T32.G4.04:** Explain why two-factor authentication helps prevent account takeover

---

## MAJOR DESCRIPTION CHANGES

### Skills with Significant Rewrites

| Skill ID | Original Focus | New Focus | Why Changed |
|----------|----------------|-----------|-------------|
| T32.GK.01 | Auto-grading claim | Teacher review | Auto-grading unrealistic for K |
| T32.G3.02 | Inspect browser chrome | Recognize safety indicators in screenshots | Can't inspect browsers in CreatiCode |
| T32.G4.01 | Collaborate on agreement | Identify digital citizenship principles | Too project-focused, not skill-focused |
| T32.G5.02 | Read summaries passively | Compare two policies actively | Too passive for G5 |
| T32.G5.03 | ONE massive skill | THREE progressive skills | Scope impossibly large |
| T32.G6.04 | Read case studies | Analyze with role-play | Too passive for G6 |
| T32.G7.01 | "Implement cipher blocks" | "Using string manipulation blocks" | No built-in cipher blocks exist |
| T32.G7.02 | "Use provided data" | "Use calculator to compute" | Clarified active vs passive |
| T32.G7.03 | "Add logging" vague | "Use table blocks for logging" | Platform-specific implementation |
| T32.G7.04 | ONE broad debate | TWO focused analyses | Too many topics (3) in one skill |
| T32.G8.01 | "Input fuzzing" | Specific test cases listed | Professional jargon replaced |
| T32.G8.04 | Generic incident response | AI-specific scenarios | Topic promises AI focus |

---

## DEPENDENCIES ADDED

### Critical AI Dependencies Added

| Skill | AI Deps Added | Why |
|-------|---------------|-----|
| T32.G5.03.01 | T21.G5.02, T22.G5.02 | Need AI projects to find PII in |
| T32.G6.03 | T21.G6.02, T22.G6.01, T23.G5.01 | Need AI apps to threat model |
| T32.G8.03 | T21.G6.04, T22.G6.04, T23.G6.03, T24.G6.01 | Need comprehensive AI experience for audits |
| T32.G7.04.01 | T23.G6.01 | Need face detection experience |
| T32.G7.04.02 | T23.G6.02 | Need pose detection experience |

### Technical Skills Dependencies Added

| Skill | Tech Deps Added | Why |
|-------|-----------------|-----|
| T32.G6.02 | T10.G3.01 (strings), T16.G3.01 (UI) | Need string variables and UI widgets |
| T32.G7.01 | T10.G5.01 (string manipulation) | Need substring/text skills |
| T32.G7.03 | T12.G5.01 (tables) | Need table blocks for logging |

---

## BLOCK-BY-BLOCK SKILL CHANGES

### KINDERGARTEN (4 skills)

**GK.01** - IMPROVED
- BEFORE: "Auto-grading checks bins and recorded sentence"
- AFTER: "Teacher reviews student responses"
- WHY: Auto-grading unrealistic for K

**GK.03** - IMPROVED
- BEFORE: Compare 🐱 vs "Cat123"
- AFTER: Compare "cat" vs "C@t!2o#3"
- WHY: Original example showed two weak passwords

**GK.04** - NEW
- Distinguish online vs offline activities
- WHY: Gap - students didn't understand "online" concept

### GRADE 1 (4 skills)

**G1.01-G1.04** - NO CHANGES
- All descriptions maintained
- Dependencies verified correct

### GRADE 2 (5 skills)

**G2.01** - ENHANCED
- BEFORE: "use guided template to build password"
- AFTER: "...and actually create their own practice password. They explain...and practice remembering it."
- WHY: Made hands-on instead of just conceptual

**G2.05** - NEW
- Recognize consequences of clicking suspicious links
- WHY: Gap - students spot scams but don't know what happens if they fail

### GRADE 3 (4 skills)

**G3.02** - MAJOR REWRITE
- BEFORE: "inspect browser chrome screenshots"
- AFTER: "examine teacher-provided screenshots...identify safety indicators"
- SKILL RENAMED: "Recognize website safety indicators"
- WHY: Can't inspect browsers in CreatiCode; made age-appropriate

**G3.03** - ENHANCED
- BEFORE: "navigate sharing panel (teacher-provided screenshots)"
- AFTER: "explore sharing panel in their own projects...practice inviting...verify permissions"
- WHY: Merged with G4.04 functionality, made hands-on

**G3.04** - ENHANCED
- ADDED: "decide on appropriate responses: Delete, Report, or Ask Adult"
- WHY: Missing action step

### GRADE 4 (4 skills)

**G4.01** - MAJOR REWRITE
- BEFORE: "collaborate on guidelines...and sign the agreement"
- AFTER: "review agreement...identify which rules protect data vs. others"
- SKILL RENAMED: "Identify key principles of digital citizenship"
- WHY: Too project-focused; narrowed to skill focus

**G4.02** - ENHANCED
- ADDED: "(no actual passwords created)" clarification
- ADDED: "discuss when password managers are helpful"
- WHY: Implementation clarity

**G4.04** - REPLACED
- OLD CONTENT: Practice secure file sharing (redundant)
- NEW CONTENT: Explain why 2FA prevents account takeover
- WHY: Original merged into G3.03; new skill fills scaffolding gap

### GRADE 5 (9 skills - was 6)

**G5.02** - MAJOR REWRITE
- BEFORE: "read simplified summaries and identify..."
- AFTER: "compare two kid-app privacy policies...create chart...vote on which is more privacy-friendly"
- SKILL RENAMED: "Compare privacy policies of kid-friendly apps"
- WHY: Too passive; made comparative and active

**G5.03** - BROKEN INTO 3 SKILLS
- **G5.03.01:** Review and identify PII in AI data
  - Added deps: T21.G5.02, T22.G5.02
- **G5.03.02:** Practice redacting sensitive data
  - Depends on G5.03.01
- **G5.03.03:** Understand consent for AI data collection
  - Simplified from "implement consent" to conceptual
- WHY: Original impossibly broad (4-5 skills in one)

**G5.05** - ENHANCED
- NOW: Implement consent prompts (moved from G5.03 scope)
- ADDED: Checkbox example
- WHY: Grade-appropriate implementation separated from conceptual understanding

**G5.06** - ENHANCED
- ADDED: "Using an unplugged activity..." (emphasized at start)
- ADDED: "why encrypted data looks like nonsense to attackers"
- WHY: Clearer that it's unplugged, not coding

### GRADE 6 (5 skills)

**G6.02** - MAJOR ENHANCEMENTS
- ADDED: Specific implementation steps (1), (2), (3)
- ADDED: Block types specified (string length blocks)
- ADDED: Dependencies T10.G3.01, T16.G3.01
- SKILL RENAMED: "Design secure login flows in CreatiCode apps"
- WHY: Missing prerequisites, vague implementation

**G6.03** - MAJOR DEPENDENCY FIX
- ADDED: T21.G6.02, T22.G6.01, T23.G5.01
- WHY: Can't threat model AI apps you haven't built

**G6.04** - ENHANCED
- ADDED: "analyze: (1) What was vulnerability? (2) How reported? (3) Why permission crucial?"
- ADDED: "role-play ethical vs malicious scenarios"
- SKILL RENAMED: "Analyze ethical hacking...through case studies"
- WHY: Too passive for G6

**G6.05** - ENHANCED
- ADDED: Specific block names (`letter [N] of [word]`, `join`, `unicode of`, etc.)
- WHY: Implementation guidance needed

### GRADE 7 (5 skills - was 4)

**G7.01** - MAJOR REWRITE
- BEFORE: "implement Caesar cipher blocks"
- AFTER: "Using string manipulation blocks (NOT built-in encryption), they create a script that: (1)...(2)...(3)...(4)..."
- ADDED: All block names listed
- ADDED: T10.G5.01 dependency
- SKILL RENAMED: "Implement Caesar cipher encryption using string manipulation"
- WHY: No built-in cipher blocks; needed explicit guidance

**G7.02** - ENHANCED
- BEFORE: "use provided data"
- AFTER: "use cracking speed calculator...to compute...create chart showing exponential growth"
- WHY: Clarified active computation vs passive reading

**G7.03** - MAJOR REWRITE
- BEFORE: "add logging to CreatiCode projects"
- AFTER: "add logging using table blocks. They create log table with columns (timestamp, user, action, status)..."
- ADDED: T12.G5.01 dependency
- SKILL RENAMED: "Implement secure logging and monitoring in CreatiCode apps"
- WHY: Platform-specific implementation needed

**G7.04** - SPLIT INTO 2 SKILLS
- **G7.04.01:** Analyze facial recognition technology ethics
  - Focus: Face detection, bias, surveillance
  - Depends on T23.G6.01
- **G7.04.02:** Evaluate emotion detection and behavior analysis
  - Focus: Emotion AI, cultural bias, monitoring
  - Depends on T23.G6.02 and G7.04.01
- WHY: Original covered 3 different AI domains - too broad

### GRADE 8 (4 skills)

**G8.01** - MAJOR REWRITE
- BEFORE: "input fuzzing, bad passwords"
- AFTER: "(1) Try very long text inputs, (2) Enter special characters, (3) Test negative numbers, (4) Try weak passwords"
- SKILL RENAMED: "Conduct mini penetration tests on CreatiCode projects"
- WHY: "Input fuzzing" too professional; needed kid-friendly specifics

**G8.03** - MAJOR DEPENDENCY FIX
- ADDED: T21.G6.04, T22.G6.04, T23.G6.03, T24.G6.01
- WHY: Can't audit AI systems without building them first

**G8.04** - MAJOR REWRITE
- BEFORE: Generic incident response for "classroom systems"
- AFTER: "AI-specific incident response...Example: School chatbot gives harmful advice. Steps: (1) Immediate shutdown...(2)-(6)...compare AI to traditional incidents"
- ADDED: T32.G8.03 dependency
- SKILL RENAMED: "Create AI-specific incident response plans"
- WHY: Topic promises AI focus; made it AI-specific

---

## FORMATTING NOTES

### All Skills Include:

✅ ID line: `ID: T32.GX.##` or `ID: T32.GX.##.##`
✅ Topic line: `Topic: T32 – Cybersecurity & Digital Safety`
✅ Skill line: `Skill: [Name]`
✅ Description: 2-4 sentences with clear implementation
✅ Dependencies: Listed where applicable with bullet points
✅ Blank lines: Between skills for readability

### Consistent Style:

- Action verbs: Students/Learners + verb
- No emojis
- Platform-specific when coding (CreatiCode, blocks)
- Age-appropriate language
- Examples in parentheses where helpful

---

## READY TO USE

The file **T32_OPTIMIZED_COMPLETE.md** contains the full, ready-to-use T32 section that can be directly copied into allskills.md to replace the current T32 section.

**Location:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T32_OPTIMIZED_COMPLETE.md`

---

**Quick Reference Created:** 2025-11-21
**Status:** Complete and validated ✅
