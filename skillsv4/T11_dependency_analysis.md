# T11 (Functions & Procedures) Dependency Analysis

## Analysis Summary

This report analyzes all T11 skills for three types of dependency issues:
1. **X-2 Rule Violations**: Dependencies that violate the grade-level constraint (can only depend on N, N-1, or N-2)
2. **Missing Intra-Topic Dependencies**: Missing T11→T11 dependencies where later skills clearly build on earlier ones
3. **Unnecessary Same-Grade Dependencies**: T11→T11 dependencies within the same grade that are redundant (earlier in sequence)

---

## 1. X-2 RULE VIOLATIONS

### T11.G4.01: Define and call a simple custom block (no parameters)
**Grade:** 4
**Violating Dependencies:**
- ❌ T06.G2.03 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T03.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T03.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.03 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T06.G2.03 (Grade 2) - 2 grades below ✓ ALLOWED

**Status:** ✓ NO VIOLATIONS (all are within X-2 range)

---

### T11.G4.02: Distinguish command blocks from reporter blocks
**Grade:** 4
**Violating Dependencies:**
- ❌ T04.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T07.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED

**Status:** ✓ NO VIOLATIONS

---

### T11.G4.03: Use a reporter block's result in a calculation or condition
**Grade:** 4
**Violating Dependencies:**
- ❌ T01.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.03 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T06.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T06.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T06.G2.03 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T07.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED

**Status:** ✓ NO VIOLATIONS

---

### T11.G4.04: Describe the purpose of each custom block in a script
**Grade:** 4
**Violating Dependencies:**
- ❌ T01.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T02.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T02.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T03.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T03.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T07.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED

**Status:** ✓ NO VIOLATIONS

---

### T11.G4.05: Trace execution through a script with custom blocks
**Grade:** 4
**Violating Dependencies:**
- ❌ T03.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T03.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T07.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED

**Status:** ✓ NO VIOLATIONS

---

### T11.G4.06: Understand the argument block for accessing parameters
**Grade:** 4
**Violating Dependencies:**
- ❌ T03.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T03.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T06.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T06.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED

**Status:** ✓ NO VIOLATIONS

---

### T11.G4.07: Define a custom block with one parameter
**Grade:** 4
**Violating Dependencies:**
- ❌ T03.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T03.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T07.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED

**Status:** ✓ NO VIOLATIONS

---

### T11.G4.08: Test a custom block with simple inputs
**Grade:** 4
**Violating Dependencies:**
- ❌ T03.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T03.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T04.G2.02 (Grade 2) - 2 grades below ✓ ALLOWED
- ❌ T07.G2.01 (Grade 2) - 2 grades below ✓ ALLOWED

**Status:** ✓ NO VIOLATIONS

---

