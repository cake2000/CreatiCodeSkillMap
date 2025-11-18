# ACSL Content Exclusion Analysis
**Date:** 2025-11-17
**Purpose:** Identify and recommend exclusion/de-emphasis of ACSL-related theoretical content

---

## Executive Summary

The CreatiCode K-8 Skill Map currently contains **52 skills** with ACSL-related or overly theoretical content that doesn't align with the vision of **creative, practical, project-based learning**. This document categorizes each skill with recommendations: EXCLUDE, DE-EMPHASIZE, or REFRAME.

### Quick Stats
- **Explicit ACSL-tagged:** 1 skill (already marked as competition track)
- **Theoretical algorithm implementation:** 16 skills
- **Formal CS concepts:** 25 skills
- **Abstract analysis (no practical application):** 10 skills

### Key Finding
Most theoretical content is already properly handled through the **difficulty track system**:
- Competition-level algorithmic skills are marked `difficulty_track: "competition"`
- Standard curriculum focuses on USING tools, not implementing algorithms
- The Week 1 fix (T10.G8.02 → T10.G8.02-ADV) is the correct pattern

---

## Recommendation Categories

### EXCLUDE (Remove Entirely)
Skills that are too theoretical, not useful for creative projects, and better suited for competitive CS leagues.

### DE-EMPHASIZE (Mark as Optional/Advanced)
Skills that have value but shouldn't be required. Mark with `difficulty_track: "competition"` or `requires_advanced_cs: true`.

### REFRAME (Keep but Make Practical/Creative)
Skills worth keeping but need to focus on practical application rather than theoretical analysis.

### KEEP AS-IS
Skills that sound theoretical but actually support creative projects (e.g., planning tools, debugging).

---

## Detailed Analysis

## 1. EXPLICIT ACSL-TAGGED SKILLS (1 skill)

### ✅ ALREADY HANDLED - T10.G8.02-ADV

**Skill:** Implement a sorting algorithm (bubble or selection sort)
**Status:** `difficulty_track: "competition"`, `competition_tags: ['ACSL_junior']`
**Recommendation:** **KEEP AS-IS** - This is the correct pattern!

**Rationale:**
- Already separated from standard curriculum
- Marked as advanced/competition track
- Students in standard track use T10.G8.02 (use built-in sort tools)
- Students preparing for ACSL can optionally take T10.G8.02-ADV

**Action:** None needed. This is the model for handling theoretical content.

---

## 2. THEORETICAL ALGORITHM IMPLEMENTATION (16 skills)

### Category A: Pure Algorithm Implementation (EXCLUDE or MARK COMPETITION)

#### DE-EMPHASIZE - T10.G3.03
**Skill:** Sort a list by swapping items
**Current:** Students implement simple sorting (bubble/selection sort intuition)
**Issue:** Grade 3 students don't need to implement sorting algorithms
**Recommendation:** **DE-EMPHASIZE** - Mark as `difficulty_track: "competition"` or convert to "use sort blocks"

**Proposed Reframe:**
- **Title:** Use sort tools to organize lists
- **Description:** Students use CreatiCode's sort blocks to arrange lists in order (smallest to largest, A-Z). They practice choosing when to sort (organizing scores, alphabetizing names).
- **Why Better:** Focuses on practical use, not algorithm implementation

---

#### KEEP AS-IS - T10.G6.01
**Skill:** Sort a table by a column
**Recommendation:** **KEEP AS-IS** - This is practical! Sorting tables by columns is a real-world skill.

**Rationale:**
- Students need this for data projects (leaderboards, organizing survey results)
- Focus is on practical application, not algorithm theory
- Aligns with data literacy goals

---

#### DE-EMPHASIZE - T02.G7.02
**Skill:** Design a flowchart for a sorting or search algorithm
**Issue:** Too focused on formal algorithmic design
**Recommendation:** **DE-EMPHASIZE** - Mark as `difficulty_track: "competition"` or `optional: true`

**Why:** Flowcharting sorting algorithms is ACSL-style prep, not needed for creative projects.

---

