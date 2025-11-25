# T11 Functions & Procedures - Actionable Dependency Fixes

## Executive Summary

- **X-2 Rule Violations:** 0 ✅
- **Missing Dependencies:** 12 to add
- **Unnecessary Dependencies:** 25 to remove
- **Total Changes Required:** 37

---

## PART 1: ADD MISSING DEPENDENCIES (12 changes)

### Grade 4 Dependencies

```
T11.G4.02: Distinguish command blocks from reporter blocks
+ ADD: T11.G4.01 (Define and call a simple custom block)

T11.G4.03: Use a reporter block's result in a calculation or condition
+ ADD: T11.G4.02 (Distinguish command blocks from reporter blocks)

T11.G4.06: Understand the argument block for accessing parameters
+ ADD: T11.G4.01 (Define and call a simple custom block)
```

### Grade 5 Dependencies

```
T11.G5.05: Analyze a modular program structure
+ ADD: T11.G5.01 (Decompose a problem into logical custom block boundaries)

T11.G5.09: Debug a script with incorrect custom block calls
+ ADD: T11.G5.08 (Define a custom reporter block that returns a value)
```

### Grade 6 Dependencies

```
T11.G6.02: Create modular programs with multiple custom blocks
+ ADD: T11.G6.01 (Design custom blocks with clear, predictable interfaces)

T11.G6.04: Refactor spaghetti code into organized custom blocks
+ ADD: T11.G6.01 (Design custom blocks with clear, predictable interfaces)

T11.G6.06: Critique custom block naming and parameter choices
+ ADD: T11.G6.01 (Design custom blocks with clear, predictable interfaces)
```

### Grade 7 Dependencies

```
T11.G7.01: Implement algorithms as reusable custom blocks
+ ADD: T11.G6.01 (Design custom blocks with clear, predictable interfaces)

T11.G7.03: Understand encapsulation and information hiding
+ ADD: T11.G7.01 (Implement algorithms as reusable custom blocks)

T11.G7.04: Trace and debug multi-level custom block calls
+ ADD: T11.G7.02 (Design a coordinated set of 3-5 custom blocks for one game feature)
```

### Grade 8 Dependencies

```
T11.G8.04: Create custom blocks that work with lists and complex data
+ ADD: T11.G8.01 (Design general-purpose custom blocks with reusable interfaces)
```

---

## PART 2: REMOVE UNNECESSARY SAME-GRADE DEPENDENCIES (25 changes)

### Grade 3 (4 removals)

```
T11.G3.02: Use a pre-made custom block with parameters
- REMOVE: T11.G3.01

T11.G3.03: Identify repeated or grouped actions that could become custom blocks
- REMOVE: T11.G3.02

T11.G3.04: Understand the concept of return values
- REMOVE: T11.G3.03

T11.G3.05: Explore the "Make a Block" interface in CreatiCode
- REMOVE: T11.G3.04
```

### Grade 4 (7 removals)

```
T11.G4.04: Describe the purpose of each custom block in a script
- REMOVE: T11.G4.01
- REMOVE: T11.G4.02

T11.G4.05: Trace execution through a script with custom blocks
- REMOVE: T11.G4.01
- REMOVE: T11.G4.02

T11.G4.07: Define a custom block with one parameter
- REMOVE: T11.G4.01
- REMOVE: T11.G4.06

T11.G4.08: Test a custom block with simple inputs
- REMOVE: T11.G4.07
```

### Grade 5 (10 removals)

```
T11.G5.03: Match parameter names to argument values when calling custom blocks
- REMOVE: T11.G5.02

T11.G5.04: Choose between adding a parameter vs. creating a separate block
- REMOVE: T11.G5.01
- REMOVE: T11.G5.03

T11.G5.06: Define a custom block with two or more parameters
- REMOVE: T11.G5.03

T11.G5.07: Decide whether a custom block should be a command or reporter
- REMOVE: T11.G5.02

T11.G5.08: Define a custom reporter block that returns a value
- REMOVE: T11.G5.07

T11.G5.09: Debug a script with incorrect custom block calls
- REMOVE: T11.G5.07

T11.G5.10: Use comments to document custom block purpose
- REMOVE: T11.G5.08

T11.G5.11: Create custom blocks with mixed text labels and parameters
- REMOVE: T11.G5.06
- REMOVE: T11.G5.10
```

### Grade 6 (2 removals)

```
T11.G6.05: Add error handling to custom blocks
- REMOVE: T11.G6.03

T11.G6.07: Evaluate custom block scope and single responsibility
- REMOVE: T11.G6.01
```

### Grade 8 (2 removals)

```
T11.G8.02: Demonstrate custom block reuse across multiple contexts
- REMOVE: T11.G8.01

T11.G8.05: Analyze trade-offs between modular and inline code
- REMOVE: T11.G8.03
```

---

## PRIORITY ORDER FOR IMPLEMENTATION

### Phase 1: Critical Grade 4 Fixes (HIGH PRIORITY)
These affect the foundation of custom blocks understanding:

1. T11.G4.02 + T11.G4.01
2. T11.G4.03 + T11.G4.02
3. T11.G4.06 + T11.G4.01

### Phase 2: Grade 6 Interface Design Dependencies (HIGH PRIORITY)
T11.G6.01 is missing from many skills:

4. T11.G6.02 + T11.G6.01
5. T11.G6.04 + T11.G6.01
6. T11.G6.06 + T11.G6.01
7. T11.G7.01 + T11.G6.01

### Phase 3: Higher-Grade Logical Flow (MEDIUM PRIORITY)

8. T11.G5.05 + T11.G5.01
9. T11.G5.09 + T11.G5.08
10. T11.G7.03 + T11.G7.01
11. T11.G7.04 + T11.G7.02
12. T11.G8.04 + T11.G8.01

### Phase 4: Cleanup (LOW PRIORITY)
Remove all 25 unnecessary same-grade dependencies (these are implied by sequence)

---

## VERIFICATION CHECKLIST

After making changes, verify:

- [ ] All Grade 4 skills properly chain through T11.G4.01
- [ ] T11.G6.01 appears in dependencies for all Grade 6-7 skills that need interface design
- [ ] No same-grade dependencies point to earlier skills in sequence
- [ ] All cross-topic dependencies (to T01-T10, T12+) are preserved
- [ ] X-2 rule still satisfied (no violations should be introduced)

---

## NOTES

### Why Same-Grade Sequential Dependencies Are Unnecessary

Within a grade, skills are implicitly ordered. If T11.G5.03 comes after T11.G5.02 in the curriculum sequence, students will naturally complete them in order. Explicitly listing T11.G5.02 as a dependency of T11.G5.03 is redundant.

**Exception:** Dependencies should be listed when:
- They cross grades (e.g., G5 skill depends on G4 skill)
- They skip over intermediate skills in the same grade (e.g., G5.08 depends on G5.02, skipping G5.03-G5.07)

### Why These Missing Dependencies Matter

The missing dependencies identified represent logical prerequisites where:
- A concept must be understood before being applied (e.g., define blocks before distinguishing types)
- A basic skill must be mastered before a more complex version (e.g., basic tracing before multi-level tracing)
- A foundational design principle must be learned before applying it (e.g., interface design before refactoring)

---

## END OF ACTIONABLE FIXES
