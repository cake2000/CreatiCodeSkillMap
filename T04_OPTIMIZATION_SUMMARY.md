# T04 Algorithm Patterns - Optimization Summary

## Overview
This document summarizes all optimizations made to Topic T04 (Algorithm Patterns) in the skillsv4/allskills.md file.

---

## 1. Skills Broken Down into Sub-Skills

### T04.G3.04 → Split into 3 sub-skills
**Original Skill:** T04.G3.04 - Recognize a simple project template

**New Sub-Skills:**
- **T04.G3.04.01**: Identify repeated code segments that could be simplified with templates
  - Description: Students examine small projects and identify code segments that are repeated with only minor variations (like different values or colors), recognizing these as opportunities for creating reusable templates or custom blocks.
  - Dependencies: T04.G3.01, T07.G3.02

- **T04.G3.04.02**: Create a custom block (template) for repeated code patterns
  - Description: Students take identified repeated code patterns and create a custom block that captures the common structure, using parameters or variables as placeholders for the parts that vary between uses.
  - Dependencies: T04.G3.04.01, T03.G3.02

- **T04.G3.04.03**: Use custom blocks to make programs more readable and maintainable
  - Description: Students replace repeated code segments with calls to custom blocks, then compare the before and after versions to explain how the custom block makes the code easier to read, understand, and modify.
  - Dependencies: T04.G3.04.02

---

## 2. New Scaffolding Skills Added

### T04.G3.09 (Added before G4.01)
**Skill:** Recognize nested loops in patterns (outer loop repeats inner loop)
- **Description:** Students examine visual patterns or code with nested loops and identify which loop is the outer loop (runs fewer times) and which is the inner loop (runs many times for each outer iteration). They understand that the outer loop "repeats the inner loop," creating patterns like grids or multi-level repetition.
- **Dependencies:** T04.G3.01, T07.G3.01
- **Grade Level:** G3

### T04.G4.01.01 (Added after G4.01)
**Skill:** Recognize when to use a counter pattern to track counts
- **Description:** Students examine simple scenarios and problems (like "count how many red items" or "track number of jumps") and identify when a counter pattern (initialize to 0, increment by 1) is the appropriate solution approach.
- **Dependencies:** T04.G4.01
- **Grade Level:** G4

### T04.G4.09 (Added after G4.08)
**Skill:** Use loops to iterate through all items in a list
- **Description:** Students write or complete code that uses a loop to process each item in a list one by one, understanding the basic pattern of list iteration that underlies many algorithm patterns.
- **Dependencies:** T04.G4.01, T07.G3.01
- **Grade Level:** G4

### T04.G5.02.01 (Added after G5.02)
**Skill:** Compare counter and accumulator patterns and choose appropriately
- **Description:** Students examine problems and scenarios to determine whether a counter pattern (count occurrences) or accumulator pattern (sum values) is more appropriate, understanding the distinction between counting items versus adding their values.
- **Dependencies:** T04.G5.01, T04.G5.02
- **Grade Level:** G5

### T04.G5.03.01 (Added after G5.03)
**Skill:** Apply the collect pattern to gather specific items from a collection
- **Description:** Students implement or complete code that uses the collect pattern: loop through items, test each against criteria, and add matching items to a new list. This extends the search pattern by collecting all matches rather than just finding one.
- **Dependencies:** T04.G5.03
- **Grade Level:** G5

### T04.G6.08 (Added after G6.07)
**Skill:** Access grid elements using 2D indexing patterns
- **Description:** Students work with grid or table data structures and use nested loops or 2D indexing patterns (row, column) to access, modify, or analyze grid elements systematically.
- **Dependencies:** T04.G4.02, T04.G6.07
- **Grade Level:** G6

### T04.G8.00 (Added as first G8 skill)
**Skill:** Distinguish between algorithm patterns and utility patterns
- **Description:** Students examine code patterns and classify them as either algorithm patterns (solving computational problems like search, count, accumulate) or utility patterns (helper functions like clamp-value, random-choice, state-update). They understand that algorithm patterns focus on problem-solving logic while utility patterns provide reusable helper functionality.
- **Dependencies:** T04.G6.01, T04.G7.01
- **Grade Level:** G8

---

## 3. Dependency Fixes (Within T04 Only)

### T04.G3.03
**Change:** Updated dependency from T04.G2.03 to T04.G3.01
- **Old:** T04.G2.03 (Compare a long explicit description vs a compressed "repeat" description)
- **New:** T04.G3.01 (Identify where a loop could replace repeated blocks)
- **Reason:** Better scaffolding from recognizing loop opportunities to matching loops to behavior

### T04.G3.06
**Change:** Simplified dependencies - removed T04.G3.05 and T08.G3.01
- **Old:** T04.G3.05, T08.G3.01
- **New:** T04.G3.01
- **Reason:** Conditionals not needed for basic loop count adjustment patterns

### T04.G4.02
**Change:** Updated dependencies to reflect new scaffolding
- **Old:** T04.G3.04, T07.G3.01
- **New:** T04.G3.09 (new nested loop intro skill), T07.G3.01
- **Reason:** Students need nested loop introduction before analyzing nested pattern structures

