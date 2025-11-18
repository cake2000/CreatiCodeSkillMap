# Critical Learning Paths: T06-T13 Programming Core

**Purpose:** This document identifies the essential skill progressions through the Programming Core topics (T06-T13) that enable students to become proficient programmers.

---

## Overview: The 5 Critical Paths

Programming education isn't linear - it's a network of interconnected skills. However, certain sequences are **critical** - without mastering these paths, students cannot progress to meaningful programming.

### The 5 Paths

1. **Path 1: The Bridge to Coding** (Grades 1-3) - Unplugged → Actual Programming
2. **Path 2: The Three Pillars** (Grade 3) - Events, Loops, Conditionals
3. **Path 3: Data-Driven Programming** (Grades 3-5) - Variables → Lists → Algorithms
4. **Path 4: Modular Programming** (Grades 4-6) - Decomposition → Functions → Organization
5. **Path 5: Quality Programming** (Grades 3-8) - Tracing → Debugging → Testing → Robustness

---

## Path 1: The Bridge to Coding

**Grades:** 1-3
**Purpose:** Transition from unplugged thinking to actual code
**Status:** THE most critical path - without this, programming cannot begin

### The Progression

```
[Grade 1: Unplugged Foundation]
T01.G1.01: Write or draw steps for a simple task
  ↓
T02.G1.01: Create an algorithm in pictures and words
  ↓
T03.G1.02: Break a simple task into steps

[Grade 2: Conceptual Programming]
  ↓
T01.G2.01: Write an algorithm with "if/then" choice
  ↓
T01.G2.02: Write an algorithm with a repeat statement
  ↓
T02.G2.01: Represent a simple algorithm with blocks or boxes
  ↓
T04.G2.02: Replace repeated code with a loop (conceptual)

[Grade 3: THE BRIDGE - Actual Coding Begins]
  ↓
T06.G3.01: Create independent scripts with different events ★ GATEWAY
  ↓
[ALL programming skills in grades 3-8]
```

### Why This Path is Critical

**Before T06.G3.01:** Students are thinking about programming
**After T06.G3.01:** Students are DOING programming

This is the single most important transition in K-8 CS education.

### Dependencies

- **T01 (Algorithms):** Provides the conceptual foundation for step-by-step thinking
- **T02 (Representation):** Helps students understand that code is just another representation
- **T03 (Decomposition):** Enables breaking down problems into programmable steps
- **T04 (Patterns):** Helps recognize when to use loops

### Teaching Implications

1. **Grades 1-2 are NOT optional** - The unplugged foundation is essential
2. **Grade 3 needs extended time** - The bridge year requires 40-50% focus on T06-T09
3. **Mastery, not exposure** - Students must MASTER T06.G3.01 before advancing
4. **Scaffolding is critical** - First coding experiences need heavy support

### Common Pitfalls

❌ **Rushing grade 1-2:** "They're too young for unplugged? Skip to coding in grade 3"
   - Result: Students don't understand what programming IS

❌ **Skipping T06 mastery:** "They made a program work once, move on"
   - Result: Students can't debug or create their own programs

❌ **Too much too fast:** "We taught events, loops, and conditionals in 3 weeks"
   - Result: Surface-level understanding, can't combine concepts

### Success Indicators

✅ Student can explain what an event is and why programs need them
✅ Student can create a simple program from scratch (not just modify examples)
✅ Student can identify and fix simple sequencing errors
✅ Student shows excitement about making the computer do what they want

---

## Path 2: The Three Pillars

**Grades:** 3
**Purpose:** Master the three core programming constructs
**Status:** Essential foundation for all subsequent programming

### The Progression

```
[Foundation: Events]
T06.G3.01: Create independent scripts with different events ★ GATEWAY
  ↓
[The Three Pillars - can be learned in parallel]
  ├─→ T07.G3.01: Use repeat-until to reach a goal ★ GATEWAY
  │     └─→ Loops enable AUTOMATION
  │
  ├─→ T08.G3.01: Use if/else in a game or interaction loop ★ GATEWAY
  │     └─→ Conditionals enable DECISIONS
  │
  └─→ T09.G3.01: Use different variable types ★ GATEWAY
        └─→ Variables enable DATA STORAGE

[Integration - Combining the Pillars]
  ↓
T07.G4.01 + T08.G4.01 + T09.G4.01: Using loops, conditionals, and variables together
  ↓
[Complex programming in grades 5-8]
```

### Why This Path is Critical