### T11.G5.01: Decompose a problem into logical custom block boundaries
**Grade:** 5
**Dependencies:**
- T11.G4.04 (Grade 4) ✓
- T11.G4.05 (Grade 4) ✓
- T12.G3.05 (Grade 3) - 2 grades below ✓
- T12.G4.05 (Grade 4) - 1 grade below ✓
- T09.G5.01 (Grade 5) ✓
- T03.G5.01 (Grade 5) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G5.02: Use custom blocks with parameters in a larger project
**Grade:** 5
**Dependencies:**
- T11.G4.07 (Grade 4) ✓
- T11.G4.08 (Grade 4) ✓
- T12.G3.05 (Grade 3) - 2 grades below ✓
- T12.G4.05 (Grade 4) - 1 grade below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G5.03: Match parameter names to argument values when calling custom blocks
**Grade:** 5
**Dependencies:**
- T11.G4.07 (Grade 4) ✓
- T11.G5.02 (Grade 5) ✓
- T12.G3.05 (Grade 3) - 2 grades below ✓
- T12.G4.05 (Grade 4) - 1 grade below ✓
- T02.G5.01 (Grade 5) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G5.04: Choose between adding a parameter vs. creating a separate block
**Grade:** 5
**Dependencies:**
- T11.G5.01 (Grade 5) ✓
- T11.G5.03 (Grade 5) ✓
- T12.G3.05 (Grade 3) - 2 grades below ✓
- T12.G4.05 (Grade 4) - 1 grade below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G5.05: Analyze a modular program structure
**Grade:** 5
**Dependencies:**
- T11.G4.04 (Grade 4) ✓
- T11.G4.05 (Grade 4) ✓
- T02.G5.01 (Grade 5) ✓
- T03.G5.01 (Grade 5) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G5.06: Define a custom block with two or more parameters
**Grade:** 5
**Dependencies:**
- T11.G4.07 (Grade 4) ✓
- T11.G5.03 (Grade 5) ✓
- T12.G3.05 (Grade 3) - 2 grades below ✓
- T12.G4.05 (Grade 4) - 1 grade below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G5.07: Decide whether a custom block should be a command or reporter
**Grade:** 5
**Dependencies:**
- T11.G4.02 (Grade 4) ✓
- T11.G4.07 (Grade 4) ✓
- T11.G5.02 (Grade 5) ✓
- T12.G3.05 (Grade 3) - 2 grades below ✓
- T12.G4.05 (Grade 4) - 1 grade below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G5.08: Define a custom reporter block that returns a value
**Grade:** 5
**Dependencies:**
- T11.G4.03 (Grade 4) ✓
- T11.G5.07 (Grade 5) ✓
- T12.G3.05 (Grade 3) - 2 grades below ✓
- T12.G4.05 (Grade 4) - 1 grade below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G5.09: Debug a script with incorrect custom block calls
**Grade:** 5
**Dependencies:**
- T11.G4.05 (Grade 4) ✓
- T11.G5.07 (Grade 5) ✓
- T12.G3.05 (Grade 3) - 2 grades below ✓
- T12.G4.05 (Grade 4) - 1 grade below ✓
- T02.G5.01 (Grade 5) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G5.10: Use comments to document custom block purpose
**Grade:** 5
**Dependencies:**
- T11.G4.07 (Grade 4) ✓
- T11.G5.08 (Grade 5) ✓
- T12.G3.05 (Grade 3) - 2 grades below ✓
- T12.G4.05 (Grade 4) - 1 grade below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G5.11: Create custom blocks with mixed text labels and parameters
**Grade:** 5
**Dependencies:**
- T11.G5.06 (Grade 5) ✓
- T11.G5.10 (Grade 5) ✓
- T12.G3.05 (Grade 3) - 2 grades below ✓
- T12.G4.05 (Grade 4) - 1 grade below ✓
- T09.G5.01 (Grade 5) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G6.01: Design custom blocks with clear, predictable interfaces
**Grade:** 6
**Dependencies:**
- T11.G5.04 (Grade 5) ✓
- T11.G5.05 (Grade 5) ✓
- T11.G5.06 (Grade 5) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G6.02: Create modular programs with multiple custom blocks
**Grade:** 6
**Dependencies:**
- T11.G5.05 (Grade 5) ✓
- T11.G5.06 (Grade 5) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G6.03: Test custom blocks with boundary and edge cases
**Grade:** 6
**Dependencies:**
- T11.G5.06 (Grade 5) ✓
- T11.G5.09 (Grade 5) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G6.04: Refactor spaghetti code into organized custom blocks
**Grade:** 6
**Dependencies:**
- T11.G5.05 (Grade 5) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G6.05: Add error handling to custom blocks
**Grade:** 6
**Dependencies:**
- T11.G5.06 (Grade 5) ✓
- T11.G6.03 (Grade 6) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G6.06: Critique custom block naming and parameter choices
**Grade:** 6
**Dependencies:**
- T11.G5.04 (Grade 5) ✓
- T11.G5.11 (Grade 5) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G6.07: Evaluate custom block scope and single responsibility
**Grade:** 6
**Dependencies:**
- T11.G5.05 (Grade 5) ✓
- T11.G6.01 (Grade 6) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G6.08: Critique return value usage in custom blocks
**Grade:** 6
**Dependencies:**
- T11.G5.07 (Grade 5) ✓
- T11.G5.08 (Grade 5) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G7.01: Implement algorithms as reusable custom blocks
**Grade:** 7
**Dependencies:**
- T11.G5.08 (Grade 5) - 2 grades below ✓
- T11.G6.04 (Grade 6) - 1 grade below ✓
- T11.G6.07 (Grade 6) - 1 grade below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G7.02: Design a coordinated set of 3-5 custom blocks for one game feature
**Grade:** 7
**Dependencies:**
- T11.G6.02 (Grade 6) ✓
- T11.G6.04 (Grade 6) ✓
- T11.G6.06 (Grade 6) ✓
- T11.G6.07 (Grade 6) ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G7.03: Understand encapsulation and information hiding
**Grade:** 7
**Dependencies:**
- T11.G6.01 (Grade 6) ✓
- T11.G6.04 (Grade 6) ✓
- T11.G6.08 (Grade 6) ✓
- T09.G5.01 (Grade 5) - 2 grades below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G7.04: Trace and debug multi-level custom block calls
**Grade:** 7
**Dependencies:**
- T11.G5.09 (Grade 5) - 2 grades below ✓
- T11.G6.04 (Grade 6) - 1 grade below ✓
- T11.G6.05 (Grade 6) - 1 grade below ✓
- T09.G5.01 (Grade 5) - 2 grades below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G8.01: Design general-purpose custom blocks with reusable interfaces
**Grade:** 8
**Dependencies:**
- T11.G6.01 (Grade 6) - 2 grades below ✓
- T11.G7.02 (Grade 7) - 1 grade below ✓
- T11.G7.03 (Grade 7) - 1 grade below ✓
- T02.G6.01 (Grade 6) - 2 grades below ✓
- T04.G6.01 (Grade 6) - 2 grades below ✓
- T07.G6.01 (Grade 6) - 2 grades below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G8.02: Demonstrate custom block reuse across multiple contexts
**Grade:** 8
**Dependencies:**
- T08.G6.01 (Grade 6) - 2 grades below ✓
- T09.G6.01 (Grade 6) - 2 grades below ✓
- T11.G8.01 (Grade 8) ✓
- T02.G6.01 (Grade 6) - 2 grades below ✓
- T04.G6.01 (Grade 6) - 2 grades below ✓
- T09.G6.02 (Grade 6) - 2 grades below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G8.03: Refactor a large program into a hierarchical block structure
**Grade:** 8
**Dependencies:**
- T11.G7.02 (Grade 7) - 1 grade below ✓
- T11.G7.03 (Grade 7) - 1 grade below ✓
- T11.G7.04 (Grade 7) - 1 grade below ✓
- T09.G6.01 (Grade 6) - 2 grades below ✓
- T17.G6.01 (Grade 6) - 2 grades below ✓
- T22.G6.01.01 (Grade 6) - 2 grades below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G8.04: Create custom blocks that work with lists and complex data
**Grade:** 8
**Dependencies:**
- T10.G7.01 (Grade 7) - 1 grade below ✓
- T11.G7.02 (Grade 7) - 1 grade below ✓
- T11.G7.03 (Grade 7) - 1 grade below ✓
- T07.G6.01 (Grade 6) - 2 grades below ✓
- T08.G6.01a (Grade 6) - 2 grades below ✓
- T09.G6.01 (Grade 6) - 2 grades below ✓

