# T06 – Events & Sequencing in Programs: Dependency Analysis

## Age-Appropriateness Framework for This Topic

**K-2 (Ages 5-8)**: Concrete event recognition (green flag = start). Simple sequences. Physical button pressing.

**3-5 (Ages 8-11)**: Multiple event types, broadcasts. Understanding concurrency. Event-driven game loops.

**6-8 (Ages 11-14)**: Complex event architectures, state machines, event-driven design patterns. Professional event handling.

---

## Skill Review & Dependencies

### Grade K (PreK–K) - Ages 5-6

#### T06.GK.01 – Spot the green flag button
- **Size**: ✓ Appropriate (identifying program start)
- **Age-appropriateness**: ✓ **PERFECT** for K - big, visual, concrete button
- **Dependencies**: []
- **Notes**: **FOUNDATIONAL** - first programming concept; extremely concrete

#### T06.GK.02 – Put actions in order
- **Size**: ✓ Appropriate (sequencing 3-4 actions)
- **Age-appropriateness**: ✓ Excellent - drag-and-drop, visual
- **Dependencies**: [T01.GK.03, T06.GK.01]
  - T01.GK.03: Order picture story panels
- **Notes**: Sequencing in code context vs general algorithms
- **Overlap Check**: Very similar to T01.GK.03 but in programming context - acceptable

#### T06.GK.03 – Match code to a picture story
- **Size**: ✓ Appropriate (connecting code to behavior)
- **Age-appropriateness**: ✓ Good - visual matching task
- **Dependencies**: [T06.GK.02, T02.GK.01]
  - T02.GK.01: Identify sequence of pictures as algorithm
- **Notes**: Multiple representations

#### T06.GK.04 – What happens when you click go?
- **Size**: ✓ Appropriate (prediction from code)
- **Age-appropriateness**: ✓ Perfect - simple prediction
- **Dependencies**: [T06.GK.03, T01.GK.02]
  - T01.GK.02: Follow directions with sequence of steps
- **Notes**: Mental execution/tracing

---

### Grade 1 (Ages 6-7)

#### T06.G1.01 – Build a short script with green flag
- **Size**: ✓ Appropriate (first code creation!)
- **Age-appropriateness**: ✓ **EXCELLENT** for G1 - 3-4 blocks, concrete actions
- **Dependencies**: [T06.GK.01, T06.GK.02, T01.G1.01]
  - T01.G1.01: Write/draw steps for simple task
- **Notes**: **MILESTONE** - first actual coding!

#### T06.G1.02 – Trace code to find the result
- **Size**: ✓ Appropriate (reading code, predicting)
- **Age-appropriateness**: ✓ Good for G1 - 2-4 blocks only
- **Dependencies**: [T06.G1.01, T01.G1.02]
  - T01.G1.02: Trace and predict outcome of algorithm
- **Notes**: Code tracing vs algorithm tracing

#### T06.G1.03 – Find the order of blocks
- **Size**: ✓ Appropriate (identifying execution order)
- **Age-appropriateness**: ✓ Good - concrete numbering task
- **Dependencies**: [T06.G1.01, T06.GK.02]
- **Notes**: Understanding sequential execution

#### T06.G1.04 – Add a block to a script
- **Size**: ✓ Appropriate (editing existing code)
- **Age-appropriateness**: ✓ Perfect - guided construction
- **Dependencies**: [T06.G1.01, T06.G1.03]
- **Notes**: First code modification skill

---

### Grade 2 (Ages 7-8)

#### T06.G2.01 – Make a sprite respond to a key
- **Size**: ✓ Appropriate (key event introduction)
- **Age-appropriateness**: ✓ **EXCELLENT** - immediate feedback, game-like
- **Dependencies**: [T06.G1.01]
- **Notes**: **IMPORTANT** - first non-green-flag event; foundation for games

#### T06.G2.02 – Know the difference between events
- **Size**: ✓ Appropriate (distinguishing event types)
- **Age-appropriateness**: ✓ Good for G2 - concept understanding
- **Dependencies**: [T06.G2.01, T06.GK.01]
- **Notes**: Event timing and triggers