#### DE-EMPHASIZE - T07.G8.02
**Skill:** Implement iterative algorithms with loops
**Current:** Computing GCD by repeated subtraction
**Issue:** This is abstract number theory, not relevant to games/apps
**Recommendation:** **DE-EMPHASIZE** or **REFRAME**

**Proposed Reframe:**
- **Title:** Use loops to repeat game logic
- **Description:** Students use loops to repeatedly update game state (move enemies, check collisions, animate sprites). Focus on practical game/simulation loops.
- **Why Better:** Same concept (iterative updates) but in creative context

---

#### KEEP AS-IS - T08.G6.03
**Skill:** Use conditionals in a search or decision algorithm
**Recommendation:** **KEEP AS-IS** - Finding max/min, linear search are practical skills

**Rationale:**
- Relevant for games (finding closest enemy, highest score)
- Relevant for apps (searching data, filtering lists)
- Not too theoretical despite "algorithm" in description

---

#### KEEP AS-IS - T09.G8.01
**Skill:** Use variables in iterative algorithms
**Recommendation:** **KEEP AS-IS** - Variables for tracking state is fundamental

**Rationale:**
- Core programming concept
- Applicable to games, simulations, apps
- Description should emphasize practical use cases over "algorithms"

---

### Category B: Algorithm Analysis (MOSTLY EXCLUDE/DE-EMPHASIZE)

#### DE-EMPHASIZE - T01.G6.01
**Skill:** Analyze an algorithm's efficiency in different scenarios
**Issue:** Too theoretical for Grade 6. "Number of steps" analysis is ACSL-style.
**Recommendation:** **DE-EMPHASIZE** - Mark as `difficulty_track: "competition"` or remove

**Why:** Students don't need to analyze algorithmic efficiency to build creative projects. They need to know "does it work?" not "how many steps does it take?"

---

#### DE-EMPHASIZE - T01.G7.02
**Skill:** Understand why different algorithms are chosen for different problems
**Issue:** Sounds theoretical but could be practical
**Recommendation:** **REFRAME** for practical context

**Proposed Reframe:**
- **Title:** Choose the right approach for your problem
- **Description:** Students learn when to use different programming patterns (loops vs conditionals vs lists) based on what they're building. Example: "Should I use a loop or a custom block for this?" Focus on practical decision-making.
- **Why Better:** Same learning goal, but framed as practical tool selection

---

#### EXCLUDE - T02.G7.03
**Skill:** Count and compare steps needed for different algorithms
**Issue:** Pure algorithmic complexity analysis (ACSL topic)
**Recommendation:** **EXCLUDE** or mark as `difficulty_track: "competition"` with `competition_tags: ['ACSL_junior']`

**Why:** This is exactly the kind of theoretical CS that's "not very interesting" for creative projects. No practical value for app/game builders.

---

#### DE-EMPHASIZE - T04.G6.04
**Skill:** Compare efficiency of different pattern solutions
**Issue:** Similar to T02.G7.03 - efficiency comparison without practical need
**Recommendation:** **DE-EMPHASIZE** - Mark as `difficulty_track: "competition"`

---

### Category C: Pseudocode & Formal Representation (REFRAME)

#### REFRAME - T01.G7.03
**Skill:** Plan an algorithm using words and simple steps
**Current:** Write pseudocode
**Recommendation:** **ALREADY REFRAMED!** (This was changed in Week 1)

**Action:** Verify it emphasizes "planning" not "pseudocode formalism"

---

#### REFRAME - T02.G4.03
**Skill:** Convert a story or real-world process into pseudocode
**Issue:** "Pseudocode" sounds too formal for Grade 4
**Recommendation:** **REFRAME** to emphasize planning/storytelling

**Proposed Reframe:**
- **Title:** Plan a process step-by-step before coding
- **Description:** Students write out a real-world process (making a sandwich, playing a game) in simple steps before turning it into code. Focus: clear planning helps you code better!
- **Why Better:** Removes "pseudocode" jargon, keeps useful planning skill

---

#### REFRAME - T02.G5.03
**Skill:** Write pseudocode for a multi-step algorithm
**Issue:** Similar to above
**Recommendation:** **REFRAME** to focus on project planning