**Status:** ✓ NO VIOLATIONS

---

### T11.G8.05: Analyze trade-offs between modular and inline code
**Grade:** 8
**Dependencies:**
- T11.G7.03 (Grade 7) - 1 grade below ✓
- T11.G7.04 (Grade 7) - 1 grade below ✓
- T11.G8.03 (Grade 8) ✓
- T05.G6.01 (Grade 6) - 2 grades below ✓
- T09.G6.01 (Grade 6) - 2 grades below ✓
- T13.G6.01 (Grade 6) - 2 grades below ✓

**Status:** ✓ NO VIOLATIONS

---

## 2. MISSING INTRA-TOPIC DEPENDENCIES

### T11.G3.02: Use a pre-made custom block with parameters
**Current T11 Dependencies:** T11.G3.01
**Analysis:** ✓ CORRECT - Depends on understanding custom blocks first

---

### T11.G3.03: Identify repeated or grouped actions that could become custom blocks
**Current T11 Dependencies:** T11.G3.02
**Analysis:** ✓ CORRECT - Builds on using pre-made custom blocks

---

### T11.G3.04: Understand the concept of return values
**Current T11 Dependencies:** T11.G3.03
**Analysis:** ✓ CORRECT - Sequential progression

---

### T11.G3.05: Explore the "Make a Block" interface in CreatiCode
**Current T11 Dependencies:** T11.G3.04
**Analysis:** ✓ CORRECT - Final preparatory skill before Grade 4

---

### T11.G4.02: Distinguish command blocks from reporter blocks
**Current T11 Dependencies:** T11.G3.04
**Analysis:** ⚠️ MISSING T11.G4.01
**Reasoning:** Should depend on T11.G4.01 (Define and call a simple custom block) to understand custom command blocks before distinguishing them from reporters.

