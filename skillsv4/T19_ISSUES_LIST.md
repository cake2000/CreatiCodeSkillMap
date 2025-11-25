# T19 (Multiplayer Apps) - Detailed Issues List

## Format
- Issue ID
- Current Skill ID (if applicable)
- Issue Description
- Recommended Fix
- Priority (High/Medium/Low)

---

## ISSUE-001
**Current Skill ID:** T19.G6.01A
**Issue Description:** Overly broad skill trying to teach 8 parameters in one skill (game name, password, display name, role, server location, capacity, width, height)
**Recommended Fix:**
- Revise T19.G6.01A to focus only on game name and password
- Create T19.G6.01A1: Configure host display name
- Create T19.G6.01A2: Choose role when creating
- Create T19.G6.01A3: Select server location
- Keep existing T19.G6.01C (capacity) and T19.G6.01C2 (dimensions)
- Update all downstream dependencies
**Priority:** HIGH

---

## ISSUE-002
**Current Skill ID:** T19.G6.01B
**Issue Description:** Overly broad skill trying to teach 6 parameters in one skill (game name, host name, server location, password, display name, role)
**Recommended Fix:**
- Revise T19.G6.01B to focus only on game name, server location, and password
- Create T19.G6.01B1: Configure display name when joining
- Create T19.G6.01B2: Choose role when joining
- Create T19.G6.01B3: Find games using host name filter
- Update all downstream dependencies
**Priority:** HIGH

---

## ISSUE-003
**Current Skill ID:** Multiple (T19.G6.01A, T19.G6.01B, T19.G6.01C, T19.G6.01C2, T19.G6.03A.01, T19.G6.06, and 20+ others)
**Issue Description:** Many skills list "T18.G5.01" as a dependency, but the nature of this skill is unclear. If T18.G5.01 doesn't exist or is mislabeled, these dependencies are broken.
**Recommended Fix:**
- Identify what T18.G5.01 is (likely widget or table-related)
- Verify it exists in the T18 topic
- If it doesn't exist, determine the intended dependency and update all references
- If it exists but is wrong, find the correct dependency
**Priority:** HIGH

---

## ISSUE-004
**Current Skill ID:** T19.G5.01
**Issue Description:** Grade 5 skill requires coding (local 2-player game with WASD/arrows, conditionals, broadcasts), violating the pattern where G5 should be mostly conceptual
**Recommended Fix:**
Option A (Recommended): Move to Grade 6
- Rename to T19.G6.00.01 "Create a local 2-player game on one keyboard"
- Place before current G6.00A sequence
- Update dependencies in all G5 skills that reference it

Option B: Simplify to conceptual only
- Revise to "Understand local multiplayer concepts"
- Remove coding requirements
- Make it pure conceptual understanding
**Priority:** MEDIUM

---

## ISSUE-005
**Current Skill ID:** T19.G6.02B
**Issue Description:** Skill teaches TWO independent parameter choices in one skill (Dynamic/Static AND Rectangle/Circle), which could be separated for better scaffolding
**Recommended Fix:**
Option A: Split into two skills
- Revise T19.G6.02B to focus only on Dynamic vs Static
- Create T19.G6.02B2: Choose Rectangle vs Circle collision shape
- Keep dependencies on G6.00D and G6.00E

Option B: Keep as single skill
- Ensure assessment tests both parameters separately
- Maintain strong dependencies on conceptual skills G6.00D and G6.00E
**Priority:** MEDIUM

---

## ISSUE-006
**Current Skill ID:** T19.G6.06, T19.G6.06B
**Issue Description:** The mp_broadcasttouchmessage block has 4 modes (stop, continue, stop and delete, continue and delete) taught across 2 skills, but there's no clear overview explaining the 2x2 matrix structure
**Recommended Fix:**
- Create T19.G6.06.00 "Understand the four collision behavior modes"
- Explain the two dimensions: movement (stop vs continue) and persistence (keep vs delete)
- Place before T19.G6.06
- Update dependencies
**Priority:** LOW

---

## ISSUE-007
**Current Skill ID:** Multiple G8 skills (T19.G8.01, T19.G8.02, T19.G8.03, T19.G8.04, T19.G8.05, T19.G8.06, T19.G8.07, T19.G8.08, T19.G8.09, T19.G8.10)
**Issue Description:** Many G8 skills have heavy dependencies on T02-T05 topics (pseudocode, modules, algorithm patterns, design checklists). While grade-legal (G8→G6 is -2), these may be unnecessary and create long prerequisite chains.
**Recommended Fix:**
- Review each cross-topic dependency individually
- Ask: "Is this truly necessary for the skill, or nice-to-have?"
- Remove dependencies that aren't essential for functionality
- For example:
  - T19.G8.01 (team assignment) may not need T03.G6.01 (modules)
  - T19.G8.02 (anti-cheat) may not need T02.G6.01 (pseudocode)
  - T19.G8.06 (privacy) may not need T04.G6.01 (algorithms)
**Priority:** MEDIUM

---

