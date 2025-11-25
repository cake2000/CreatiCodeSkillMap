# GRADE 6 - TOP PRIORITY FIXES

## CRITICAL FIX #1: Replace T08.G3.01 (36 occurrences)

**Current:** T08.G3.01 - Use a simple if in a script
**Replace with:** T08.G4.01 or T08.G5.01

**Affected skills:**
- T23.G6.01.01: Capture a single spoken phrase with basic speech recognition
- T23.G6.01.02: Select speech recognition language
- T23.G6.01.03: Use continuous speech recognition
- T23.G6.01.04: Build a voice command system
- T23.G6.02.01: Classify images using basic vision blocks
- T23.G6.02.02: Use vision confidence scores
- T23.G6.02.03: Build a visual object detector
- T23.G6.03.01: Recognize facial expressions
- T23.G6.03.02: Build an emotion-responsive app
- T23.G6.04.01-07: Multiple AI perception skills
- T23.G6.06.01-04: Vision and speech skills
- T23.G6.08-12: Advanced AI skills
- T01.G6.04: Revise an algorithm to do less work
- T01.G6.07: Design a flowchart for a multi-step program
- T04.G6.04: Turn repeated code into a custom block
- T04.G6.06: Compare pattern-based solutions
- T13.G6.01: Trace complex code with multiple variables
- T13.G6.02: Use systematic debugging process
- T18.G6.03: Refactor repeated object creation
- T32.G6.05: Build a math quiz with score tracking

**Action:** Global find-replace T08.G3.01 → T08.G5.01 in all T23 G6 skills


## CRITICAL FIX #2: Replace T09.G3.01.04 (32 occurrences)

**Current:** T09.G3.01.04 - Display variable value on stage using monitor
**Replace with:** T09.G4.04 or T09.G5.01

**Affected skills:**
- T23.G6.01.01: Capture spoken phrase
- T23.G6.01.02: Select speech language
- T23.G6.01.03: Continuous speech recognition
- T23.G6.01.04: Voice command system
- T23.G6.02.01-03: Image classification skills
- T23.G6.03.01-02: Facial expression skills
- T23.G6.04.01-03: Object detection skills
- T23.G6.06.02-04: Vision skills
- T23.G6.08-12: Advanced AI skills
- T01.G6.03: Spot unnecessary work in algorithm
- T01.G6.07: Design flowchart
- T01.G6.08: Implement code from flowchart
- T03.G6.01: Propose modules for project
- T04.G6.01: Group snippets by pattern
- T13.G6.01: Trace complex code
- T13.G6.03: Design boundary tests
- T21.G6.03: Build prompt test bench
- T32.G6.05: Math quiz

**Action:** Global find-replace T09.G3.01.04 → T09.G5.01 in all affected skills


## MEDIUM PRIORITY: Add T09 dependency to T31 (Sorting)

**Current:** T31 has NO cross-topic dependencies
**Problem:** Sorting requires lists!

**Affected skills (ALL need T09.G5.01 or similar):**
- T31.G6.01: Implement bubble sort
- T31.G6.02: Implement selection sort
- T31.G6.03: Compare sorting algorithms
- T31.G6.03.01-03: Sorting sub-skills
- T31.G6.04: Implement insertion sort
- T31.G6.05: Implement merge sort
- T31.G6.06: Implement quick sort
- T31.G6.06.01: Quick sort partition

**Recommended addition:** T09.G5.01 (or T09.G4.04) to ALL T31.G6 skills


## MEDIUM PRIORITY: Add T09 dependency to T34 (Web Scraping)

**Current:** T34 has NO cross-topic dependencies
**Problem:** Web scraping stores data in lists!

**Affected skills:**
- T34.G6.01: Extract data from simple web page
- T34.G6.02: Parse structured data from HTML
- T34.G6.03: Build a web data collection tool

**Recommended addition:** T09.G5.01 to ALL T34.G6 skills


## LOW PRIORITY: Review T05 (Design Thinking) redundancies

**Current:** T05.G5.01 appears 183 times (often redundant)

This dependency is: "Write clear user needs and requirements for a small app"

Many skills depend on it both directly AND transitively through other deps.
Example: Skill X depends on both T05.G5.01 and T24.G5.03, but T24.G5.03
already depends on T05.G5.01.

**Recommendation:** Keep most of these! Design thinking is foundational.
Only remove if skill already has 5+ other dependencies.


## SPECIFIC EXAMPLE FIXES

### BEFORE (T23.G6.01.01):
```
Dependencies:
* T05.G5.01: Write clear user needs
* T06.G5.01: Identify standard event patterns
* T08.G3.01: Use a simple if  <--- VIOLATION
* T09.G3.01.04: Display variable monitor  <--- VIOLATION
* T09.G5.01: Use multiple variables
* T11.G5.01: Decompose into custom blocks
* T15.G5.01: Coordinate scene changes
* T23.G5.02: Explain why AI might mis-hear
```

### AFTER (T23.G6.01.01):
```
Dependencies:
* T05.G5.01: Write clear user needs
* T06.G5.01: Identify standard event patterns
* T08.G5.01: Design multi-branch decision logic  <--- FIXED
* T09.G5.01: Use multiple variables  <--- FIXED (already had G5)
* T11.G5.01: Decompose into custom blocks
* T15.G5.01: Coordinate scene changes
* T23.G5.02: Explain why AI might mis-hear
```


## SUMMARY OF FIXES NEEDED

1. T08.G3.01 → T08.G5.01: 36 skills (mostly T23)
2. T09.G3.01.04 → T09.G5.01: 32 skills (mostly T23)
3. T07.G3.01 → T07.G5.01: 5 skills
4. T06.G3.01 → T06.G5.01: 4 skills
5. Other G3 deps → G5 equivalents: 18 skills

**Total:** 95 fixes required
**Estimated effort:** 2-3 hours for systematic replacement