**Proposed Reframe:**
- **Title:** Plan your code with written steps
- **Description:** Before coding a complex feature (game level, animation sequence), write out the steps in plain English. "First, the character moves right. Then, check if they hit a wall. If yes, stop. If no, keep moving."
- **Why Better:** Same skill, practical framing

---

#### REFRAME - T02.G6.03
**Skill:** Write pseudocode with nested structures
**Issue:** Too formal
**Recommendation:** **REFRAME** or **DE-EMPHASIZE**

**Proposed Reframe:**
- **Title:** Plan complex code with nested steps
- **Description:** For complex game logic, plan nested patterns: "For each enemy: check if player is nearby. If yes: move toward player. Otherwise: patrol randomly."
- **Why Better:** Focuses on practical game/app logic

---

### Category D: Flowcharts & Formal Diagrams (MIXED)

#### KEEP WITH CAUTION - T02.G3.01, T02.G4.01
**Skills:** Create simple flowcharts / Create flowcharts with loops
**Recommendation:** **KEEP** but ensure practical framing

**Rationale:**
- Flowcharts can help visual learners
- Useful for planning game flow, story branches
- BUT: Should focus on planning tools, not formal CS notation

**Check:** Do these skills emphasize "flowcharts as planning tools" or "flowcharts as formal algorithm representation"? If latter, reframe.

---

## 3. FORMAL CS CONCEPTS (25 skills)

### Category A: Formal Specification Documents (MIXED)

#### KEEP AS-IS - T03.G8.02
**Skill:** Create a formal project specification document
**Recommendation:** **KEEP AS-IS** - Supports project development

**Rationale:**
- Needed for competitions (Congressional App Challenge)
- Teaches professional documentation
- "Formal" here means "complete/professional," not "theoretical CS"

---

#### KEEP AS-IS - T12.G8.05
**Skill:** Create a Technical Specification Document
**Recommendation:** **KEEP AS-IS** - This is a Week 2 project development skill

**Rationale:**
- Part of the Congressional App Challenge pathway
- Practical documentation for real projects
- Not theoretical despite name

---

### Category B: Complexity & Efficiency Analysis (MOSTLY EXCLUDE)

#### EXCLUDE - T01.G6.01 (duplicate from earlier)
**Skill:** Analyze an algorithm's efficiency in different scenarios
**Recommendation:** **EXCLUDE** or mark as competition track

---

#### EXCLUDE - T03.G8.03
**Skill:** Analyze project complexity and estimate effort
**Issue:** Sounds like algorithmic complexity analysis
**Recommendation:** **REFRAME** or **DE-EMPHASIZE**

**Check Description:** If this is about estimating project effort (useful!), **REFRAME** to clarify. If it's about algorithmic complexity (not useful), **EXCLUDE**.

**Proposed Reframe (if project estimation):**
- **Title:** Estimate how long your project will take
- **Description:** Students look at project plans and estimate effort: "This needs 3 sprites, 5 features, testing with users - probably 4 weeks of work." Learn realistic planning.
- **Why Better:** Practical project management skill

---

### Category C: UX Flows & Design Diagrams (KEEP)

#### KEEP AS-IS - T05.G3.03, T05.G5.01
**Skills:** Make a UX flow diagram / Create a simple design document
**Recommendation:** **KEEP AS-IS** - These support creative projects!

**Rationale:**
- UX flows help plan apps and games
- Design documents guide project development
- Not theoretical - practical planning tools

---

## 4. ABSTRACT THEORY WITH NO PRACTICAL APPLICATION (10 skills)

### Category A: Edge Case Analysis (MIXED)

#### REFRAME - T01.G7.04
**Skill:** Analyze an algorithm for correctness on edge cases
**Issue:** Sounds ACSL-theoretical
**Recommendation:** **REFRAME** for practical testing context

**Proposed Reframe:**
- **Title:** Test your code with unusual inputs
- **Description:** Test your game/app with edge cases: What happens with 0 players? 1000 enemies? Empty text input? Learn to find bugs by testing extreme cases.
- **Why Better:** Same skill (edge case testing), practical framing