#### T06.G2.03 – Order actions in a key event
- **Size**: ✓ Appropriate (sequencing within event)
- **Age-appropriateness**: ✓ Good - combines events + sequencing
- **Dependencies**: [T06.G2.01, T06.G1.03]
- **Notes**: Sequences within different event contexts

#### T06.G2.04 – Assign controls to sprite movements
- **Size**: ✓ Appropriate (game controls setup)
- **Age-appropriateness**: ✓ **PERFECT** for G2 - game controls are motivating
- **Dependencies**: [T06.G2.01, T06.G2.03]
- **Notes**: Practical application; foundation for all game projects

---

### Grade 3 (Ages 8-9)

#### T06.G3.01 – Multiple scripts in one project
- **Size**: ✓ Appropriate (independent concurrent scripts)
- **Age-appropriateness**: ✓ Good for G3 - can understand parallel execution
- **Dependencies**: [T06.G2.04, T06.G2.02]
- **Notes**: Concurrency introduction

#### T06.G3.02 – Use broadcasts to trigger other scripts
- **Size**: ✓ Appropriate (broadcast/receive introduction)
- **Age-appropriateness**: ✓ Good for G3 - message-passing abstraction
- **Dependencies**: [T06.G3.01]
- **Notes**: **CRITICAL** for complex programs; script communication

#### T06.G3.03 – Multiple events running at the same time
- **Size**: ✓ Appropriate (understanding concurrency)
- **Age-appropriateness**: ✓ Good - interactive exploration
- **Dependencies**: [T06.G3.01, T06.G3.02]
- **Notes**: Concurrency and emergent behavior

#### T06.G3.04 – Find and fix event problems
- **Size**: ✓ Appropriate (debugging events)
- **Age-appropriateness**: ✓ Good for G3 - guided debugging
- **Dependencies**: [T06.G3.01, T06.G2.02, T13.G2.01]
  - T13.G2.01: Testing - find and fix simple errors
- **Notes**: Event-specific debugging
- **Grade-level check**: ✓ T13.G2.01 is G2

---

### Grade 4 (Ages 9-10)

#### T06.G4.01 – Sequence with delays and timing
- **Size**: ✓ Appropriate (wait blocks, timer events)
- **Age-appropriateness**: ✓ Good for G4 - temporal control
- **Dependencies**: [T06.G3.01, T06.G1.01]
- **Notes**: Time-based event programming

#### T06.G4.02 – Use loops inside event handlers
- **Size**: ✓ Appropriate (refactoring repeated event code)
- **Age-appropriateness**: ✓ Perfect - combines events + loops
- **Dependencies**: [T06.G2.01, T07.G3.02]
  - T07.G3.02: Forever loop for controls
- **Notes**: Integration of events and loops
- **Grade-level check**: ✓ T07.G3.02 is G3

#### T06.G4.03 – Events with conditional outcomes
- **Size**: ✓ Appropriate (conditionals in events)
- **Age-appropriateness**: ✓ Good - state-based responses
- **Dependencies**: [T06.G2.01, T08.G3.01]
  - T08.G3.01: If/else in game loop
- **Notes**: Events + conditionals integration
- **Grade-level check**: ✓ T08.G3.01 is G3

#### T06.G4.04 – Trace event sequences in complex projects
- **Size**: ✓ Appropriate (multi-event analysis)
- **Age-appropriateness**: ✓ Good for G4 - can follow complex flows
- **Dependencies**: [T06.G3.02, T06.G3.03, T02.G4.02]
  - T02.G4.02: Trace code with multiple if/else
- **Notes**: Complex event flow analysis
- **Grade-level check**: ✓ T02.G4.02 is G4

---

### Grade 5 (Ages 10-11)

#### T06.G5.01 – Structure a game with events
- **Size**: ✓ Appropriate (game architecture with events)
- **Age-appropriateness**: ✓ **EXCELLENT** for G5 - game design focus
- **Dependencies**: [T06.G4.03, T06.G3.02, T14.G4.01]
  - T14.G4.01: Game design basics
