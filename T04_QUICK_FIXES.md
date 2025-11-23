# T04 Algorithm Patterns - Quick Fix Summary

## Critical Issues (Fix First)

### 1. Split G3.04 into 3 skills

**Current G3.04**: Recognize a simple project template (TOO BROAD)

**Replace with:**
- **G3.04a**: Identify placeholder values vs hardcoded values in code
- **G3.04b**: Match code patterns to their customization points
- **G3.04c**: Recognize a simple project template (refined)

**Update dependencies for**: G3.05, G4.04, G4.08, G5.06, G6.05

### 2. Fix Counter Pattern Introduction

**Problem**: Mentioned in G3.08, not introduced until G5.01

**Actions:**
- **Revise G3.08**: Remove "counter" reference, focus only on loop and conditional patterns
- **Add G4.01b** (NEW): Recognize when code counts occurrences (before G5.01)

### 3. Add Nested Loop Scaffolding

**Problem**: G4.02 analyzes nested loops without prior introduction

**Action:**
- **Add G3.09** (NEW): Recognize that loops can contain other loops
- **Update G4.02** to depend on G3.09

### 4. Fix Dependency Errors (8 fixes)

1. **G3.03**: Change dependency from G2.03 to G3.01
2. **G3.06**: Remove T08.G3.01 (conditionals not needed for this task)
3. **G6.01**: Change from G4.04 to G4.05
4. **G6.02**: Change from G4.04 to G4.05
5. **G6.03**: Remove T04.G5.01 (counter not needed)
6. **G6.03**: Remove T01.G3.01 (G3 dependency in G6 violates progression)
7. **G8.02**: Fix skill name reference to match G8.01
8. **G3.03**: Should depend on G3.01 or G3.02 (skip issue)

## Medium Priority Issues

### 5. Add List Iteration Before Search

**Problem**: G5.03 (linear search) requires iterating through lists, but pattern not introduced

**Action:**
- **Add G4.09** (NEW): Recognize for-each loop pattern over list items
- **Update G5.03** to depend on G4.09

### 6. Simplify Filter Pattern

**Problem**: G5.04 combines loop + conditional + list add without scaffolding

**Action:**
- **Add G5.03b** (NEW): Recognize collect pattern (add items to list)
- **Update G5.04** to depend on G5.03b

### 7. Add Grid Pattern Scaffolding

**Problem**: G7.02 introduces grid pattern without preparation

**Action:**
- **Add G6.08** (NEW): Recognize 2D grid access pattern
- **Update G7.02** to depend on G6.08

### 8. Clarify Counter vs Accumulator

**Problem**: G5.02 introduces accumulator right after counter without distinguishing

**Action:**
- **Add G5.02a** (NEW): Distinguish counter vs accumulator patterns
- Place after G5.02, before G5.05

## Low Priority Polish

### 9. Library Pattern Introduction

**Action:**
- **Add G8.00** (NEW): Distinguish algorithm patterns from utility patterns
- **Update G8.01** description to reference utility patterns vs algorithm patterns

### 10. Add Implementation Notes

Add clarification to:
- **G3.04**: What makes code a "template"?
- **G3.08**: Which patterns should students recognize?
- **G4.06**: What are "known patterns" at this grade?
- **G8.01**: Examples of utility patterns

## New Skills Summary (8 total)

1. **G3.04a**: Identify placeholder vs hardcoded values
2. **G3.04b**: Match patterns to customization points
3. **G3.09**: Recognize nested loops (inner/outer)
4. **G4.01b**: Recognize counting in code
5. **G4.09**: Recognize for-each loop pattern
6. **G5.02a**: Distinguish counter vs accumulator
7. **G5.03b**: Recognize collect pattern
8. **G8.00**: Distinguish algorithm vs utility patterns

## Coordination Needed

- **T07 (Loops)**: Ensure nested loops introduced at G3 level before T04.G4.02
- **T09 (Variables)**: Verify counter/accumulator scaffolding aligns with T04.G5.01-G5.02
- **List Operations**: Ensure list iteration covered before T04.G5.03 needs it

## Quick Stats

- Total skills: 59
- Skills with issues: 22 (37%)
- Dependency fixes needed: 8
- New skills recommended: 8
- High priority issues: 4
- Medium priority issues: 4

## Implementation Order

1. Fix dependency errors (quick wins)
2. Split G3.04 into 3 skills
3. Add G3.09 (nested loops)
4. Revise G3.08 and add G4.01b (counter)
5. Add G4.09 (list iteration)
6. Add remaining scaffolding skills (G5.02a, G5.03b, G6.08, G8.00)