---

#### REFRAME - T02.G7.04
**Skill:** Trace an algorithm and identify a bug or edge case
**Issue:** "Trace an algorithm" is ACSL language
**Recommendation:** **REFRAME** as debugging skill

**Proposed Reframe:**
- **Title:** Debug by tracing code step-by-step
- **Description:** When code doesn't work, trace through it step-by-step: "First this happens, then this, then... wait, that's wrong!" Learn to find bugs by stepping through logic.
- **Why Better:** Same technique, practical debugging context

---

### Category B: XO Algorithm Design Help (KEEP)

#### KEEP AS-IS - T24.G6.01
**Skill:** Ask XO for algorithm design help
**Recommendation:** **KEEP AS-IS** - This teaches practical XO usage

**Rationale:**
- Students ask XO "how do I search a list?" - practical!
- Using AI assistance is a modern skill
- Not theoretical despite "algorithm" in title

---

### Category C: Code Organization Analysis (KEEP)

#### KEEP AS-IS - T12.G6.01
**Skill:** Analyze a program's organization and suggest improvements
**Recommendation:** **KEEP AS-IS** - Code review is practical!

**Rationale:**
- Learning to refactor code is valuable
- Helps students write better organized projects
- Analysis here is practical, not theoretical

---

## Summary Tables

### Skills to EXCLUDE (Move to Competition Track)

| Skill ID | Title | Reason |
|----------|-------|--------|
| T02.G7.03 | Count and compare steps needed for different algorithms | Pure algorithmic complexity - ACSL content |
| T01.G6.01 | Analyze an algorithm's efficiency | Theoretical efficiency analysis |
| T04.G6.04 | Compare efficiency of different pattern solutions | Similar to above |

**Action:** Mark these with `difficulty_track: "competition"` and `competition_tags: ['ACSL_junior']`

---

### Skills to DE-EMPHASIZE (Mark Optional/Advanced)

| Skill ID | Title | Reason | Action |
|----------|-------|--------|--------|
| T10.G3.03 | Sort a list by swapping items | Algorithm implementation for Grade 3 | Mark optional OR reframe as "use sort tools" |
| T02.G7.02 | Design flowchart for sorting algorithm | ACSL-style formal flowcharting | Mark `optional: true` or competition track |
| T07.G8.02 | Implement iterative algorithms | Abstract number theory (GCD) | Reframe with game/app examples |

**Action:** Add `optional: true` or move to competition track

---

### Skills to REFRAME (Keep but Make Practical)

| Skill ID | Current Title | Proposed Reframe |
|----------|---------------|------------------|
| T02.G4.03 | Convert story to pseudocode | Plan a process step-by-step before coding |
| T02.G5.03 | Write pseudocode for multi-step algorithm | Plan your code with written steps |
| T02.G6.03 | Write pseudocode with nested structures | Plan complex code with nested steps |
| T01.G7.02 | Why different algorithms are chosen | Choose the right approach for your problem |
| T01.G7.04 | Analyze algorithm correctness on edge cases | Test your code with unusual inputs |
| T02.G7.04 | Trace algorithm and identify bug | Debug by tracing code step-by-step |

**Action:** Update title and description to emphasize practical creative context

---

### Skills to KEEP AS-IS (Actually Practical!)

| Skill ID | Title | Why Keep |
|----------|-------|----------|
| T10.G6.01 | Sort a table by a column | Practical data skill |
| T08.G6.03 | Use conditionals in search/decision | Practical for games/apps |
| T09.G8.01 | Use variables in iterative algorithms | Core programming concept |
| T03.G8.02 | Create formal project specification | Needed for competitions |
| T12.G8.05 | Create technical specification document | Week 2 project skill |
| T05.G3.03 | Make UX flow diagram | Planning tool for apps |
| T05.G5.01 | Create design document | Project planning |
| T24.G6.01 | Ask XO for algorithm design help | Practical AI usage |
| T12.G6.01 | Analyze program organization | Code review skill |

**Action:** None - these support creative projects

---