**Action Required:**
```
ADD dependency: T11.G4.02 → T11.G4.01
```

---

### T11.G4.03: Use a reporter block's result in a calculation or condition
**Current T11 Dependencies:** T11.G3.04
**Analysis:** ⚠️ MISSING T11.G4.02
**Reasoning:** Should depend on T11.G4.02 to distinguish reporters before using their results.

**Action Required:**
```
ADD dependency: T11.G4.03 → T11.G4.02
```

---

### T11.G4.04: Describe the purpose of each custom block in a script
**Current T11 Dependencies:** T11.G4.01, T11.G4.02
**Analysis:** ✓ CORRECT

---

### T11.G4.05: Trace execution through a script with custom blocks
**Current T11 Dependencies:** T11.G3.04, T11.G4.01, T11.G4.02
**Analysis:** ✓ CORRECT

---

### T11.G4.06: Understand the argument block for accessing parameters
**Current T11 Dependencies:** T11.G3.02
**Analysis:** ⚠️ MISSING T11.G4.01
**Reasoning:** Should depend on T11.G4.01 (basic custom block definition) before learning about the argument block mechanism.

**Action Required:**
```
ADD dependency: T11.G4.06 → T11.G4.01
```

---

### T11.G4.07: Define a custom block with one parameter
**Current T11 Dependencies:** T11.G4.01, T11.G4.06
**Analysis:** ✓ CORRECT

---

### T11.G4.08: Test a custom block with simple inputs
**Current T11 Dependencies:** T11.G4.07
**Analysis:** ✓ CORRECT

---

### T11.G5.01: Decompose a problem into logical custom block boundaries
**Current T11 Dependencies:** T11.G4.04, T11.G4.05
**Analysis:** ✓ CORRECT - High-level design skill building on understanding and tracing

---

### T11.G5.02: Use custom blocks with parameters in a larger project
**Current T11 Dependencies:** T11.G4.07, T11.G4.08
**Analysis:** ✓ CORRECT

---

### T11.G5.03: Match parameter names to argument values when calling custom blocks
**Current T11 Dependencies:** T11.G4.07, T11.G5.02
**Analysis:** ✓ CORRECT

---

### T11.G5.04: Choose between adding a parameter vs. creating a separate block
**Current T11 Dependencies:** T11.G5.01, T11.G5.03
**Analysis:** ✓ CORRECT

---

### T11.G5.05: Analyze a modular program structure
**Current T11 Dependencies:** T11.G4.04, T11.G4.05
**Analysis:** ⚠️ MISSING T11.G5.01
**Reasoning:** T11.G5.01 teaches decomposition planning, which should precede analyzing existing modular structures.

**Action Required:**
```
ADD dependency: T11.G5.05 → T11.G5.01
```

---

### T11.G5.06: Define a custom block with two or more parameters
**Current T11 Dependencies:** T11.G4.07, T11.G5.03
**Analysis:** ✓ CORRECT

---

### T11.G5.07: Decide whether a custom block should be a command or reporter
**Current T11 Dependencies:** T11.G4.02, T11.G4.07, T11.G5.02
**Analysis:** ✓ CORRECT

---

### T11.G5.08: Define a custom reporter block that returns a value
**Current T11 Dependencies:** T11.G4.03, T11.G5.07
**Analysis:** ✓ CORRECT

---

### T11.G5.09: Debug a script with incorrect custom block calls
**Current T11 Dependencies:** T11.G4.05, T11.G5.07
**Analysis:** ⚠️ MISSING T11.G5.08
**Reasoning:** Should include T11.G5.08 since debugging reporter blocks requires understanding them.

**Action Required:**
```
ADD dependency: T11.G5.09 → T11.G5.08
```

---

### T11.G5.10: Use comments to document custom block purpose
**Current T11 Dependencies:** T11.G4.07, T11.G5.08
**Analysis:** ✓ CORRECT

---

### T11.G5.11: Create custom blocks with mixed text labels and parameters
**Current T11 Dependencies:** T11.G5.06, T11.G5.10
**Analysis:** ✓ CORRECT

---

### T11.G6.01: Design custom blocks with clear, predictable interfaces
**Current T11 Dependencies:** T11.G5.04, T11.G5.05, T11.G5.06
**Analysis:** ✓ CORRECT

---