- **Notes**: Event-driven game architecture
- **Grade-level check**: ✓ T14.G4.01 is G4

#### T06.G5.02 – Many events happening together
- **Size**: ✓ Appropriate (concurrent event management)
- **Age-appropriateness**: ✓ Good - complex but manageable
- **Dependencies**: [T06.G3.03, T06.G5.01]
- **Notes**: Managing event complexity

#### T06.G5.03 – Send and receive broadcasts
- **Size**: ✓ Appropriate (modular broadcast design)
- **Age-appropriateness**: ✓ Perfect for G5 - decoupling concept
- **Dependencies**: [T06.G3.02, T06.G5.01]
- **Notes**: **IMPORTANT** - modular design through broadcasts

#### T06.G5.04 – Choreograph animations with events
- **Size**: ✓ Appropriate (synchronized multi-sprite animations)
- **Age-appropriateness**: ✓ Good - creative + technical
- **Dependencies**: [T06.G5.03, T06.G4.01, T15.G4.01]
  - T15.G4.01: Animation/story timing
- **Notes**: Broadcast-based synchronization
- **Grade-level check**: ✓ T15.G4.01 is G4

---

### Grade 6 (Ages 11-12)

#### T06.G6.01 – Trace event execution paths
- **Size**: ✓ Appropriate (complex event analysis)
- **Age-appropriateness**: ✓ Good for G6 - abstract reasoning
- **Dependencies**: [T06.G4.04, T06.G5.02, T02.G6.02]
  - T02.G6.02: Trace nested loops with variables
- **Notes**: Event dispatch and execution order
- **Grade-level check**: ✓ T02.G6.02 is G6

#### T06.G6.02 – Improve event script organization
- **Size**: ✓ Appropriate (refactoring events)
- **Age-appropriateness**: ✓ Good - code quality focus
- **Dependencies**: [T06.G5.01, T12.G5.01]
  - T12.G5.01: Code documentation
- **Notes**: Event organization and maintainability
- **Grade-level check**: ✓ T12.G5.01 is G5

#### T06.G6.03 – Create meaningful broadcast messages
- **Size**: ✓ Appropriate (broadcast naming/design)
- **Age-appropriateness**: ✓ Perfect for G6 - design thinking
- **Dependencies**: [T06.G5.03, T12.G5.01]
- **Notes**: Broadcasts as communication protocol

#### T06.G6.04 – Debug unexpected event behavior
- **Size**: ✓ Appropriate (subtle event bugs)
- **Age-appropriateness**: ✓ Good - complex debugging
- **Dependencies**: [T06.G3.04, T06.G6.01, T13.G5.02]
  - T13.G5.02: Test with edge cases
- **Notes**: Advanced event debugging
- **Grade-level check**: ✓ T13.G5.02 is G5

---

### Grade 7 (Ages 12-13)

#### T06.G7.01 – Use events to manage game states
- **Size**: ✓ Appropriate (state machine design)
- **Age-appropriateness**: ✓ **EXCELLENT** for G7 - architectural thinking
- **Dependencies**: [T06.G5.01, T14.G6.01]
  - T14.G6.01: Game state management
- **Notes**: **CRITICAL** - state machine pattern
- **Grade-level check**: ✓ T14.G6.01 is G6

#### T06.G7.02 – Decouple systems with broadcasts
- **Size**: ✓ Appropriate (loose coupling architecture)
- **Age-appropriateness**: ✓ Good for G7 - advanced design pattern
- **Dependencies**: [T06.G5.03, T06.G6.03, T12.G6.02]
  - T12.G6.02: Refactor for clarity
- **Notes**: Professional software architecture
- **Grade-level check**: ✓ T12.G6.02 is G6

#### T06.G7.03 – Analyze event priorities and timing
- **Size**: ✓ Appropriate (event ordering analysis)
- **Age-appropriateness**: ✓ Good - reasoning about execution
- **Dependencies**: [T06.G6.01, T06.G7.01]
- **Notes**: Event system optimization