**These three constructs are the "atoms" of programming:**
- Nearly every program uses events, loops, conditionals, and variables
- Advanced topics (functions, lists, testing) build on these three
- Real-world programming requires combining all three

**You cannot build houses from atoms** - but you need atoms to build houses.

### Dependencies

```
T07 (Loops) depends on:
  - T06.G3.01 (Events - to run the loop)
  - T01.G2.02 (Algorithms with repeat)
  - T04.G2.01 (Pattern recognition)

T08 (Conditionals) depends on:
  - T06.G3.01 (Events - to run the conditional)
  - T01.G2.01 (Algorithms with if/then)

T09 (Variables) depends on:
  - T06.G3.01 (Events - to set/use variables)
```

### Teaching Implications

1. **Teach pillars in parallel, not sequence**
   - Don't do "2 weeks loops, 2 weeks conditionals, 2 weeks variables"
   - Instead: Introduce all three, then practice combining them

2. **Every project should use multiple pillars**
   - "Loop-only" projects don't reflect real programming
   - Example: "Count to 10 with a loop" → "Count to 10, but celebrate multiples of 5"
     (Adds conditionals to the loop)

3. **Emphasize the "why" of each pillar**
   - Loops: "How do we avoid repetitive code?"
   - Conditionals: "How do we make different things happen in different situations?"
   - Variables: "How do we remember information?"

### Integration Patterns

**Grade 3-4:** Pairs of pillars
- Loops + Variables (loop counter)
- Loops + Conditionals (repeat until condition)
- Conditionals + Variables (if score > 10)

**Grade 5-6:** All three together
- Loop through numbers, check condition, update variable
- Example: "Find the largest number in a list"

**Grade 7-8:** Nested and complex combinations
- Nested loops with conditionals
- Multiple variables with complex logic

### Success Indicators

✅ Student can explain when to use each pillar
✅ Student can combine two pillars in a project
✅ Student can debug problems involving multiple pillars
✅ Student chooses the right construct for the problem

---

## Path 3: Data-Driven Programming

**Grades:** 3-5
**Purpose:** Enable working with realistic data and collections
**Status:** Critical for applications (games, data science, AI)

### The Progression

```
[Foundation: Variables]
T09.G3.01: Use different variable types (number, text, boolean) ★ GATEWAY
  ↓
T09.G4.01: Store and use user input in a variable ★ GATEWAY
  ↓
T09.G4-G5: Variable expressions and calculations

[Collections: Lists]
  ↓
T10.G4.01: Use nested loops to process 2D arrangements ★ GATEWAY
  ↓
T10.G4-G5: List operations (add, remove, search, access by index)

[Algorithms on Data]
  ↓
T07.G5+ + T10.G5+: Iterate through lists
  ↓
T08.G5+ + T10.G5+: Filter and search lists
  ↓
T07 + T08 + T10: Sort, aggregate, analyze data

[Applications]
  ↓
- Games: Inventories, high scores, player stats
- Data Science: Analyze datasets
- AI: Training data, pattern recognition
- Simulations: Track multiple entities
```

### Why This Path is Critical

**Modern programming is data-driven:**
- Games track scores, inventories, enemy positions
- Data science analyzes datasets
- AI learns from data
- Simulations model multiple entities

**Without lists, students are limited to trivial problems with 1-3 pieces of data.**

### Dependencies

```
Lists depend on:
  - T09.G3.01: Variables (lists are containers of variables)
  - T07.G3.01: Loops (to iterate through lists)
  - T06.G3.01: Events (to run the code)

List operations depend on:
  - T08.G3.01: Conditionals (for filtering, searching)
  - T07.G4+: Loops (for iteration)

Advanced algorithms depend on:
  - All three pillars (T07, T08, T09)
  - Lists (T10)
```

### Teaching Implications

1. **Start with single variables, progress to lists**
   - Grade 3: One variable (score)
   - Grade 4: Multiple variables (score, lives, level)
   - Grade 4-5: Lists (high scores, inventory)

2. **Use realistic data**
   - Not: "Make a list of three numbers"
   - Better: "Track the high scores of 10 players"
   - Best: "Import real weather data and find the hottest day"

3. **Emphasize algorithms on data**
   - Finding (search)
   - Filtering (select subset)
   - Aggregating (sum, average, max, min)
   - Sorting (order by criterion)

### Common Applications

**Games:**
- High score tables (list of scores)
- Inventory systems (list of items)
- Enemy positions (list of coordinates)

