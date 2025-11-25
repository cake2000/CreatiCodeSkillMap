# T33 Connected Services - Action Checklist
**Date:** 2025-11-25

Use this checklist to systematically fix all 32 identified issues.

---

## PHASE 1: CRITICAL SPLITS (7 actions)

### Split Overly Broad Skills

- [ ] **Action 1.1:** T33.G6.01 - Clarify as SURVEY only (not teaching all 15 blocks)
  - Update description to emphasize identification, not usage
  - Keep as meta-skill for network dependency recognition

- [ ] **Action 1.2:** T33.G6.10 → Split into 2 skills
  - Create T33.G6.10a: Fetch data from collections (READ)
  - Create T33.G6.10b: Insert data into collections (CREATE)
  - Update dependencies for both

- [ ] **Action 1.3:** T33.G7.01 → Split into 3 skills
  - Create T33.G7.01a: List all sheets
  - Create T33.G7.01b: Add new sheets
  - Create T33.G7.01c: Remove sheets
  - Remove "clear sheet" mention (already in G6.05)

- [ ] **Action 1.4:** T33.G7.11 → Split into 3 skills
  - Create T33.G7.11a: Update collections from tables
  - Create T33.G7.11b: Update collections in-place
  - Create T33.G7.11c: Delete documents from collections
  - Update dependencies for each

- [ ] **Action 1.5:** T33.G7.12 → Split into 2 skills
  - Create T33.G7.12a: Combine conditions with AND/OR/NOT
  - Create T33.G7.12b: Use LIMIT and SORT modifiers
  - Update dependencies for both

- [ ] **Action 1.6:** T33.G8.01 - KEEP as-is, but enhance description
  - Add use cases for each of 4 blocks
  - Clarify row vs column operations
  - Explain clear vs delete structure

- [ ] **Action 1.7:** Add T33.G6.09b for collection/field reporters
  - NEW skill for `collection` and `field` reporter blocks
  - Place after T33.G6.09 (conceptual comparison)

---

## PHASE 2: CRITICAL CLARITY FIXES (3 actions)

### Fix Misleading Descriptions

- [ ] **Action 2.1:** T33.G7.05 - COMPLETE REWRITE (CRITICAL!)
  - Change from "multiplayer experiences" to "cloud variables ONLY"
  - Add explicit note: NOT sprites/physics/game state
  - Add contrast with T19 Multiplayer blocks
  - Emphasize: variables-only synchronization

- [ ] **Action 2.2:** T33.G5.02 - Rewrite for variable focus
  - Change title to "real-time variable sync vs one-time requests"
  - Update examples to emphasize cloud variables
  - Add note distinguishing from full multiplayer

- [ ] **Action 2.3:** T33.G6.08 → MOVE to G5.04 (privacy before sharing)
  - Renumber as T33.G5.04
  - Place BEFORE any Google Sheets usage
  - Update G6.03, G6.04 to depend on new G5.04

---

## PHASE 3: DEPENDENCY FIXES (5 actions)

### Update Prerequisites

- [ ] **Action 3.1:** T33.G6.10a/b - Add table manipulation prerequisite
  - Add T10.G6.01 (Sort a table) to both new skills

- [ ] **Action 3.2:** T33.G7.01a/b/c - Fix clear sheet redundancy
  - Remove "clear sheet" from descriptions (already G6.05)
  - OR add T33.G6.05 as prerequisite if keeping mention

- [ ] **Action 3.3:** T33.G7.04 - Remove incorrect dependency
  - Remove T33.G6.03 (Drive folders ≠ Google Sheets)
  - Keep T33.G6.06 (error handling still relevant)

- [ ] **Action 3.4:** T33.G8.06 - Add database prerequisites
  - Add T33.G7.11a (update collections)
  - Add T33.G7.12a (complex queries)
  - Capstone should cover all major operations

- [ ] **Action 3.5:** Document G7 same-grade dependency sequence
  - Create ordered list: structure → operations → queries → updates
  - Validate all G7 internal dependencies follow this order

---

## PHASE 4: DESCRIPTION ENHANCEMENTS (12 actions)

### Add Concrete Content

- [ ] **Action 4.1:** T33.G6.02 - Add result processing
  - Add: display fetched content
  - Add: parse/extract specific information
  - Add: handle empty/error responses

- [ ] **Action 4.2:** T33.G7.02 - Add tradeoff analysis
  - Compare: cell operations vs full read/write
  - When to use each approach
  - Performance implications

- [ ] **Action 4.3:** T33.G7.04 - Clarify read-only access
  - Add: can list but NOT upload/delete/modify
  - Explain metadata returned
  - Set expectations for capabilities

- [ ] **Action 4.4:** T33.G7.08 - Add decision framework
  - Create "Use X when:" table for each service
  - Add practice scenarios
  - Include justification criteria