#### T06.G7.04 – Multi-stage event sequences
- **Size**: ✓ Appropriate (complex event chains)
- **Age-appropriateness**: ✓ Good for G7 - can handle complexity
- **Dependencies**: [T06.G7.01, T06.G5.03]
- **Notes**: Conditional event cascades

---

### Grade 8 (Ages 13-14)

#### T06.G8.01 – Coordinate events across players
- **Size**: ✓ Appropriate (multiplayer event handling)
- **Age-appropriateness**: ✓ **PERFECT** for G8 - networked thinking
- **Dependencies**: [T06.G7.02, T19.G7.01]
  - T19.G7.01: Multiplayer synchronization
- **Notes**: Race conditions, synchronization
- **Grade-level check**: ✓ T19.G7.01 is G7

#### T06.G8.02 – Create reusable event-handling patterns
- **Size**: ✓ Appropriate (abstraction of event logic)
- **Age-appropriateness**: ✓ Good - design patterns
- **Dependencies**: [T06.G7.02, T11.G7.01]
  - T11.G7.01: Advanced custom blocks
- **Notes**: Event handler abstraction
- **Grade-level check**: ✓ T11.G7.01 is G7

#### T06.G8.03 – Evaluate event system design
- **Size**: ✓ Appropriate (architecture review)
- **Age-appropriateness**: ✓ Good for G8 - meta-analysis
- **Dependencies**: [T06.G7.03, T06.G7.02, T12.G7.02]
  - T12.G7.02: Advanced organization
- **Notes**: Event architecture optimization
- **Grade-level check**: ✓ T12.G7.02 is G7

#### T06.G8.04 – Explain event design decisions
- **Size**: ✓ Appropriate (design justification)
- **Age-appropriateness**: ✓ Perfect - articulating trade-offs
- **Dependencies**: [T06.G8.03, T01.G7.02]
  - T01.G7.02: Choose right algorithm for task
- **Notes**: Event architecture reasoning
- **Grade-level check**: ✓ T01.G7.02 is G7

---

## Summary

**Total Skills**: 36 (4 per grade K-8)
**Granularity**: ✓ All appropriately sized
**Age-Appropriateness**: ✓ **EXCELLENT** progression

**Issues Found**: None - all dependencies properly ordered

**Key Observations**:

1. **Foundational Topic**: T06 is the **ENTRY POINT** for all coding
   - T06.G1.01 is first actual code writing
   - Almost all other programming topics depend on T06

2. **Progression Quality**: Excellent K-8 ladder
   - K: Recognize program start (green flag)
   - 1: Write first scripts
   - 2: Multiple event types (keys)
   - 3: Broadcasts, concurrency
   - 4-5: Integration with loops/conditionals, game architecture
   - 6-8: State machines, professional event architectures

3. **Age-Appropriateness Highlights**:
   - K-2: Very concrete (buttons, visible events)
   - 3-5: Game controls highly motivating
   - 6-8: Abstract architectural thinking

4. **No Overlap Issues**: Unlike T04, this topic is distinct and essential

**Cross-Topic Dependencies**:
- **From T01**: Algorithm concepts feed into event sequencing
- **From T02**: Representation/tracing used for event analysis
- **To T07**: Events trigger loops
- **To T08**: Events contain conditionals
- **To T09-T10**: Events manipulate variables/lists
- **To T11**: Events use custom blocks
- **To T12**: Event organization is program organization
- **To T13**: Event debugging
- **To T14-T24**: ALL applications use events
- **To T19**: Multiplayer events

**Dependency Pattern**: T06 is heavily depended upon, has minimal dependencies
- Only depends on: T01 (algorithms), T02 (tracing), T13 (testing)
- Depended on by: Almost every other topic

**Recommendation**: **NO CHANGES NEEDED** - This is a well-designed foundational topic.

**Special Note**: T06 skills should be considered **prerequisites for most programming skills** in other topics, starting from G1.