## ISSUE-008
**Current Skill ID:** T19.G6.03A, T19.G6.03B, T19.G6.03C
**Issue Description:** Three deprecated skills have circular dependencies (each depends on its own final sub-skill), which is logically impossible
**Recommended Fix:**
Option A (Recommended): Remove deprecated skills entirely
- Delete T19.G6.03A, T19.G6.03B, T19.G6.03C from the skill tree
- Students should use the .01-.04 sub-skills directly

Option B: Fix dependencies
- Change dependencies to point to prerequisites of the .01 sub-skill
- Or remove dependencies entirely (redirect-only entries)
**Priority:** LOW

---

## ISSUE-009
**Current Skill ID:** T19.G6.00A through T19.G6.00K
**Issue Description:** Inconsistent naming convention with awkward phrases like "deeper dive," "in depth," and inconsistent suffixes (A, B, C, C2)
**Recommended Fix:**
- Standardize to numeric suffixes: .01, .02, .03, etc.
- Remove "in depth" and "deeper dive" phrases
- Rename:
  - T19.G6.00A → T19.G6.00.01
  - T19.G6.00B → T19.G6.00.02
  - T19.G6.00C → T19.G6.00.03
  - T19.G6.00C2 → T19.G6.00.04
  - T19.G6.00D → T19.G6.00.05
  - And so on...
- Update all references and dependencies
**Priority:** LOW

---

## ISSUE-010
**Current Skill ID:** None (missing skill)
**Issue Description:** No skill teaches password management best practices in multiplayer games (when to use, how to share securely, not broadcasting passwords)
**Recommended Fix:**
- Create T19.G7.06A: "Understand password security in multiplayer games"
- Description: Students learn password best practices: when to require passwords (private games with friends) vs open games (public matchmaking), how to share passwords securely (direct message, not public broadcast), why passwords protect rooms but not individual players. They understand trade-offs and implement both protected and open games.
- Dependencies: T19.G6.01A, T19.G7.06
- Placement: After T19.G7.06
**Priority:** LOW

---

## ISSUE-011
**Current Skill ID:** T19.G7.01, T19.G7.02
**Issue Description:** Skills have misleading dependency comments that reference grades incorrectly (comment says "G5" but dependency is actually OK at G7→G5 which is -2)
**Recommended Fix:**
- Review and clarify dependency comments
- Remove misleading comments or fix them to be accurate
- For T19.G7.01: Remove or fix comment about T06.G5.01
- For T19.G7.02: Remove or fix comment about T06.G5.01
**Priority:** LOW

---

## ISSUE-012
**Current Skill ID:** T19.G7.05, T19.G7.09
**Issue Description:** Potential overlap between two skills about fair starting conditions
- T19.G7.05: "Balance starting conditions and scoring for fairness"
- T19.G7.09: "Design fair starting conditions for variable player counts"
Both address fairness, but G7.09 is more specific about variable player counts
**Recommended Fix:**
- Clarify the distinction in skill descriptions
- T19.G7.05 focuses on auditing and testing fairness in general
- T19.G7.09 focuses specifically on dynamic spawn point calculation for variable player counts
- Ensure T19.G7.09 depends on T19.G7.05 (it already does)
- Update descriptions to make the distinction clearer
**Priority:** LOW

---

## ISSUE-013
**Current Skill ID:** Multiple G7 and G8 skills
**Issue Description:** Some G7/G8 skills are unclear about whether they expect design/conceptual work or implementation/coding work
**Recommended Fix:**
- Review each skill description and make explicit whether students should:
  - Design/Plan (create design document, flowchart, or written plan)
  - Implement (write actual code)
  - Analyze (evaluate existing games or code)
- Examples to clarify:
  - T19.G7.03: "Choose what data to synchronize" → is this design or implementation?
  - T19.G7.05: "Balance starting conditions" → is this design or implementation?
  - T19.G8.10: "Compare P2P vs client-server" → clearly conceptual analysis
**Priority:** LOW

---

## ISSUE-014
**Current Skill ID:** None (missing skill)
**Issue Description:** No skill addresses sprite cloning in multiplayer context (whether it works, how it interacts with replication)
**Recommended Fix:**
- Verify whether sprite cloning (T06.G5.02) works in multiplayer games
- If YES: Create T19.G7.XX: "Use sprite cloning in multiplayer games"
  - Explain how clones interact with replication
  - Address whether clones need to be registered
  - Cover use cases (projectiles, particles, temporary objects)
- If NO: Create T19.G7.XX: "Understand why cloning doesn't work in multiplayer"
  - Explain technical limitations
  - Provide alternatives (message-based spawning)
**Priority:** LOW

---

## ISSUE-015
**Current Skill ID:** None (missing skill)
**Issue Description:** No systematic testing checklist skill for multiplayer games (beyond basic 2-window and 3+ player testing)
**Recommended Fix:**
- Create T19.G7.08A: "Create a multiplayer testing checklist"
- Description: Students create a systematic testing checklist for multiplayer games including: test with 2 players, test with maximum capacity, test with player joining mid-game, test with player leaving mid-game, test with different server locations, test with simulated lag, test all game states (lobby, playing, game over), verify synchronization of all game objects, verify error messages for common failures. They use this checklist to thoroughly test their game before release.
- Dependencies: T19.G6.01G, T19.G7.08
- Placement: After T19.G7.08
**Priority:** LOW