## Week 1 Fixes Were Correct!

The Week 1 changes already handled the worst offender:

### ✅ Fixed: T10.G8.02

**BEFORE:**
- **Title:** Implement a sorting algorithm (bubble sort or selection sort)
- **Description:** Students implement a complete sorting algorithm...
- **Track:** Standard curriculum

**AFTER:**
- **T10.G8.02 (Standard):** Use sorting tools to organize lists of data
- **T10.G8.02-ADV (Competition):** Implement a sorting algorithm
  - `difficulty_track: "competition"`
  - `competition_tags: ['ACSL_junior']`
  - `requires_advanced_cs: true`

**This is the correct pattern!** Theoretical algorithm implementation → competition track. Practical tool usage → standard curriculum.

---

## Recommendations for Implementation

### 1. Apply the T10.G8.02 Pattern

For clearly theoretical skills (T02.G7.03, T01.G6.01):
1. Create "standard" version focused on practical use
2. Create "-ADV" competition version with theory
3. Tag with `ACSL_junior` or `ACSL_intermediate`

### 2. Add Metadata Fields

For theoretical skills to keep:
```json
{
  "optional": true,
  "difficulty_track": "competition",
  "competition_tags": ["ACSL_junior"],
  "requires_advanced_cs": true,
  "theoretical_focus": true
}
```

### 3. Reframe Descriptions

For skills worth keeping but poorly framed:
- Remove "algorithm" language → use "approach," "method," "technique"
- Remove "pseudocode" → use "planning," "writing steps"
- Remove "analyze efficiency" → use "test," "compare," "choose"
- Add concrete creative examples (games, apps, art)

### 4. Update Competition Paths Document

The `competition_paths.md` file lists ACSL pathways. Update to clarify:
- ACSL skills are OPTIONAL competition prep
- Standard curriculum focuses on creative projects
- Students can choose ACSL track if interested in competitive CS

---

## Final Verdict

### Skills to Remove from Standard Curriculum: 3
- T02.G7.03 - Count algorithm steps
- T01.G6.01 - Analyze algorithm efficiency
- T04.G6.04 - Compare efficiency of patterns

### Skills to Mark Optional/Competition: 5
- T10.G3.03 - Sort by swapping (or reframe)
- T02.G7.02 - Flowchart for sorting algorithm
- T07.G8.02 - Iterative algorithms (or reframe)
- T02.G6.03 - Pseudocode with nesting (or reframe)
- T01.G7.04 - Algorithm correctness analysis (or reframe)

### Skills to Reframe: 6
- T02.G4.03 - Story to pseudocode → Step-by-step planning
- T02.G5.03 - Multi-step pseudocode → Plan your code
- T01.G7.02 - Why algorithms chosen → Choose right approach
- T02.G7.04 - Trace algorithm → Debug step-by-step
- T03.G8.03 - Analyze complexity → Estimate project effort (if that's what it means)
- T07.G8.02 - Iterative algorithms → Use loops in games (if kept)

### Skills That Are Actually Fine: 40+
Most skills that mention "algorithm" or "analysis" are actually practical when you read the descriptions!

---

## Conclusion

**The curriculum is mostly good!** The theoretical content is concentrated in:
1. **One explicit ACSL skill** (already handled correctly)
2. **~10 skills** that need reframing to emphasize practical use
3. **~5 skills** that should be optional/competition track

**The user's concern is valid but manageable.** Most "theoretical" skills are actually practical when you look closely. The fix is mostly about:
- **Language:** Replace CS jargon with practical framing
- **Examples:** Add game/app/art context to descriptions
- **Tracking:** Mark purely theoretical skills as competition-only

**The Week 1 fixes show the right approach:** Separate practical tool usage (standard) from algorithm implementation theory (competition).

---

## Next Steps

1. **Apply reframing changes** to the 6 skills identified above
2. **Mark 3 skills** as competition-only (move to ACSL pathway)
3. **Update competition_paths.md** to clarify ACSL is optional
4. **Add "creative_application" field** to all skills with practical examples
5. **Test with teachers:** "Does this skill help students build creative projects?"

