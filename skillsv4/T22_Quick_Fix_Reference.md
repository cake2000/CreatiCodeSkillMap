# T22 (Chatbots & Prompting) - Quick Fix Reference

## CRITICAL FIXES NEEDED IMMEDIATELY

### Issue 1: Skill ID Naming Violations

**Problem**: Two skills use non-standard ID format with extra dots

#### Fix 1A: T22.G5.1.5 → T22.G5.15
```
CURRENT: T22.G5.1.5
RENAME TO: T22.G5.15
SKILL: Use a chatbot block to get AI responses
```

**Update these dependencies:**
- T22.G5.04 currently depends on T22.G5.1.5
- T22.G6.04.01 currently depends on T22.G5.1.5

**Change to:** T22.G5.15

---

#### Fix 1B: T22.G6.05.5 → T22.G6.055
```
CURRENT: T22.G6.05.5
RENAME TO: T22.G6.055
SKILL: Understand chatbot session types
```

**No dependencies need updating** (no other skills reference this one)

---

### Issue 2: Dependency Order Problems in Grade 5

**Problem**: T22.G5.04 depends on T22.G5.1.5, creating backward reference

**RECOMMENDED SOLUTION: Resequence Grade 5 Skills**

#### Current Sequence (BROKEN):
```
T22.G5.01: Flag risky vs safe chatbot prompts
  Deps: T06.G3.09, T09.G3.05, T22.G3.01

T22.G5.02: Observe chatbot strengths and weaknesses through testing
  Deps: T22.G4.01, T22.G5.01

T22.G5.03: Experiment with prompt phrasing to improve responses
  Deps: T22.G4.01, T22.G5.02

T22.G5.04: Identify ChatGPT block parameters in starter code
  Deps: T22.G5.1.5, T22.G5.02  ← DEPENDS ON LATER SKILL!

T22.G5.1.5: Use a chatbot block to get AI responses
  Deps: T09.G4.01, T22.G5.01, T22.G5.03  ← FOUNDATION SKILL COMES LAST!
```

#### Recommended Fixed Sequence:
```
T22.G5.01: Flag risky vs safe chatbot prompts (CONCEPTUAL)
  Deps: T06.G3.09, T09.G3.05, T22.G3.01
  [Keep as-is]

T22.G5.02: Use a chatbot block to get AI responses (FOUNDATION - MOVE UP)
  [Renamed from T22.G5.1.5]
  Deps: T09.G4.01, T22.G5.01
  [REMOVE dependency on G5.03 - circular!]

T22.G5.03: Observe chatbot strengths and weaknesses through testing
  [Renamed from T22.G5.02]
  Deps: T22.G4.01, T22.G5.01, T22.G5.02

T22.G5.04: Experiment with prompt phrasing to improve responses
  [Renamed from T22.G5.03]
  Deps: T22.G4.01, T22.G5.03

T22.G5.05: Identify ChatGPT block parameters in starter code
  [Renamed from T22.G5.04]
  Deps: T22.G5.02, T22.G5.03
```

**Dependencies that need updating:**
- T22.G6.04.01 deps: Change T22.G5.1.5 → T22.G5.02

---

## COMPLETE RENAMING MAP

### Grade 5 Renumbering
| Old ID | New ID | Skill Name | Action |
|--------|--------|------------|--------|
| T22.G5.01 | T22.G5.01 | Flag risky vs safe chatbot prompts | NO CHANGE |
| T22.G5.02 | T22.G5.03 | Observe chatbot strengths and weaknesses | RENUMBER |
| T22.G5.03 | T22.G5.04 | Experiment with prompt phrasing | RENUMBER |
| T22.G5.04 | T22.G5.05 | Identify ChatGPT block parameters | RENUMBER |
| T22.G5.1.5 | T22.G5.02 | Use a chatbot block to get AI responses | RENUMBER + MOVE |

### Grade 6 Renumbering
| Old ID | New ID | Skill Name | Action |
|--------|--------|------------|--------|
| T22.G6.05.5 | T22.G6.055 | Understand chatbot session types | RENAME ONLY |