**Data Science:**
- Analyze test scores (list of numbers)
- Find patterns in data (search and filter)
- Calculate statistics (aggregate)

**Simulations:**
- Track multiple sprites (list of positions/velocities)
- Model populations (list of entities)

### Success Indicators

✅ Student can create and populate a list
✅ Student can iterate through a list with a loop
✅ Student can search a list for a specific item
✅ Student can explain when to use a list vs. multiple variables

---

## Path 4: Modular Programming

**Grades:** 4-6
**Purpose:** Enable scalable, maintainable code
**Status:** Critical for larger projects and collaboration

### The Progression

```
[Foundation: Decomposition Thinking]
T03.G3.01: Decompose a project into scenes and features
  ↓
T03.G4.01: Assess whether a design is well-decomposed
  ↓
T03.G4.02: Refactor code to separate concerns

[Functions: Code Reuse]
  ↓
T11.G4.01: Create a custom block that returns a value ★ GATEWAY
  ↓
T11.G5.01-G5.02: Custom blocks with parameters
  ↓
T11.G5.03: Decide between parameter and separate block ★ GATEWAY

[Organization: Maintainable Code]
  ↓
T12.G4-G5: Comments, naming, structure
  ↓
T12.G6-G7: Refactoring, style conventions
  ↓
T03.G7-G8 + T11.G7-G8 + T12.G7-G8: Architectural patterns

[Applications]
  ↓
- Large projects (games, apps)
- Reusable libraries
- Team collaboration
- Maintainable codebases
```

### Why This Path is Critical

**Without modularization:**
- Projects are limited to ~50-100 lines of code
- Code is hard to debug and maintain
- Collaboration is nearly impossible
- Students can't tackle realistic problems

**With modularization:**
- Projects can scale to 500+ lines
- Code is organized and understandable
- Collaboration becomes possible
- Students can build professional-quality software

### Dependencies

```
Functions depend on:
  - T03.G3+: Decomposition (breaking into reusable parts)
  - T06.G3.01: Events (to call functions)
  - T09.G3.01: Variables (for parameters)

Organization depends on:
  - T03.G4+: Decomposition
  - T11.G4+: Functions (to organize code)
  - Having written code to organize!
```

### Teaching Implications

1. **Introduce functions when projects get messy**
   - Don't teach functions in isolation
   - Wait until students feel the pain of repetitive code
   - Then: "There's a better way..."

2. **Emphasize the "why" of modularization**
   - Reuse: "Write once, use many times"
   - Readability: "Name what it does"
   - Debugging: "Test one part at a time"
   - Collaboration: "Each person owns a function"

3. **Practice refactoring**
   - Start with messy code
   - Identify repeated patterns
   - Extract to functions
   - Observe the improvement

### Progression of Abstraction

**Grade 4:** Simple custom blocks (no parameters)
- Example: "Make a custom block for 'draw a square'"

**Grade 5:** Parameterized custom blocks
- Example: "Make a custom block for 'draw a square of size N'"

**Grade 6:** Custom blocks with return values
- Example: "Make a custom block that 'calculates distance between two points'"

**Grade 7-8:** Libraries and modules
- Example: "Make a library of geometry functions for your game"

### Success Indicators

✅ Student recognizes when to create a custom block
✅ Student can explain the benefits of functions
✅ Student uses parameters effectively
✅ Student's projects are organized and readable

---

## Path 5: Quality Programming

**Grades:** 3-8
**Purpose:** Ensure code correctness and robustness
**Status:** Critical for real-world programming

### The Progression

```
[Foundation: Understanding Execution]
T02.G3.01: Create a simple flowchart with start, end, and action boxes
  ↓
T02.G3.02-G3.04: Trace programs with conditions and loops
  ↓
T02.G4-G5: Trace complex programs

[Debugging: Fixing Problems]
  ↓
T13.G3.01: Debug a conditional inside a loop ★ GATEWAY
  ↓
T13.G4.01-G4.02: Systematic debugging strategies
  ↓
T13.G5.01-G5.02: Debugging with multiple constructs

[Testing: Preventing Problems]
  ↓
T13.G5.03: Create test cases for a program
  ↓
T13.G6.01-G6.02: Systematic testing, edge cases
  ↓
T13.G7-G8: Test planning, error handling, robustness

[Quality Code]
  ↓
- Code that works correctly
- Code that handles edge cases
- Code that fails gracefully
- Code that can be maintained
```

### Why This Path is Critical

**The difference between student code and professional code is quality:**