---

## ISSUE-016
**Current Skill ID:** None (missing skill)
**Issue Description:** No skill addresses monitoring connection stability during active gameplay (between basic connection checking and full reconnection handling)
**Recommended Fix:**
- Create T19.G7.06B: "Monitor connection stability during gameplay"
- Description: Students implement continuous connection monitoring during active gameplay. They check connection status periodically (not just at join time), detect when connection becomes unstable (increased latency, packet loss), display warnings to players when connection degrades ("Connection unstable..."), and pause or adjust gameplay appropriately. They understand that proactive monitoring prevents sudden disconnections from surprising players.
- Dependencies: T19.G6.01F, T19.G6.00G (lag concepts)
- Placement: After T19.G7.06
**Priority:** LOW

---

## ISSUE-017
**Current Skill ID:** None (optimization opportunity)
**Issue Description:** The mp_broadcastmessagetoall block is excellently covered with 4 skills (T19.G6.04A/B/C/D), which could serve as a model for how other complex blocks should be taught
**Recommended Fix:**
- Use T19.G6.04X sequence as a template when teaching other complex blocks
- Document this as a best practice example
- When breaking down ISSUE-001 and ISSUE-002, use similar structure:
  - Conceptual understanding skill
  - Basic usage skill
  - Advanced parameters skill
  - Integration/application skill
**Priority:** INFORMATIONAL (not a fix, but a pattern to replicate)

---

## SUMMARY STATISTICS

**Total Issues Identified:** 17

**By Priority:**
- HIGH: 3 issues (ISSUE-001, ISSUE-002, ISSUE-003)
- MEDIUM: 3 issues (ISSUE-004, ISSUE-005, ISSUE-007)
- LOW: 10 issues (ISSUE-006, ISSUE-008, ISSUE-009, ISSUE-010, ISSUE-011, ISSUE-012, ISSUE-013, ISSUE-014, ISSUE-015, ISSUE-016)
- INFORMATIONAL: 1 (ISSUE-017)

**By Type:**
- Overly Broad Skills: 2 (ISSUE-001, ISSUE-002)
- Missing Skills: 4 (ISSUE-010, ISSUE-014, ISSUE-015, ISSUE-016)
- Dependency Issues: 4 (ISSUE-003, ISSUE-004, ISSUE-007, ISSUE-008)
- Naming/Organization: 2 (ISSUE-009, ISSUE-011)
- Clarity/Overlap: 3 (ISSUE-005, ISSUE-012, ISSUE-013)
- Best Practice: 1 (ISSUE-017)

**By Block:**
- mp_createmultiplayergame: 1 HIGH issue (ISSUE-001)
- mp_joinmultiplayergame: 1 HIGH issue (ISSUE-002)
- mp_addspritetogame: 1 MEDIUM issue (ISSUE-005)
- mp_broadcasttouchmessage: 1 LOW issue (ISSUE-006)
- Other blocks: adequately covered

**Skills Requiring Major Revision:**
- T19.G6.01A (ISSUE-001) - break into 6 skills
- T19.G6.01B (ISSUE-002) - break into 4 skills
- T19.G5.01 (ISSUE-004) - move to G6 or make conceptual

**Skills Requiring Minor Revision:**
- T19.G6.02B (ISSUE-005) - optionally split
- T19.G6.00A-K (ISSUE-009) - rename for consistency
- T19.G7.05, T19.G7.09 (ISSUE-012) - clarify distinction
- Various G7/G8 skills (ISSUE-013) - clarify expectations

**Deprecated Skills to Remove:**
- T19.G6.03A, T19.G6.03B, T19.G6.03C (ISSUE-008)

**Cross-Cutting Issues:**
- T18.G5.01 mystery dependency (ISSUE-003) affects 20+ skills
- Cross-topic dependencies in G8 (ISSUE-007) affect 10+ skills

---

## RECOMMENDED ACTION PLAN

### Phase 1: Critical Fixes (Complete First)
1. Identify and resolve T18.G5.01 dependency (ISSUE-003)
2. Break down T19.G6.01A into scaffolded sequence (ISSUE-001)
3. Break down T19.G6.01B into scaffolded sequence (ISSUE-002)

### Phase 2: Grade Alignment (Complete Second)
4. Move T19.G5.01 to G6 or make conceptual (ISSUE-004)
5. Review and reduce G8 cross-topic dependencies (ISSUE-007)

### Phase 3: Quality Improvements (Complete Third)
6. Optionally split T19.G6.02B (ISSUE-005)
7. Remove deprecated skills (ISSUE-008)
8. Standardize G6.00X naming (ISSUE-009)

### Phase 4: Enhancements (Complete Last)
9. Add collision mode overview skill (ISSUE-006)
10. Add missing advanced skills (ISSUE-010, ISSUE-014, ISSUE-015, ISSUE-016)
11. Clarify skill overlaps and expectations (ISSUE-011, ISSUE-012, ISSUE-013)

