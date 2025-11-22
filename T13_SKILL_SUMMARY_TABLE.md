# T13 Skills Summary Table

| Skill ID | Grade | Skill Title | Dependencies Count | Notes |
|----------|-------|-------------|-------------------|-------|
| T13.GK.01 | K | Spot a missing or wrong action in an animation | 0 | Foundation skill |
| T13.GK.02 | K | Retry after noticing something went wrong | 1 | |
| T13.GK.03 | K | Fix a single wrong direction or action in steps | 2 | |
| T13.G1.01 | 1 | Identify which step causes a problem and explain why | 1 | |
| T13.G1.02 | 1 | Fix a sequence error in steps | 1 | |
| T13.G1.03 | 1 | Change a number to fix a repeated action | 1 | |
| T13.G1.04 | 1 | Demonstrate steps physically and identify the error | 1 | |
| T13.G2.01 | 2 | Fix steps that use the wrong signal | 1 | |
| T13.G2.02 | 2 | Trace a set of steps and predict behavior | 2 | Important foundation |
| T13.G2.03 | 2 | Fix a repeated step that happens too many or too few times | 2 | |
| T13.G2.04 | 2 | Add a simple check to see if steps worked | 2 | |
| T13.G3.01 | 3 | Test a simple block-based script | 2 | First coding skill |
| T13.G3.01b | 3 | Trace a block script step-by-step before running it | 2 | ISSUE: Use decimal notation |
| T13.G3.02 | 3 | Fix a wrong block in a sequence | 2 | |
| T13.G3.03 | 3 | Debug a script with a missing block | 2 | |
| T13.G3.04 | 3 | Try again and adjust when program doesn't work | 2 | |
| T13.G3.05 | 3 | Identify which block causes unexpected behavior | 2 | |
| T13.G4.01 | 4 | Debug a conditional inside a loop | 3 | First nested debugging |
| T13.G4.02 | 4 | Identify and manually test edge cases | 3 | |
| T13.G4.03 | 4 | Design an alternative approach and compare results | 3 | |
| T13.G4.04 | 4 | Identify and fix an infinite loop or program hang | 3 | |
| T13.G4.05.01 | 4 | Create a simple test plan with documented test cases | 2 | Testing series |
| T13.G4.05.02 | 4 | Run tests and record results | 1 | Testing series |
| T13.G4.06 | 4 | Compare two programs solving the same task | 2 | |
| T13.G4.07 | 4 | Debug complex two-level nested structures | 3 | |
| T13.G4.08 | 4 | Record what went wrong and how you fixed it | 1 | Documentation |
| T13.G4.09 | 4 | Distinguish between different types of bugs | 3 | Bug taxonomy |
| T13.G5.01 | 5 | Debug programs using tracing and logging | 2 | |
| T13.G5.02 | 5 | Add input validation to handle invalid entries | 2 | |
| T13.G5.03 | 5 | Create and follow a comprehensive test plan | 1 | |
| T13.G5.04 | 5 | Modify a program to improve reliability and correctness | 3 | |
| T13.G5.05 | 5 | Debug deeply nested structures (three+ levels) | 3 | ISSUE: Dep title mismatch |
| T13.G6.01 | 6 | Trace complex code with multiple variables | 4 | Most dependencies |
| T13.G6.02 | 6 | Use a systematic debugging process | 2 | |
| T13.G6.03 | 6 | Design systematic boundary tests | 2 | |
| T13.G6.04 | 6 | Document known limitations and potential bugs | 2 | |
| T13.G7.01 | 7 | Write comprehensive test cases for an algorithm | 3 | ISSUE: Depends on T08.G5.01 |
| T13.G7.02 | 7 | Debug logic errors in complex programs | 3 | ISSUE: Depends on T08.G5.01 |
| T13.G7.03 | 7 | Refactor for testability and clarity | 3 | ISSUE: Depends on T08.G5.01 |
| T13.G7.04 | 7 | Compare reliability of different program designs | 3 | ISSUE: Depends on T08.G5.01 |
| T13.G7.05 | 7 | Anticipate runtime errors and add defensive checks | 3 | ISSUE: Depends on T08.G5.01 |
| T13.G8.01 | 8 | Design and execute a rigorous test suite | 3 | |
| T13.G8.02 | 8 | Debug for correctness against specifications | 3 | |
| T13.G8.03 | 8 | Handle errors gracefully with defensive programming patterns | 3 | |
| T13.G8.04 | 8 | Evaluate code correctness, edge case coverage, and assumptions | 3 | Metacognitive |

## Statistics by Grade

| Grade | Skill Count | Avg Dependencies | Notes |
|-------|-------------|-----------------|--------|
| K | 3 | 1.0 | Unplugged, foundational |
| 1 | 4 | 1.0 | Unplugged, explanatory |
| 2 | 4 | 1.75 | Unplugged, predictive |
| 3 | 6 | 2.0 | First block coding |
| 4 | 9 | 2.4 | HEAVY - consider redistribution |
| 5 | 5 | 2.2 | Robust programming |
| 6 | 4 | 2.5 | Systematic methods |
| 7 | 5 | 3.0 | Professional practices |
| 8 | 4 | 3.0 | Advanced analysis |

## Key Skill Chains

### Testing Progression
1. G3: T13.G3.01 - Test a simple script
2. G4: T13.G4.05.01 - Create test plan
3. G4: T13.G4.05.02 - Run tests and record
4. G5: T13.G5.03 - Comprehensive test plan
5. G6: T13.G6.03 - Systematic boundary tests
6. G7: T13.G7.01 - Test cases for algorithms
7. G8: T13.G8.01 - Rigorous test suite

### Debugging Nested Structures
1. G4: T13.G4.01 - Conditional inside loop (1 level)
2. G4: T13.G4.07 - Two-level nesting
3. G5: T13.G5.05 - Three+ levels
4. G6: T13.G6.01 - Complex code with multiple variables

### Error Handling Progression
1. G4: T13.G4.02 - Identify edge cases
2. G5: T13.G5.02 - Input validation
3. G6: T13.G6.03 - Boundary tests
4. G7: T13.G7.05 - Anticipate runtime errors
5. G8: T13.G8.03 - Defensive programming patterns

### Documentation Progression
1. G4: T13.G4.08 - Record fixes
2. G6: T13.G6.04 - Document limitations
3. G7: T13.G7.03 - Refactor for clarity
4. G8: T13.G8.04 - Critical code evaluation