---

## DEPENDENCY UPDATE CHECKLIST

### Skills That Reference T22.G5.1.5 (to be changed to T22.G5.02):
- [ ] T22.G5.05 (old T22.G5.04): Change dep from G5.1.5 → G5.02
- [ ] T22.G6.04.01: Change dep from G5.1.5 → G5.02

### Skills That Reference T22.G5.02 (to be changed to T22.G5.03):
- [ ] T22.G5.04 (old G5.03): Change dep from G5.02 → G5.03
- [ ] T22.G5.05 (old G5.04): Change dep from G5.02 → G5.03

### Skills That Reference T22.G5.03 (to be changed to T22.G5.04):
- [ ] T22.G5.02 (old G5.1.5): REMOVE this dependency (circular!)

---

## UPDATED GRADE 5 SKILLS (CORRECTED VERSION)

### T22.G5.01 (NO CHANGE)
- **Skill**: Flag risky vs safe chatbot prompts
- **Dependencies**:
  - T06.G3.09: Fix a behavior that runs at the wrong time
  - T09.G3.05: Trace code with variables to predict outcomes
  - T22.G3.01: Identify chatbot behavior from fixed button replies

### T22.G5.02 (RENAMED FROM G5.1.5, MOVED UP)
- **Skill**: Use a chatbot block to get AI responses
- **Description**: Students use the basic `OpenAI ChatGPT: request [PROMPT] result [VARIABLE]` block to send a simple message to ChatGPT and store the response in a variable. They build a minimal project that displays the AI's answer on the stage, learning the fundamental mechanics of making an AI request before exploring advanced features.
- **Dependencies**:
  - T09.G4.01: Build a simple string variable for name entry
  - T22.G5.01: Flag risky vs safe chatbot prompts

### T22.G5.03 (RENAMED FROM G5.02)
- **Skill**: Observe chatbot strengths and weaknesses through testing
- **Description**: Students use a pre-built CreatiCode chatbot project without modifying code. They test different types of questions (factual, creative, math, opinion) and document when the bot performs well vs. poorly. They create a simple chart showing "good at" vs "struggles with" categories based on their observations.
- **Dependencies**:
  - T22.G4.01: Write clear, polite questions for a helper bot
  - T22.G5.01: Flag risky vs safe chatbot prompts
  - T22.G5.02: Use a chatbot block to get AI responses

### T22.G5.04 (RENAMED FROM G5.03)
- **Skill**: Experiment with prompt phrasing to improve responses
- **Description**: Students take a question the chatbot answered poorly and systematically try variations: adding context ("I'm in 5th grade"), being more specific ("Explain in 2 sentences"), or providing an example format. They record which changes helped most and write a "prompting tip" based on their experiments.
- **Dependencies**:
  - T22.G4.01: Write clear, polite questions for a helper bot
  - T22.G5.03: Observe chatbot strengths and weaknesses through testing

### T22.G5.05 (RENAMED FROM G5.04)
- **Skill**: Identify ChatGPT block parameters in starter code
- **Description**: Students examine a simple CreatiCode project using the ChatGPT block and identify what each parameter does (mode, temperature, max length, session). They don't modify the code yet, but label screenshots showing where each parameter is and predict what happens if values change. This prepares them for tracing more complex scripts in G6.
- **Dependencies**:
  - T22.G5.02: Use a chatbot block to get AI responses
  - T22.G5.03: Observe chatbot strengths and weaknesses through testing

---

## UPDATED GRADE 6 SKILL (CORRECTED VERSION)

### T22.G6.055 (RENAMED FROM G6.05.5)
- **Skill**: Understand chatbot session types
- **Description**: Students learn the difference between single-turn requests (independent questions) and multi-turn conversations (maintaining context across exchanges). They identify when to use the basic request block versus when to manage sessions with the session parameter, understanding how context affects chatbot responses.
- **Dependencies**: (NO CHANGE)
  - T22.G6.01: Trace how a chatbot script processes each turn
  - T22.G6.02: Adjust temperature for response creativity
  - T22.G6.03: Handle streaming mode and long requests

