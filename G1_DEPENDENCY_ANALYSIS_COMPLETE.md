# Grade 1 Cross-Topic Dependency Analysis - Complete Report

**Date:** 2024-11-24
**Scope:** All 112 Grade 1 skills across 36 topics
**Focus:** Cross-topic dependencies, X-2 rule compliance, transitive redundancies

---

## Executive Summary

### Analysis Overview
- **Total Grade 1 Skills Analyzed:** 112 skills across 34 topics (T11 and T19 have no G1 skills)
- **Total Dependency Issues Found:** 3 verified issues
- **X-2 Rule Violations:** 0 (all Grade 1 skills correctly depend only on K and 1)
- **Transitive Redundancies:** 3 confirmed cases
- **Missing Cross-Topic Dependencies:** 0 (all skills have appropriate dependencies)

### Key Findings

1. **Grade 1 skills are well-structured** with appropriate dependencies
2. **Cross-topic dependencies are minimal** - most skills depend on T01 (Everyday Algorithms) as foundation
3. **No X-2 rule violations** - all Grade 1 skills correctly avoid depending on Grade 2 skills
4. **Three transitive redundancies** need cleanup (same-topic dependencies)

---

## Verified Issues

### Issue 1: T10.G1.01 - Transitive Redundancy

**Skill:** Sort items using two rules
**Topic:** T10 – Lists & Tables

**Current Dependencies:**
- `T10.GK.01`: Sort picture cards into groups
- `T10.GK.04`: Add an item to the right group

**Problem:** T10.GK.01 is already a direct dependency of T10.GK.04, making it transitive when both are listed.

**Proposed Fix:**
```
Dependencies:
* T10.GK.04: Add an item to the right group
```

**Reasoning:** Remove T10.GK.01 since it's already reached through T10.GK.04. The skill builds on "adding items to groups" which inherently includes the prerequisite of "sorting into groups."

---

### Issue 2: T24.G1.02 - Transitive Redundancy

**Skill:** Compare AI answers to expected answers
**Topic:** T24 – XO & Generative AI Practices

**Current Dependencies:**
- `T24.GK.01`: Identify AI as a computer helper
- `T24.GK.03`: Give simple instructions to an AI helper

**Problem:** T24.GK.01 is already a direct dependency of T24.GK.03.

**Proposed Fix:**
```
Dependencies:
* T24.GK.03: Give simple instructions to an AI helper
```

**Reasoning:** Remove T24.GK.01 since students must first know what AI is (GK.01) before they can give it instructions (GK.03). The dependency chain GK.01 → GK.03 → G1.02 is appropriate.

---

### Issue 3: T24.G1.03 - Transitive Redundancy

**Skill:** Understand AI needs clear instructions
**Topic:** T24 – XO & Generative AI Practices

**Current Dependencies:**
- `T24.GK.03`: Give simple instructions to an AI helper
- `T24.G1.02`: Compare AI answers to expected answers

**Problem:** T24.GK.03 is already a direct dependency of T24.G1.02.

**Proposed Fix:**
```
Dependencies:
* T24.G1.02: Compare AI answers to expected answers
```

**Reasoning:** Remove T24.GK.03 since it's already reached through T24.G1.02. Understanding that AI needs clear instructions (G1.03) builds on comparing AI answers (G1.02), which already requires knowing how to give instructions (GK.03).

---

## Cross-Topic Dependency Analysis

### Most Common Cross-Topic Dependency Patterns

Grade 1 skills most frequently depend on:

1. **T01 (Everyday Algorithms):** 19 dependencies
   - Foundation for sequencing, patterns, and algorithmic thinking
   - Appropriate as conceptual foundation before technical topics

2. **T03 (Problem Decomposition):** 4 dependencies
   - Used by organizing and debugging skills
   - Appropriate for breaking down complex tasks

3. **T04 (Algorithm Patterns):** 1 dependency
   - Used by debugging skills
   - Appropriate for recognizing repeated structures

### Topics Most Dependent on Other Topics

Topics with highest cross-topic dependency ratios:
- T13 (Testing & Debugging): 4 out of 4 skills have cross-topic deps
- T14 (2D Games): 3 out of 5 skills have cross-topic deps
- T20 (Algorithmic Art): 4 out of 4 skills have cross-topic deps
- T35 (Impacts & Ethics): 3 out of 4 skills have cross-topic deps

This is appropriate as these are more advanced topics building on foundational concepts.

---

## X-2 Rule Compliance

**Result: 100% Compliant**

All 112 Grade 1 skills were checked for X-2 rule violations (Grade 1 depending on Grade 2).

**Violations Found:** 0

This confirms that the grade progression is properly structured, with Grade 1 skills only depending on Kindergarten and other Grade 1 prerequisites.

---

## Missing Cross-Topic Dependency Analysis

### Methodology
Analyzed all Grade 1 skills for potential missing dependencies by:
1. Identifying skills that mention concepts from other topics (events, loops, variables, etc.)
2. Distinguishing between unplugged/conceptual activities vs. programming activities
3. Checking if programming-specific skills have appropriate technical dependencies

### Result: No Missing Dependencies

**Key Finding:** Most Grade 1 skills are:
- **Unplugged activities** (sorting cards, matching pictures, role-playing)
- **Conceptual learning** (identifying patterns, understanding concepts)
- **Picture-based assessments** (no code required)