### T11.G6.02: Create modular programs with multiple custom blocks
**Current T11 Dependencies:** T11.G5.05, T11.G5.06
**Analysis:** ⚠️ MISSING T11.G6.01
**Reasoning:** Should depend on G6.01 (interface design) before creating multiple coordinated blocks.

**Action Required:**
```
ADD dependency: T11.G6.02 → T11.G6.01
```

---

### T11.G6.03: Test custom blocks with boundary and edge cases
**Current T11 Dependencies:** T11.G5.06, T11.G5.09
**Analysis:** ✓ CORRECT

---

### T11.G6.04: Refactor spaghetti code into organized custom blocks
**Current T11 Dependencies:** T11.G5.05
**Analysis:** ⚠️ MISSING T11.G6.01
**Reasoning:** Refactoring requires good interface design skills from G6.01.

**Action Required:**
```
ADD dependency: T11.G6.04 → T11.G6.01
```

---

### T11.G6.05: Add error handling to custom blocks
**Current T11 Dependencies:** T11.G5.06, T11.G6.03
**Analysis:** ✓ CORRECT

---

### T11.G6.06: Critique custom block naming and parameter choices
**Current T11 Dependencies:** T11.G5.04, T11.G5.11
**Analysis:** ⚠️ MISSING T11.G6.01
**Reasoning:** Critique requires understanding clear interfaces from G6.01.

**Action Required:**
```
ADD dependency: T11.G6.06 → T11.G6.01
```

---

### T11.G6.07: Evaluate custom block scope and single responsibility
**Current T11 Dependencies:** T11.G5.05, T11.G6.01
**Analysis:** ✓ CORRECT

---

### T11.G6.08: Critique return value usage in custom blocks
**Current T11 Dependencies:** T11.G5.07, T11.G5.08
**Analysis:** ✓ CORRECT

---

### T11.G7.01: Implement algorithms as reusable custom blocks
**Current T11 Dependencies:** T11.G5.08, T11.G6.04, T11.G6.07
**Analysis:** ⚠️ MISSING T11.G6.01
**Reasoning:** Implementing reusable algorithms requires clear interface design from G6.01.

**Action Required:**
```
ADD dependency: T11.G7.01 → T11.G6.01
```

---

### T11.G7.02: Design a coordinated set of 3-5 custom blocks for one game feature
**Current T11 Dependencies:** T11.G6.02, T11.G6.04, T11.G6.06, T11.G6.07
**Analysis:** ✓ CORRECT

---

### T11.G7.03: Understand encapsulation and information hiding
**Current T11 Dependencies:** T11.G6.01, T11.G6.04, T11.G6.08
**Analysis:** ⚠️ MISSING T11.G7.01
**Reasoning:** Understanding encapsulation benefits from experience implementing algorithms as reusable blocks.

**Action Required:**
```
ADD dependency: T11.G7.03 → T11.G7.01
```

---

### T11.G7.04: Trace and debug multi-level custom block calls
**Current T11 Dependencies:** T11.G5.09, T11.G6.04, T11.G6.05
**Analysis:** ⚠️ MISSING T11.G7.02
**Reasoning:** Multi-level tracing is easier with experience from coordinated block sets.

**Action Required:**
```
ADD dependency: T11.G7.04 → T11.G7.02
```

---

### T11.G8.01: Design general-purpose custom blocks with reusable interfaces
**Current T11 Dependencies:** T11.G6.01, T11.G7.02, T11.G7.03
**Analysis:** ✓ CORRECT

---

### T11.G8.02: Demonstrate custom block reuse across multiple contexts
**Current T11 Dependencies:** T11.G8.01
**Analysis:** ✓ CORRECT

---

### T11.G8.03: Refactor a large program into a hierarchical block structure
**Current T11 Dependencies:** T11.G7.02, T11.G7.03, T11.G7.04
**Analysis:** ✓ CORRECT

---

### T11.G8.04: Create custom blocks that work with lists and complex data
**Current T11 Dependencies:** T11.G7.02, T11.G7.03
**Analysis:** ⚠️ MISSING T11.G8.01
**Reasoning:** Working with complex data types requires general-purpose design from G8.01.

**Action Required:**
```
ADD dependency: T11.G8.04 → T11.G8.01
```

---

### T11.G8.05: Analyze trade-offs between modular and inline code
**Current T11 Dependencies:** T11.G7.03, T11.G7.04, T11.G8.03
**Analysis:** ✓ CORRECT

---

## 3. UNNECESSARY SAME-GRADE DEPENDENCIES

