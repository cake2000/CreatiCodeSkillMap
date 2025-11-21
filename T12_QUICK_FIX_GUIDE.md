# T12 Phase 1 Quick Fix Guide
**Topic:** T12 - Organizing Programs
**Date:** 2025-11-20

## Critical Fixes (Must Implement)

### 1. Remove Same-Grade T12 Dependencies

**Grade 3:**
```
T12.G3.02: Remove T12.G3.01 → Keep only T09.G3.02
T12.G3.03: Remove T12.G3.02 → Keep only T07.G3.03
T12.G3.04: Remove T12.G3.03 → Keep only T08.G3.03, T10.G3.02
```

**Grade 5 (simplify to single G4 dep):**
```
T12.G5.01: Remove T12.G4.03 → Keep only T12.G4.04
T12.G5.02: Remove T12.G4.03 → Keep T12.G3.01, T12.G4.04
T12.G5.03: Remove T12.G4.03 → Keep only T12.G4.04
T12.G5.04: Remove T12.G4.03 → Keep only T12.G4.04
```

**Grade 6 (simplify to single G5 dep):**
```
T12.G6.01: Remove T12.G5.03 → Keep T06.G3.01, T08.G3.01, T12.G5.04
T12.G6.02: Remove T12.G5.03 → Keep T07.G3.01, T08.G3.01, T12.G5.04
T12.G6.03: Remove T12.G1.01, T12.G5.03 → Keep T09.G3.01, T12.G5.04  ⚠️ CRITICAL
T12.G6.04: No change (already has only T12.G5.04)
```

**Grade 7 (simplify to single G6 dep):**
```
T12.G7.01: Remove T12.G6.03 → Keep T06.G3.01, T08.G5.01, T12.G6.04
T12.G7.02: Remove T12.G6.03 → Keep T08.G5.01, T12.G5.01, T12.G6.04
T12.G7.03: Remove T12.G6.03 → Keep T08.G5.01, T09.G5.01, T12.G6.04
T12.G7.04: Remove T12.G6.03 → Keep T07.G5.01, T09.G5.01, T12.G6.04
```

**Grade 8 (simplify to single G7 dep):**
```
T12.G8.01: Remove T12.G7.03 → Keep T06.G6.01, T09.G6.01, T12.G6.01, T12.G7.04
T12.G8.02: Remove T12.G7.03 → Keep T06.G6.01, T08.G6.01, T09.G6.01, T12.G7.04
T12.G8.03: Remove T12.G7.03 → Keep T06.G6.01, T08.G6.01, T12.G6.01, T12.G7.04
T12.G8.04: Remove T12.G7.03 → Keep T01.G6.01, T06.G6.01, T09.G6.01, T12.G7.04
```

---

### 2. Update Skill Descriptions (High Priority)

**T12.G3.01:**
```
OLD: "Write a comment explaining a complex block"
NEW: "Add simple labels or comments to organize blocks in a script"
WHY: Easier entry to block-based organization
```

---

## Recommended Fixes (Should Implement)

### 3. Clarify Skill Descriptions

**T12.G1.03:**
```
OLD: "Explain what each group of steps does"
NEW: "Tell what each group of steps does"
```

**T12.G5.01:**
```
OLD: "Create external documentation for a project"
NEW: "Create a README or project guide explaining what the program does"
```

**T12.G5.02:**
```
OLD: "Document code functionality and choices"
NEW: "Add inline comments explaining how code works and why choices were made"
```

**T12.G5.03:**
```
OLD: "Organize a multi-feature project with sections"
NEW: "Organize a project with 3+ features into labeled sections or scripts"
```

**T12.G5.04:**
```
OLD: "Review and improve another student's code organization"
NEW: "Review another student's code and suggest at least 2 organizational improvements"
```

**T12.G4.03:**
```
OLD: "Refactor repeated blocks into a custom block for clarity"
NEW: "Refactor repeated blocks into a custom block"
```

**T12.G6.01:**
```
OLD: "Analyze a program's organization and suggest improvements"
NEW: "Analyze a program's structure using a checklist and suggest specific improvements"
```

**T12.G7.02:**
```
OLD: "Analyze readability vs performance trade-offs"
NEW: "Compare two code versions and explain the readability vs performance trade-offs"
```

**T12.G8.03:**
```
OLD: "Refactor for maintainability in a team context"
NEW: "Refactor code for team maintainability and collaboration"
```

**T12.G8.04:**
```
OLD: "Evaluate and improve code for accessibility and inclusion"
NEW: "Review code for accessibility issues and implement 2+ improvements"
```

---

## Verification Checklist

After implementing fixes:

- [ ] T12.G6.03 no longer depends on T12.G1.01
- [ ] No T12 skill depends on earlier skill in same grade
- [ ] All T12 dependencies follow X-2 rule (max 2 grades back)
- [ ] All cross-topic dependencies preserved (T01, T03, T06, T07, T08, T09, T10, T11)
- [ ] All revised descriptions are more specific and assessable
- [ ] Grade 3 entry skill (G3.01) is appropriate for first coding-based org skill

---

## Summary Stats

**Dependency Removals:**
- Grade 3: 3 same-grade deps removed
- Grade 5: 4 redundant deps removed
- Grade 6: 5 deps removed (including CRITICAL T12.G1.01)
- Grade 7: 4 redundant deps removed
- Grade 8: 4 redundant deps removed
- **Total: 20 dependencies removed**

**Description Updates:**
- 1 HIGH priority (G3.01)
- 9 MEDIUM priority
- **Total: 10 descriptions revised**

**Net Result:**
- Cleaner dependency graph
- More specific, assessable skills
- Better progression G2→G3
- All X-2 rule violations fixed
