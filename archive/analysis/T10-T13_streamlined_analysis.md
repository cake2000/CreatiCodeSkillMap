# T10-T13: Core Programming (Streamlined Analysis)

## T10 – Lists & Tables (36 skills)

**Age-Appropriateness**: ✓ Excellent K→data structures progression
**Granularity**: ✓ All appropriate
**Issues**: None

### Key Progression:
- **K-2**: Visual lists, ordering, grouping (unplugged)
- **3-5**: List blocks (add, access by index), loop through lists
- **6-8**: 2D tables, sorting, searching, data structures

### Critical Dependencies:
- T09 (Variables): Lists are special variables
- T07 (Loops): Iterate through lists
- T08 (Conditionals): Filter lists
- T25 (Data Representation): Data as lists

### Sample Skills by Grade:
- **GK**: Sort toys into groups (concrete)
- **G1**: Order items in a sequence
- **G4**: Create list, add/remove items (**MILESTONE**)
- **G5**: Loop through list with index
- **G6**: 2D tables/grids, search list
- **G7**: Sort algorithms, filter lists
- **G8**: Complex data structures

### Dependency Pattern:
- Early skills (K-2): Stand-alone or depend on T01 (algorithms)
- G4+: Depend heavily on T07 (loops), T09 (variables)
- G6+: Feed into T25-T29 (data topics)

**Status**: ✅ Clean, no issues

---

## T11 – Functions & Modularization (35 skills)

⚠️ **OVERLAP CHECK WITH T04 (Patterns)**

**Age-Appropriateness**: ✓ Excellent - abstraction emerges G3+
**Granularity**: ✓ All appropriate
**Issues**: Expected overlaps with T04 (documented in T04 analysis)

### Key Progression:
- **K-2**: Recognize reusable actions (unplugged)
- **G3**: First custom blocks (**CRITICAL MILESTONE**)
- **G4**: Parameters in custom blocks
- **G5**: Libraries of custom blocks
- **G6-8**: Advanced modularity, decomposition patterns

### Expected T04 Overlaps (from T04 analysis):
- **T11.G3.01**: Create custom blocks (T04.G3.03 should reference)
- **T11.G4.01**: Parameterized blocks (T04.G4.02 should reference)
- **T11.G5.01**: Libraries (T04.G5.02 should reference)

### Resolution Strategy:
- **T11 = authoritative** for custom block implementation
- **T04 = pattern recognition** only, references T11 for "how to build"

### Critical Dependencies:
- T03 (Decomposition): Breaking into reusable parts
- T04 (Patterns): Recognizing reusable patterns → T11 implements
- T07 (Loops): Functions often contain loops
- T09 (Variables): Parameters are variables

### Sample Skills:
- **G1**: Identify repeated multi-block sequences
- **G3**: Create first custom block (e.g., "jump" = move up + wait + move down)
- **G4**: Add parameters (e.g., "jump(height)")
- **G5**: Build library (multiple related functions)
- **G6**: Decompose complex tasks into functions
- **G7**: Modular architecture
- **G8**: Function design patterns

**Status**: ✅ Clean - overlaps with T04 expected and documented

---

## T12 – Program Organization (35 skills)

**Age-Appropriateness**: ✓ Good - code quality focus emerges G4+
**Granularity**: ✓ All appropriate
**Issues**: None

### Key Progression:
- **K-2**: Recognize organized vs messy (unplugged)
- **G3**: Sprite organization, naming
- **G4-5**: Comments, documentation
- **G6-8**: Code architecture, refactoring for clarity

### Critical Dependencies:
- T03 (Decomposition): Organizational thinking
- T11 (Functions): Modular organization
- T06 (Events): Organizing events
- T13 (Testing): Documentation aids testing

### Sample Skills:
- **G1**: Keep scripts together vs scattered
- **G3**: Name sprites/variables clearly
- **G4**: Add comments to code (**MILESTONE**)
- **G5**: Group related code
- **G6**: Refactor for clarity
- **G7**: Design for maintainability
- **G8**: Professional code structure

**Status**: ✅ Clean, no issues

---

## T13 – Testing & Debugging (35 skills)

**Age-Appropriateness**: ✓ **EXCELLENT** - systematic testing emerges naturally
**Granularity**: ✓ All appropriate
**Issues**: None

### Key Progression:
- **K-2**: Find what's wrong (visual debugging)
- **G3-5**: Systematic testing, predict-test-fix cycle
- **G6-8**: Edge cases, test strategies, professional debugging

### Critical Dependencies:
- T02 (Tracing): Debugging requires tracing
- T01 (Algorithms): Predicting outcomes
- ALL programming topics: Testing applies to everything

### Sample Skills:
- **K**: Spot the broken sequence (picture cards)
- **G2**: Find simple bugs in code (**MILESTONE**)
- **G3**: Test and predict program behavior
- **G4**: Create test cases
- **G5**: Test edge cases (boundary conditions)
- **G6**: Systematic debugging strategies
- **G7**: Test-driven development concepts
- **G8**: Complex debugging, testing frameworks

### This topic is depended upon by:
- T05 (HCD): Iteration and user testing
- T06-T12: All need testing/debugging
- T14-T24: Application testing

**Status**: ✅ Clean, excellent topic

---

## Domain 2 Core Programming (T06-T13) Summary

**Total Skills**: 280 (35-43 per topic)
**Issues Found**: 0 dependency errors, documented overlaps only
**Quality**: A+ (all topics excellent)

### Issue Resolution Tracking:

| Issue | Location | Status | Action |
|-------|----------|--------|--------|
| T04/T07 overlap | 6 skills | ✅ Documented | T04 refocus needed |
| T04/T11 overlap | 3 skills | ✅ Documented | T04 references T11 |
| T08.G6.04 dependency | T01.G7.02 (G7) | 📋 Noted | Change to T01.G6.01 |

### Core Programming Dependencies (Foundational Order):

1. **T06 (Events)** ← Everyone depends on this
2. **T09 (Variables)** ← Critical for state
3. **T07 (Loops)** ← Iteration foundation
4. **T08 (Conditionals)** ← Decision foundation
5. **T10 (Lists)** ← Data structures (depends on T07, T09)
6. **T11 (Functions)** ← Abstraction (depends on T03)
7. **T12 (Organization)** ← Quality (depends on T11)
8. **T13 (Testing)** ← Meta-skill (applies to all)

### Age-Appropriateness Highlights:

**Outstanding Topics**:
- T09 (Variables): Perfect concrete→abstract
- T13 (Testing): Natural emergence of systematic thinking
- T06 (Events): Highly motivating (games)

**All Topics**: Age-appropriate K-8 progressions ✅

### Next: Domain 2 Applications (T14-T24)

Applications depend heavily on T06-T13 core programming.
Expected: Clean dependencies, no overlaps.

---

**D2 Core Complete**: 280 skills analyzed, 1 minor fix needed (T08.G6.04)