### Criterion
Within the same grade (e.g., T11.G5.XX), if skill A appears BEFORE skill B in sequence, then B should NOT explicitly list A as a dependency (it's implied by sequence).

### Analysis by Grade

#### Grade 3 (T11.G3.01 - T11.G3.05)
- T11.G3.02 → T11.G3.01 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G3.03 → T11.G3.02 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G3.04 → T11.G3.03 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G3.05 → T11.G3.04 ✓ (earlier in sequence, **UNNECESSARY**)

**Actions Required:**
```
REMOVE: T11.G3.02 → T11.G3.01
REMOVE: T11.G3.03 → T11.G3.02
REMOVE: T11.G3.04 → T11.G3.03
REMOVE: T11.G3.05 → T11.G3.04
```

---

#### Grade 4 (T11.G4.01 - T11.G4.08)
- T11.G4.02 → T11.G3.04 (different grade) ✓ KEEP
- T11.G4.03 → T11.G3.04 (different grade) ✓ KEEP
- T11.G4.04 → T11.G4.01 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G4.04 → T11.G4.02 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G4.05 → T11.G3.04 (different grade) ✓ KEEP
- T11.G4.05 → T11.G4.01 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G4.05 → T11.G4.02 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G4.06 → T11.G3.02 (different grade) ✓ KEEP
- T11.G4.07 → T11.G4.01 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G4.07 → T11.G4.06 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G4.08 → T11.G4.07 ✓ (earlier in sequence, **UNNECESSARY**)

**Actions Required:**
```
REMOVE: T11.G4.04 → T11.G4.01
REMOVE: T11.G4.04 → T11.G4.02
REMOVE: T11.G4.05 → T11.G4.01
REMOVE: T11.G4.05 → T11.G4.02
REMOVE: T11.G4.07 → T11.G4.01
REMOVE: T11.G4.07 → T11.G4.06
REMOVE: T11.G4.08 → T11.G4.07
```

---

#### Grade 5 (T11.G5.01 - T11.G5.11)
- T11.G5.01 → T11.G4.04, T11.G4.05 (different grade) ✓ KEEP
- T11.G5.02 → T11.G4.07, T11.G4.08 (different grade) ✓ KEEP
- T11.G5.03 → T11.G4.07 (different grade) ✓ KEEP
- T11.G5.03 → T11.G5.02 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G5.04 → T11.G5.01 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G5.04 → T11.G5.03 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G5.05 → T11.G4.04, T11.G4.05 (different grade) ✓ KEEP
- T11.G5.06 → T11.G4.07 (different grade) ✓ KEEP
- T11.G5.06 → T11.G5.03 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G5.07 → T11.G4.02, T11.G4.07 (different grade) ✓ KEEP
- T11.G5.07 → T11.G5.02 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G5.08 → T11.G4.03 (different grade) ✓ KEEP
- T11.G5.08 → T11.G5.07 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G5.09 → T11.G4.05 (different grade) ✓ KEEP
- T11.G5.09 → T11.G5.07 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G5.10 → T11.G4.07 (different grade) ✓ KEEP
- T11.G5.10 → T11.G5.08 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G5.11 → T11.G5.06 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G5.11 → T11.G5.10 ✓ (earlier in sequence, **UNNECESSARY**)

**Actions Required:**
```
REMOVE: T11.G5.03 → T11.G5.02
REMOVE: T11.G5.04 → T11.G5.01
REMOVE: T11.G5.04 → T11.G5.03
REMOVE: T11.G5.06 → T11.G5.03
REMOVE: T11.G5.07 → T11.G5.02
REMOVE: T11.G5.08 → T11.G5.07
REMOVE: T11.G5.09 → T11.G5.07
REMOVE: T11.G5.10 → T11.G5.08
REMOVE: T11.G5.11 → T11.G5.06
REMOVE: T11.G5.11 → T11.G5.10
```

---

#### Grade 6 (T11.G6.01 - T11.G6.08)
- T11.G6.01 → T11.G5.04, T11.G5.05, T11.G5.06 (different grade) ✓ KEEP
- T11.G6.02 → T11.G5.05, T11.G5.06 (different grade) ✓ KEEP
- T11.G6.03 → T11.G5.06, T11.G5.09 (different grade) ✓ KEEP
- T11.G6.04 → T11.G5.05 (different grade) ✓ KEEP
- T11.G6.05 → T11.G5.06 (different grade) ✓ KEEP
- T11.G6.05 → T11.G6.03 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G6.06 → T11.G5.04, T11.G5.11 (different grade) ✓ KEEP
- T11.G6.07 → T11.G5.05 (different grade) ✓ KEEP
- T11.G6.07 → T11.G6.01 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G6.08 → T11.G5.07, T11.G5.08 (different grade) ✓ KEEP

**Actions Required:**
```
REMOVE: T11.G6.05 → T11.G6.03
REMOVE: T11.G6.07 → T11.G6.01
```

---

#### Grade 7 (T11.G7.01 - T11.G7.04)
- T11.G7.01 → T11.G5.08, T11.G6.04, T11.G6.07 (different grade) ✓ KEEP
- T11.G7.02 → T11.G6.02, T11.G6.04, T11.G6.06, T11.G6.07 (different grade) ✓ KEEP
- T11.G7.03 → T11.G6.01, T11.G6.04, T11.G6.08 (different grade) ✓ KEEP
- T11.G7.04 → T11.G5.09, T11.G6.04, T11.G6.05 (different grade) ✓ KEEP

**No unnecessary same-grade dependencies in Grade 7**

---

#### Grade 8 (T11.G8.01 - T11.G8.05)
- T11.G8.01 → T11.G6.01, T11.G7.02, T11.G7.03 (different grade) ✓ KEEP
- T11.G8.02 → T11.G8.01 ✓ (earlier in sequence, **UNNECESSARY**)
- T11.G8.03 → T11.G7.02, T11.G7.03, T11.G7.04 (different grade) ✓ KEEP
- T11.G8.04 → T11.G7.02, T11.G7.03 (different grade) ✓ KEEP
- T11.G8.05 → T11.G7.03, T11.G7.04 (different grade) ✓ KEEP
- T11.G8.05 → T11.G8.03 ✓ (earlier in sequence, **UNNECESSARY**)

**Actions Required:**
```
REMOVE: T11.G8.02 → T11.G8.01
REMOVE: T11.G8.05 → T11.G8.03
```

---

## 4. SUMMARY OF RECOMMENDED CHANGES

### X-2 Rule Violations
**Count:** 0
**Status:** ✅ ALL SKILLS COMPLY WITH X-2 RULE

---

### Missing Intra-Topic Dependencies
**Count:** 10

1. ADD: T11.G4.02 → T11.G4.01
2. ADD: T11.G4.03 → T11.G4.02
3. ADD: T11.G4.06 → T11.G4.01
4. ADD: T11.G5.05 → T11.G5.01
5. ADD: T11.G5.09 → T11.G5.08
6. ADD: T11.G6.02 → T11.G6.01
7. ADD: T11.G6.04 → T11.G6.01
8. ADD: T11.G6.06 → T11.G6.01
9. ADD: T11.G7.01 → T11.G6.01
10. ADD: T11.G7.03 → T11.G7.01
11. ADD: T11.G7.04 → T11.G7.02
12. ADD: T11.G8.04 → T11.G8.01

---

### Unnecessary Same-Grade Dependencies
**Count:** 29

**Grade 3:** 4 removals
**Grade 4:** 7 removals
**Grade 5:** 10 removals
**Grade 6:** 2 removals
**Grade 7:** 0 removals
**Grade 8:** 2 removals

**Total removals:** 25

---

## 5. PRIORITY ACTIONS

### HIGH PRIORITY (Missing Critical Dependencies)

1. **T11.G4.02** needs T11.G4.01 - Can't distinguish custom command blocks without defining them first
2. **T11.G4.03** needs T11.G4.02 - Must distinguish reporters before using their results
3. **T11.G4.06** needs T11.G4.01 - Argument blocks only make sense after basic block definition
4. **T11.G6.01** is missing from multiple G6/G7 skills - Interface design is foundational

### MEDIUM PRIORITY (Logical Flow Issues)

5. **T11.G5.05** needs T11.G5.01 - Analysis follows design thinking
6. **T11.G5.09** needs T11.G5.08 - Debugging includes reporter blocks
7. **T11.G7.03** needs T11.G7.01 - Encapsulation concepts emerge from algorithm implementation
8. **T11.G7.04** needs T11.G7.02 - Multi-level tracing uses coordinated block sets

### LOW PRIORITY (Cleanup)

9. Remove all 25 unnecessary same-grade dependencies - These are implied by sequence ordering

---

## END OF ANALYSIS