**Student mindset:** "It worked once, I'm done"
**Professional mindset:** "Does it work in all cases? What if the user does something unexpected?"

**Without quality practices:**
- Code breaks in unexpected ways
- Debugging takes hours
- Users encounter errors
- Projects are abandoned

**With quality practices:**
- Code is reliable
- Debugging is systematic
- Edge cases are handled
- Projects are maintained

### Dependencies

```
Testing depends on:
  - T02.G3+: Tracing (understanding execution)
  - T06.G3.01: Events (having code to test)
  - Any programming construct being tested

Debugging depends on:
  - T02.G3+: Tracing
  - Understanding the construct being debugged

Error handling depends on:
  - T08.G5+: Conditionals (to check for errors)
  - T13.G5+: Testing (to identify what can go wrong)
```

### Teaching Implications

1. **Integrate testing from day one**
   - Don't wait for "the testing unit"
   - First program → first debugging experience
   - Testing is not a separate topic, it's part of programming

2. **Teach systematic debugging**
   - Not: "Try random things until it works"
   - Instead: "What do we expect? What actually happened? What could cause that difference?"

3. **Emphasize edge cases**
   - What if the list is empty?
   - What if the number is negative?
   - What if the user types text instead of a number?

4. **Make debugging a normal part of programming**
   - "Bugs are learning opportunities"
   - "Professional programmers spend 50% of time debugging"
   - "Good debuggers are good programmers"

### Progression of Testing

**Grade 3:** Observation testing
- "Run the program, see if it looks right"

**Grade 4:** Systematic testing
- "Test it with different inputs"

**Grade 5:** Test cases
- "Plan what to test before testing"

**Grade 6:** Edge case testing
- "What could go wrong?"

**Grade 7-8:** Error handling
- "Make it fail gracefully"

### Success Indicators

✅ Student tests code before claiming it's done
✅ Student can trace program execution step-by-step
✅ Student uses systematic debugging strategies
✅ Student considers edge cases
✅ Student's code handles errors gracefully

---

## Cross-Path Dependencies

The five paths are not independent - they interact and reinforce each other:

### Path Intersections

**Path 1 × Path 2:** The bridge enables the pillars
- T06.G3.01 (events) is required for T07.G3.01 (loops), T08.G3.01 (conditionals), T09.G3.01 (variables)

**Path 2 × Path 3:** The pillars enable data
- Variables (Path 2) are required for lists (Path 3)
- Loops (Path 2) are required for list iteration (Path 3)
- Conditionals (Path 2) are required for list filtering (Path 3)

**Path 2 × Path 4:** The pillars enable modularization
- Functions (Path 4) use variables (Path 2) as parameters
- Functions (Path 4) often contain loops and conditionals (Path 2)

**Path 2 × Path 5:** The pillars require testing
- Every programming construct (Path 2) needs testing (Path 5)
- More complex constructs require more sophisticated testing

**Path 4 × Path 5:** Modularization enables testing
- Functions (Path 4) can be tested independently
- Good organization (Path 4) makes debugging (Path 5) easier

### The Complete Picture

```
[Grades 1-2: Unplugged Foundation]
Path 1: Building conceptual understanding
  ↓
[Grade 3: THE GATEWAY YEAR]
Path 1 → Path 2 → Path 5
T06.G3.01 → T07/T08/T09.G3.01 → T13.G3.01
Events → Loops/Conditionals/Variables → Debugging
  ↓
[Grades 4-5: Integration]
Path 2 + Path 3 + Path 4 + Path 5
Combining pillars + Data structures + Functions + Testing
  ↓
[Grades 6-8: Sophistication]
All paths operating together
Complex applications requiring all skills
```

---

## Teaching Sequence Recommendations

### Grade 1-2: Unplugged (Path 1)

**Focus:** Conceptual foundation
**Time:** Full year, integrated across subjects

**Sequence:**
1. Algorithms (T01) - "What are step-by-step instructions?"
2. Decomposition (T03) - "How do we break down problems?"
3. Patterns (T04) - "What repeats? What's the rule?"
4. Representation (T02) - "How can we show algorithms?"

### Grade 3: Gateway Year (Paths 1, 2, 5)

**Focus:** Bridge to coding + Core constructs
**Time:** 40-50% of year on T06-T09

**Sequence:**
1. **Weeks 1-4:** T06.G3.01 (Events) - MASTER THIS
   - Green flag, clicks, keys
   - Multiple sprites, independent scripts
   - Practice until automatic