Therefore, they correctly do NOT require dependencies on programming topics like:
- T06 (Events) - only needed when using actual event blocks
- T07 (Loops) - only needed when using repeat blocks
- T09 (Variables) - only needed when using variable blocks
- T14 (Motion) - only needed when moving sprites with blocks
- T21 (Pen) - only needed when using pen blocks

**Example of Correct Design:**
- `T29.G1.02: Count words in a sentence` - Uses paper strips, not variables
- `T20.G1.02: Match directions to drawings` - Matches pictures, not pen blocks
- `T16.G1.01: Match interface elements` - Unplugged matching, not event blocks

---

## Transitive Redundancy Deep Dive

### What is Transitive Redundancy?

When skill A depends on both B and C, but B already depends on C:
```
A → B → C
A → C (redundant)
```

### Why Remove Transitive Dependencies?

1. **Cleaner dependency graphs**
2. **Easier maintenance** - changing C only requires updating one place
3. **Pedagogical clarity** - shows the direct prerequisite
4. **Reduced complexity** - shorter dependency lists

### When to Keep "Redundant" Dependencies?

Some cases where transitive dependencies are kept for pedagogical reasons:
- **Different aspects:** Skill needs multiple independent facets from prerequisites
- **Reinforcement:** Skill explicitly builds on multiple earlier concepts simultaneously
- **Cross-topic clarity:** Making cross-topic connections explicit

**In our 3 cases:** All are same-topic transitive dependencies with clear linear progression, so removal is appropriate.

---

## Grade 1 Skills by Category

### Foundational Concepts (T01-T05)
- **T01:** 10 skills - Everyday algorithms, sequencing
- **T02:** 5 skills - Algorithm diagrams
- **T03:** 4 skills - Problem decomposition
- **T04:** 4 skills - Algorithm patterns
- **T05:** 4 skills - Human-centered design

### Control Structures (T06-T10)
- **T06:** 3 skills - Events & sequences
- **T07:** 2 skills - Loops
- **T08:** 3 skills - Conditions & logic
- **T09:** 2 skills - Variables & expressions
- **T10:** 6 skills - Lists & tables

### Program Development (T12-T13)
- **T12:** 4 skills - Organizing programs
- **T13:** 4 skills - Testing & debugging

### Graphics & Games (T14-T18)
- **T14:** 5 skills - 2D games
- **T15:** 3 skills - Looks & effects
- **T16:** 2 skills - User interfaces
- **T17:** 1 skill - 2D motion & physics
- **T18:** 1 skill - Sprites & clones basics

### Creative Coding (T20-T23)
- **T20:** 4 skills - Algorithmic art
- **T21:** 2 skills - AI media
- **T22:** 2 skills - Sensing
- **T23:** 3 skills - Sound

### Data & AI (T24-T29)
- **T24:** 3 skills - XO & generative AI
- **T25:** 3 skills - Data representation
- **T26:** 3 skills - Data collection
- **T27:** 3 skills - Data analysis
- **T28:** 4 skills - Chance & simulations
- **T29:** 4 skills - Text data & NLP

### Systems & Digital Citizenship (T30-T36)
- **T30:** 3 skills - Devices & hardware
- **T31:** 1 skill - Internet & cloud
- **T32:** 4 skills - Cybersecurity
- **T33:** 1 skill - Connected services
- **T34:** 2 skills - Custom blocks
- **T35:** 4 skills - Impacts & ethics
- **T36:** 3 skills - Careers & collaboration

---

## Recommendations

### Immediate Actions Required

1. **Fix 3 transitive redundancies:**
   - T10.G1.01: Remove T10.GK.01
   - T24.G1.02: Remove T24.GK.01
   - T24.G1.03: Remove T24.GK.03

### No Action Required

1. **X-2 Rule:** All skills compliant ✓
2. **Cross-topic dependencies:** All appropriate ✓
3. **Missing dependencies:** None identified ✓

### Monitoring Recommendations

1. **Future Grade 2 development:** Ensure Grade 2 skills properly build on Grade 1
2. **Cross-grade progression:** Verify smooth transition from G1 to G2 in each topic
3. **Advanced topic foundations:** As more advanced topics develop, ensure proper foundational dependencies

---

## Conclusion

The Grade 1 skills in the curriculum are **well-structured and properly organized**. The dependency structure is sound, with only 3 minor transitive redundancies to clean up. The curriculum correctly:

1. ✓ Maintains X-2 rule (no G1 → G2 dependencies)
2. ✓ Uses appropriate cross-topic dependencies
3. ✓ Distinguishes between unplugged/conceptual vs. programming activities
4. ✓ Builds logical progression within topics
5. ✓ Creates appropriate foundation for later grades

The identified issues are low-priority cleanup items that will improve maintainability but do not affect educational soundness.

---

## Appendix: Analysis Methodology

### Tools Used
1. Python scripts for automated dependency parsing
2. Pattern matching for keyword detection
3. Manual verification of edge cases
4. Topic-by-topic systematic review

### Validation Approach
1. Parse all 112 Grade 1 skills
2. Extract dependency information
3. Check X-2 rule compliance
4. Identify transitive dependencies
5. Analyze cross-topic patterns
6. Manual review of flagged issues
7. Distinguish true issues from false positives

### False Positive Elimination
Many automated flags were eliminated as false positives because:
- Skills use words like "draw" for paper activities, not pen blocks
- Skills mention "click" for unplugged card matching, not event blocks
- Skills involve "counting" conceptually, not with variable blocks
- Skills are picture-based assessments, not programming tasks

This careful distinction between conceptual and programming activities is crucial for accurate analysis.

---

**End of Report**