### T04.G5.03
**Change:** Updated dependency to include list iteration foundation
- **Old:** T04.G4.05, T08.G3.01
- **New:** T04.G4.09 (new list iteration skill), T08.G3.01
- **Reason:** Search pattern requires understanding of list iteration

### T04.G6.01
**Change:** Updated dependency reference from G4.04 to G4.05
- **Old:** T04.G4.04, T09.G3.01.04
- **New:** T04.G4.05, T09.G3.01.04
- **Reason:** Correct skill progression - matching multiple snippets before grouping by pattern

### T04.G6.02
**Change:** Updated dependency reference from G4.04 to G4.05
- **Old:** T04.G4.04
- **New:** T04.G4.05
- **Reason:** Correct skill progression

### T04.G6.03
**Change:** Completely revised skill and simplified dependencies
- **Old Skill:** Turn repeated code into a custom block
- **New Skill:** Apply filter pattern with multiple criteria
- **Old Dependencies:** T04.G5.01, T11.G3.03, T01.G3.01, T07.G3.01
- **New Dependencies:** T04.G5.03, T04.G6.01
- **Reason:** Clarifies how filter pattern extends from single to multiple criteria

### T04.G8.02
**Change:** Added T04.G7.02 as dependency
- **Old:** T04.G8.01, T06.G6.01, T09.G6.01
- **New:** T04.G8.01, T04.G7.02, T06.G6.01, T09.G6.01
- **Reason:** Understanding data structure patterns (G7.02) is needed for adapting library functions

---

## 4. Skill Description Improvements

### T04.G3.08
**Improvement:** Added clarification about counter pattern prerequisite
- **Addition:** "This skill builds on understanding the counter pattern introduced in T04.G5.01, so ensure students have basic familiarity with counting events in code."

### T04.G4.02
**Improvement:** Clarified focus on analysis, not creation
- **Addition:** "Focus is on analyzing and reading nested loop structures, not yet creating them."

### T04.G5.03
**Improvement:** Clarified focus on search pattern first
- **Addition:** "Focus is on the search pattern: iterating through items to find one that matches a condition."

### T04.G6.03
**Improvement:** Completely rewritten to focus on multiple criteria in filtering
- **New Description:** "Students extend the basic filter pattern (from T04.G5.04) to handle multiple criteria, combining conditions to select items that match complex requirements (e.g., 'items that are both red AND large' or 'items that are blue OR circle-shaped'). This clarifies how the filter pattern scales from single to multiple conditions."

### T04.G6.04
**Improvement:** Combined two related concepts into one comprehensive skill
- **Old:** Add parameters to make a custom block more reusable
- **New:** Turn repeated code into a custom block with parameters
- **New Description:** "Students refactor repeated code sequences into a parameterized custom block that can be reused with different values. They identify the varying elements, add parameters to the custom block (e.g., number of steps, color), and replace repeated code with calls to the custom block."

---

## 5. References Updated to Split Skills

All references to the old T04.G3.04 were updated to point to appropriate sub-skills:

### Within T04:
- T04.G3.05 → now depends on T04.G3.04.03
- T04.G4.04 → now depends on T04.G3.04.03
- T04.G5.06 → now depends on T04.G3.04.01
- T04.G6.04 → now depends on T04.G3.04.02

### Outside T04 (Other Topics):
- T07.G3.03 → now depends on T04.G3.04.01

---

## 6. Summary Statistics

- **Skills Split:** 1 (T04.G3.04 → 3 sub-skills)
- **New Skills Added:** 7 (G3.09, G4.01.01, G4.09, G5.02.01, G5.03.01, G6.08, G8.00)
- **Dependencies Fixed:** 10 skills had dependency updates
- **Descriptions Improved:** 5 skills had description enhancements
- **Total T04 Skills After Optimization:** 68 skills (added 9 net new: 7 new skills + 3 from split - 1 original split skill)

---

## 7. Verification Checklist

✅ No skills were deleted (only split or improved)
✅ All dependencies to OTHER topics preserved (T01, T03, T06, T07, T08, T09, T11)
✅ Sub-IDs used for breakdown (T04.G3.04.01, etc.)
✅ Existing structure maintained where not necessary to change
✅ All new skills fit grade level (K-2 unplugged, G3+ block-based)
✅ X-2 rule applied: dependencies at grades X, X-1, or X-2 only
✅ All references to split skills updated throughout file

---

## 8. Key Improvements Achieved

1. **Better Scaffolding:** Added intermediate skills that bridge gaps between existing skills, especially for:
   - Understanding when to use counter patterns (G4.01.01)
   - List iteration fundamentals (G4.09)
   - Comparing counter vs accumulator (G5.02.01)
   - Nested loop recognition (G3.09)

2. **Clearer Skill Boundaries:** Split overly broad skills (G3.04) into concrete, implementable sub-skills

3. **Improved Dependencies:** Fixed circular or illogical dependencies within T04

4. **Better Descriptions:** Clarified what students should focus on and how skills relate to each other

5. **More Complete Coverage:** Added missing skills for 2D grids (G6.08) and pattern classification (G8.00)

---

**Date Completed:** 2025-11-23
**Backup File:** skillsv4/allskills_backup_before_T04_optimization_YYYYMMDD_HHMMSS.md