2. **Weeks 5-8:** T07.G3.01 (Loops) - Add automation
   - Repeat blocks
   - Repeat-until
   - Combining loops and events

3. **Weeks 9-12:** T08.G3.01 (Conditionals) - Add decisions
   - If/else blocks
   - Sensing and responding
   - Combining conditionals and events

4. **Weeks 13-16:** T09.G3.01 (Variables) - Add data
   - Number, text, boolean variables
   - Updating variables
   - Combining variables with loops/conditionals

5. **Weeks 17-20:** T13.G3.01 (Debugging) + Integration
   - Debugging strategies
   - Projects combining all pillars
   - Testing and iteration

6. **Weeks 21-36:** Application projects (early T14-T36)
   - Simple games
   - Interactive stories
   - Animations
   - Every project uses multiple pillars

### Grades 4-5: Integration (Paths 2, 3, 4, 5)

**Focus:** Combining constructs, data structures, functions
**Time:** Continuing to build on grade 3 foundation

**Sequence by semester:**

**Grade 4, Semester 1:**
- Deepen the pillars (T07.G4, T08.G4, T09.G4)
- Introduction to lists (T10.G4)
- Introduction to functions (T11.G4)
- Integrated projects

**Grade 4, Semester 2:**
- Combining pillars in projects
- List operations
- Custom blocks with parameters
- More complex games/apps

**Grade 5, Semester 1:**
- Advanced loops and conditionals (T07.G5, T08.G5)
- List algorithms (search, sort, filter)
- Functions with return values
- Systematic testing (T13.G5)

**Grade 5, Semester 2:**
- Data-driven projects
- Reusable function libraries
- Code organization and refactoring
- Complex applications

### Grades 6-8: Sophistication (All Paths)

**Focus:** Advanced concepts, real-world applications
**Time:** Project-based, integrating all paths

**Approach:**
- Teach advanced concepts through complex projects
- Every project should require:
  - Multiple programming constructs (Path 2)
  - Data structures (Path 3)
  - Functions and organization (Path 4)
  - Testing and debugging (Path 5)

**Example Grade 6 project:** "Build a quiz app"
- Events: Button clicks, quiz navigation
- Conditionals: Check answers, calculate score
- Variables: Track score, current question
- Lists: Questions and answers
- Functions: Check answer, load question, show score
- Testing: Test with different questions, edge cases

---

## Assessment Checkpoints

To ensure students are progressing along the critical paths, assess at these key checkpoints:

### Checkpoint 1: End of Grade 2

**Can the student:**
- [ ] Explain what an algorithm is
- [ ] Create simple step-by-step instructions
- [ ] Recognize patterns in sequences
- [ ] Trace a simple algorithm
- [ ] Break a simple task into steps

**If yes:** Ready for Grade 3 coding
**If no:** Additional unplugged support needed

### Checkpoint 2: Middle of Grade 3

**Can the student:**
- [ ] Create a program with an event (green flag or click)
- [ ] Explain what an event is
- [ ] Sequence blocks correctly
- [ ] Identify and fix simple sequencing errors

**If yes:** Ready for loops, conditionals, variables
**If no:** Additional T06 support needed - DO NOT ADVANCE

### Checkpoint 3: End of Grade 3

**Can the student:**
- [ ] Use loops to avoid repetitive code
- [ ] Use if/else to make decisions
- [ ] Use variables to store and update data
- [ ] Combine two of the above in a project
- [ ] Debug simple errors in their code

**If yes:** Ready for Grade 4 integration
**If no:** Additional practice with the three pillars needed

### Checkpoint 4: End of Grade 4

**Can the student:**
- [ ] Create and use lists
- [ ] Create custom blocks
- [ ] Iterate through a list with a loop
- [ ] Use conditionals to filter or search a list
- [ ] Test their code systematically

**If yes:** Ready for Grade 5 advanced topics
**If no:** Additional practice with data structures and functions

### Checkpoint 5: End of Grade 5

**Can the student:**
- [ ] Implement search or sort algorithms
- [ ] Create functions with parameters and return values
- [ ] Organize code with functions and comments
- [ ] Create test cases and test edge cases
- [ ] Complete a multi-day project combining all skills

**If yes:** Ready for Grades 6-8 sophisticated applications
**If no:** Additional integration practice needed

---

## Common Failure Modes and Remedies

### Failure Mode 1: "They saw it but didn't master it"

**Symptom:** Students were "exposed to" T06.G3.01 but can't create programs independently