- [ ] **Action 4.5:** T33.G8.02 - Add concrete ToS activities
  - Create guided checklist format
  - Add "test against rules" scenarios
  - Make age-appropriate and actionable

- [ ] **Action 4.6:** T33.G8.04 - Add validation examples
  - Google Sheets: column count, empty cells, data types
  - Web Fetch: non-empty, expected keywords, not error page
  - Add specific IF-check examples

- [ ] **Action 4.7:** T33.G8.05 - Add measurement metrics
  - Internet dependency test (airplane mode)
  - Response time measurement
  - Data persistence test
  - Ease of updates comparison

### Simplify Content

- [ ] **Action 4.8:** T33.G7.09 - Remove timestamp complexity
  - Keep basic cache lookup and storage
  - REMOVE: timestamp tracking
  - REMOVE: cache expiration logic
  - Keep simple: "was this requested recently?"

- [ ] **Action 4.9:** T33.G8.03 - Simplify outage testing
  - Change from "outage simulator" to "offline testing"
  - Use airplane mode, not simulation
  - Focus on fallback design, not incident response

### Fix Premature/Unclear Content

- [ ] **Action 4.10:** T33.G6.05 - Remove delete comparison
  - Remove "preferable to deleting" (haven't learned delete yet)
  - Keep focus on clearing data while preserving structure
  - Add delete comparison to G7.01c instead

- [ ] **Action 4.11:** T33.G7.06 - Differentiate or remove
  - Option A: Remove (fold into G6.08/G5.04)
  - Option B: Clarify as platform mechanism vs user responsibility
  - Decision needed based on curriculum goals

- [ ] **Action 4.12:** Review all G8 skills for age appropriateness
  - Verify concrete examples in G8.02, G8.04, G8.05
  - Ensure hands-on activities, not abstract analysis
  - Check measurement/testing is appropriate for 8th grade

---

## PHASE 5: VALIDATION (5 actions)

### Final Checks

- [ ] **Action 5.1:** Verify block coverage = 100%
  - All 28 blocks explicitly covered
  - Collection/field reporters in G6.09b
  - No implicit or assumed coverage

- [ ] **Action 5.2:** Validate all dependencies respect X-2 rule
  - Check all new split skills
  - Verify G5.04 move doesn't create violations
  - Document any borderline cases

- [ ] **Action 5.3:** Check grade progression
  - G5: Concepts + privacy foundation
  - G6: Introduction to individual services
  - G7: Advanced operations + multi-service
  - G8: Integration + analysis

- [ ] **Action 5.4:** Review for terminology consistency
  - Cloud variables vs regular variables
  - Collections vs sheets vs tables
  - Cloud sessions vs multiplayer games
  - Service blocks vs Cloud blocks

- [ ] **Action 5.5:** Create final skill count verification
  - GK: 1, G1: 1, G2: 1, G3: 1, G4: 1
  - G5: 4 (+1 moved)
  - G6: 12 (+2 new)
  - G7: 18 (+6 split)
  - G8: 6 (enhanced)
  - **Total: 45 skills** (was 36, net +9)

---

## SUMMARY METRICS

### Skills Changed
- **Removed:** 0
- **Added:** 10 (splits) + 1 (new reporters) = 11 total
- **Moved:** 1 (privacy to G5)
- **Enhanced:** 12 (description improvements)
- **Net Change:** 36 → 45 (+9 skills)

### Coverage
- **Before:** 26/28 explicit (93%)
- **After:** 28/28 explicit (100%)

### Actions Required
- **Phase 1:** 7 actions (splits + new skill)
- **Phase 2:** 3 actions (critical clarity)
- **Phase 3:** 5 actions (dependencies)
- **Phase 4:** 12 actions (descriptions)
- **Phase 5:** 5 actions (validation)
- **Total:** 32 actions

---

## ESTIMATED EFFORT

- **Phase 1 (Splits):** 8-10 hours (create 11 new skills with descriptions/deps)
- **Phase 2 (Clarity):** 2-3 hours (rewrite 3 critical skills)
- **Phase 3 (Dependencies):** 2-3 hours (update prerequisite lists)
- **Phase 4 (Descriptions):** 6-8 hours (enhance 12 skill descriptions)
- **Phase 5 (Validation):** 3-4 hours (verify consistency and coverage)

**Total Estimated Effort:** 21-28 hours

---

## NOTES

- Start with Phase 1 and 2 (most critical)
- Phase 3 can be done in parallel with Phase 1
- Phase 4 can be incremental
- Phase 5 is essential before declaring complete

---

**Full Analysis:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T33_Phase1_Comprehensive_Issues.md`
**Quick Reference:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T33_ISSUES_AT_A_GLANCE.md`