---

## SEARCH & REPLACE COMMANDS

### Step 1: Rename G5.1.5 to G5.02 in all files
```bash
# In allskills.md - be careful with multi-step approach
# 1. First create placeholder
sed -i 's/T22\.G5\.1\.5/T22.G5.TEMP15/g' allskills.md

# 2. Continue with other renames...
```

### Step 2: Update all Grade 5 skills
**Note**: These need to be done in specific order to avoid conflicts

```bash
# Backup first!
cp allskills.md allskills_backup_before_t22_fixes.md

# Use a more careful approach - edit manually or use temporary IDs
```

---

## MANUAL EDIT LOCATIONS

### Locations to manually edit in allskills.md:

**Line ~13107**: Change ID from T22.G5.1.5 to T22.G5.02
**Line ~13113**: Update dependency reference in this skill

**Line ~13087**: Change ID from T22.G5.02 to T22.G5.03
**Line ~13082-13084**: Update dependencies

**Line ~13097**: Change ID from T22.G5.03 to T22.G5.04
**Line ~13092-13094**: Update dependencies

**Line ~13107**: Change ID from T22.G5.04 to T22.G5.05
**Line ~13102-13104**: Update dependencies

**Line ~13213**: Change ID from T22.G6.05.5 to T22.G6.055

**Line ~13163-13166**: T22.G6.04.01 dependencies - change G5.1.5 to G5.02

---

## ADDITIONAL IMPROVEMENTS (LOWER PRIORITY)

### Issue 3: Skills That Need Better Scope Definition

#### T22.G5.03 (old G5.02): Make deliverable more specific
**Current**: "create a simple chart showing 'good at' vs 'struggles with'"
**Suggest**: Add template or specify format (table with 3 rows minimum)

#### T22.G6.055 (old G6.05.5): Add hands-on component
**Current**: "Students learn the difference..." (too passive)
**Suggest**: "Students build two projects: one single-turn Q&A, one multi-turn conversation"

#### T22.G7.09: Break into smaller skills or add checklist
**Current**: "prepare at least four tester personas..."
**Suggest**: Create specific rubric or break into:
- G7.09a: Create test personas
- G7.09b: Run usability tests
- G7.09c: Document and fix issues

#### T22.G8.04: Consider breaking into 2 skills
**Current**: Testing harness + logging + reporting + timing + off-topic detection
**Suggest**:
- G8.04a: Build testing harness with prompt table
- G8.04b: Add automated reporting and quality metrics

---

## VALIDATION CHECKLIST

After making fixes, verify:

- [ ] No skill IDs use more than one decimal point (e.g., G5.1.5)
- [ ] All Grade 5 skills sequence properly (01, 02, 03, 04, 05)
- [ ] No forward dependencies (later skills depending on earlier ones)
- [ ] T22.G5.02 is referenced correctly in G6.04.01
- [ ] All old references to G5.1.5 are updated
- [ ] All old references to G5.02, G5.03, G5.04 are updated to new numbers
- [ ] G6.05.5 is renamed to G6.055 (or reorganized entirely)

---

## SUMMARY

**Critical Fixes (MUST DO)**:
1. Rename T22.G5.1.5 → T22.G5.02
2. Renumber T22.G5.02-G5.04 → T22.G5.03-G5.05
3. Fix circular dependency (remove G5.03 from G5.02 deps)
4. Rename T22.G6.05.5 → T22.G6.055
5. Update all dependency references

**Recommended Improvements (SHOULD DO)**:
1. Add deliverable specifics to G5.03
2. Add hands-on component to G6.055
3. Add rubric/scope to G7.09
4. Consider splitting G8.04

**Total Skills Affected**:
- 5 skills need renumbering (G5.02-G5.05, plus G5.1.5 moving to G5.02)
- 1 skill needs ID format fix (G6.05.5)
- 3-4 dependencies need updating
- 4 skills could use scope improvements