**Cause:** Moved too fast, didn't ensure mastery

**Remedy:**
- Go back to T06.G3.01
- Extended practice with scaffolding gradually removed
- Require independent creation, not just modification
- Assess mastery before advancing

### Failure Mode 2: "They can do each separately but not together"

**Symptom:** Students can use loops OR conditionals OR variables, but not combinations

**Cause:** Taught topics in isolation, no integration practice

**Remedy:**
- Projects that require combinations
- Start with simple combinations (loop + variable)
- Progress to complex combinations (loop + conditional + variable)
- Scaffold: provide one part, student adds another

### Failure Mode 3: "They can code but can't debug"

**Symptom:** Students create code but can't fix errors

**Cause:** Testing/debugging was not integrated into learning

**Remedy:**
- Introduce T13.G3.01 immediately after first programming
- Every project includes debugging component
- Teach systematic debugging strategies
- Make debugging a normal, expected part of programming

### Failure Mode 4: "They hit a wall at lists"

**Symptom:** Students struggle with T10 (lists) even though they mastered T07-T09

**Cause:** Lists require integration of variables, loops, and conditionals

**Remedy:**
- Ensure T07, T08, T09 are solid (not just "passed")
- Start with simple lists (no conditionals)
- Add list iteration (lists + loops)
- Add list filtering (lists + loops + conditionals)
- Progress gradually

### Failure Mode 5: "They can follow tutorials but can't create"

**Symptom:** Students can follow step-by-step instructions but can't create their own programs

**Cause:** Too much scaffolding, not enough independent creation

**Remedy:**
- Gradual release of responsibility
- Start: Follow complete tutorial
- Next: Follow tutorial with gaps to fill in
- Next: Create program from description
- Finally: Create program from own idea
- Each step requires more independence

---

## Success Stories: Evidence of Path Mastery

### Student Who Mastered Path 1 (The Bridge)

**Grade 3, End of Year:**
- Creates programs from scratch without prompting
- Chooses appropriate events for tasks
- Explains why programs need events
- Excited to show what they made

**Evidence:** Independent creation, conceptual understanding, enthusiasm

### Student Who Mastered Path 2 (The Three Pillars)

**Grade 4, End of Year:**
- Combines loops, conditionals, and variables in projects
- Chooses the right construct for the problem
- Explains when to use each construct
- Debugs problems involving multiple constructs

**Evidence:** Appropriate tool selection, integration, debugging

### Student Who Mastered Path 3 (Data-Driven)

**Grade 5, End of Year:**
- Implements search and sort algorithms
- Uses lists to manage game inventories or datasets
- Iterates through lists with loops and filters with conditionals
- Explains when to use lists vs. variables

**Evidence:** Algorithm implementation, data structure selection

### Student Who Mastered Path 4 (Modular)

**Grade 6, End of Year:**
- Organizes large projects with functions
- Creates reusable function libraries
- Code is readable and maintainable
- Collaborates effectively on team projects

**Evidence:** Code organization, reusability, collaboration

### Student Who Mastered Path 5 (Quality)

**Grades 7-8:**
- Tests code systematically before claiming it's done
- Debugs problems efficiently
- Considers and handles edge cases
- Code is robust and reliable

**Evidence:** Testing practices, debugging efficiency, robustness

---

## Conclusion: The Interconnected Web

While we've described five "paths," the reality is more complex:

**Programming is an interconnected web of skills, not a linear sequence.**

The critical paths represent the **strongest threads** in that web - the progressions that, if mastered, enable everything else.

**The key insight:** Focus on the gateway skills, ensure path mastery at checkpoints, and integrate paths through projects.

**Do this, and students will become proficient programmers.**

---

## Quick Reference: Gateway Skills by Path

### Path 1: The Bridge
- T06.G3.01 ★★★★★ (Most critical skill in K-8 CS)

### Path 2: The Three Pillars
- T07.G3.01 ★★★★ (Loops)
- T08.G3.01 ★★★★ (Conditionals)
- T09.G3.01 ★★★★ (Variables)

### Path 3: Data-Driven
- T09.G4.01 ★★★ (User input)
- T10.G4.01 ★★★ (2D arrays/lists)

### Path 4: Modular
- T11.G4.01 ★★★ (Functions with return values)
- T11.G5.03 ★★★ (Design decisions)

### Path 5: Quality
- T13.G3.01 ★★★★ (First debugging)

**Stars indicate criticality (more stars = more critical)**

---

**End of Critical Paths Document**
