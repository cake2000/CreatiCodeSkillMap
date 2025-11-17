# Subagent Task: Analyze Dependencies for T14-T24 (Applications Domain)

## Context
You are analyzing 346 skills across 11 application topics (T14-T24) to identify skill dependencies for a K-8 coding skill map.

## Input Files
- `skills_T14_T24_extracted.json` - All 346 skills for T14-T24
- `dependencies_T01_T05.json` - Dependencies for Algorithms & Design topics
- `dependencies_T06_T13.json` - Dependencies for Programming Core topics (includes 21 gateway skills)

## Topics to Analyze (346 skills total)
- **T14** (32 skills): 2D Games & Interactive Simulations
- **T15** (32 skills): Stories, Animation & Digital Media
- **T16** (32 skills): User Interfaces & Widgets
- **T17** (32 skills): Physics-Based Motion & Simulation
- **T18** (32 skills): 3D Worlds & Games
- **T19** (31 skills): Multiplayer & Connected Apps
- **T20** (32 skills): Algorithmic Art & Creative Coding
- **T21** (32 skills): AI Media Tools & Creative Assets
- **T22** (31 skills): AI Chatbots & Information Apps
- **T23** (32 skills): AI Voice, Vision & Gesture Interfaces
- **T24** (28 skills): XO & AI-Supported Coding Practices

## Your Task
For EACH of the 346 skills, identify dependencies in this priority order:

### 1. Dependencies on T06-T13 (Programming Core) - MOST IMPORTANT
These are the fundamental programming skills that application skills build upon:
- **T06** (Events): Click handlers, keyboard input, sprite events
- **T07** (Loops): Repeat, forever, for loops, animation loops
- **T08** (Conditionals): If/then, if/else, boolean logic, collision detection
- **T09** (Variables): Position tracking, score, state, game data
- **T10** (Lists & Tables): Player data, inventory, dialogue arrays
- **T11** (Functions): Custom blocks, reusable behaviors, game logic modules
- **T12** (Program Organization): Multi-scene projects, code structure
- **T13** (Testing): Debugging games, edge cases

### 2. Dependencies on T01-T05 (Algorithms & Design)
Design thinking foundations:
- **T01** (Algorithms): Planning game logic, optimization
- **T02** (Representing/Tracing): Flowcharts, pseudocode
- **T03** (Decomposition): Breaking down game features
- **T04** (Patterns): Recognizing reusable behaviors
- **T05** (Human-Centered Design): UX, accessibility, user testing

### 3. Within-Topic Dependencies (Same Topic)
- Basic skills → Intermediate → Advanced within same topic
- Example: T14.G3 basic movement → T14.G5 advanced collision

### 4. Cross-Application Dependencies (T14-T24)
- Shared concepts across application topics
- Example: T14 (2D games) → T18 (3D games)
- Example: T16 (UI widgets) → T22 (Chatbot interfaces)

## Critical Dependency Patterns by Topic

### T14 (2D Games)
- Movement: T06 (events), T07 (loops), T09 (variables for x/y)
- Collision: T08 (conditionals), T09 (variables)
- Scoring: T09 (variables), T08 (conditionals)
- Game states: T08 (conditionals), T11 (functions)
- Multiple levels: T12 (organization), T10 (lists)

### T15 (Stories/Animation)
- Scene control: T06 (events), T12 (multi-scene)
- Animation: T07 (loops), T09 (variables)
- Branching narrative: T08 (conditionals)
- Dialogue: T09 (variables), T10 (lists)
- Character behaviors: T11 (functions)

### T16 (UI/Widgets)
- Interactive elements: T06 (events)
- Input handling: T09 (variables), T08 (validation)
- Forms/menus: T10 (lists), T08 (conditionals)
- Widget libraries: T11 (functions), T12 (organization)

### T17 (Physics)
- Motion simulation: T07 (loops), T09 (velocity/acceleration)
- Gravity/forces: T08 (conditionals), T09 (variables)
- Collisions: T08 (conditionals), T09 (position)
- Often builds on: T14 (2D games)

### T18 (3D Worlds)
- 3D movement: T06 (events), T09 (x/y/z coords)
- Camera control: T09 (variables), T08 (conditionals)
- 3D collision: T08 (conditionals)
- Builds on: T14 (2D game patterns in 3D)

### T19 (Multiplayer)
- Player data: T10 (lists), T09 (variables)
- Sync logic: T08 (conditionals), T11 (functions)
- Turn-based: T08 (game logic), T09 (state)
- Builds on: T14 (games), T18 (3D games)

### T20 (Algorithmic Art)
- Pattern generation: T07 (nested loops), T09 (parameters)
- Generative systems: T04 (patterns), T11 (functions)
- Parametric design: T09 (variables), T07 (loops)

### T21 (AI Media)
- AI API calls: T06 (events), T09 (variables for responses)
- Asset generation: T10 (lists), T08 (conditionals)
- Integration: T15 (media), T16 (UI)

### T22 (AI Chatbots)
- Conversation flow: T08 (conditionals), T10 (dialogue lists)
- User input: T06 (events), T09 (variables)
- Context tracking: T09 (variables), T10 (lists)
- UI: T16 (widgets)
- Ethics: T05 (HCD)

### T23 (AI Voice/Vision/Gesture)
- Sensor input: T06 (events), T09 (variables)
- Recognition logic: T08 (conditionals), T10 (lists)
- Interaction: T16 (UI), T06 (events)
- Ethics: T05 (HCD)

### T24 (XO AI Practices)
- Meta-level: Uses skills from many other topics
- Planning: T03 (decomposition), T02 (planning)
- Code generation: T01 (algorithms), T11 (functions)
- Debugging: T13 (testing)
- Ethics: T05 (HCD)

## Output Format
Create JSON file `dependencies_T14_T24.json` with this structure:

```json
[
  {
    "id": "T14.G3.01",
    "dependencies": ["T14.G2.01", "T14.G1.01"],
    "cross_domain_dependencies": [
      "T06.G3.01",  // Events - click to start
      "T07.G3.01",  // Loops - movement
      "T09.G3.01"   // Variables - position
    ],
    "notes": "Basic 2D game movement requires events, loops, and variables",
    "grade_level_ok": true,
    "quality_issues": [],
    "gateway_skill": false,
    "dependency_count": 5,
    "capstone_skill": false
  }
]
```

## Field Definitions
- **id**: Skill ID (e.g., "T14.G3.01")
- **dependencies**: Within-topic prerequisites (same Txx)
- **cross_domain_dependencies**: Skills from other topics (T01-T13, T14-T24)
- **notes**: Brief explanation of why these dependencies exist
- **grade_level_ok**: true unless dependencies are from higher grades
- **quality_issues**: Array of concerns (e.g., ["Missing T08 for collision logic"])
- **gateway_skill**: true if this is a critical foundational skill (rare in applications)
- **dependency_count**: Total dependencies (within + cross-domain)
- **capstone_skill**: true if integrates 5+ prerequisites from 3+ topics

## Special Analysis Requirements

### 1. Identify Capstone Skills
Skills that integrate 5+ prerequisites from 3+ different topics. These are excellent assessment opportunities.

Example capstone:
- T14.G7.01 "Create complete multi-level game" might require:
  - T06.G6.01 (events)
  - T07.G6.01 (loops)
  - T08.G6.01 (conditionals)
  - T09.G6.01 (variables)
  - T10.G6.01 (lists)
  - T11.G6.01 (functions)
  - T12.G6.01 (organization)

### 2. Grade Level Validation
- Check that cross_domain_dependencies are from SAME or LOWER grade
- Flag any violations in quality_issues
- Example: T14.G4.01 should NOT depend on T06.G5.01

### 3. Gateway Skills (Rare in Applications)
- Most gateway skills are in T06-T13
- Applications might have a few gateways (e.g., first complete game)
- Mark as gateway_skill: true only if truly foundational for other application skills

### 4. Cross-Application Patterns
Track common patterns across topics:
- Game patterns (T14, T17, T18, T19)
- Media patterns (T15, T21)
- Interface patterns (T16, T22, T23)
- AI patterns (T21, T22, T23, T24)

## Quality Checks
For each skill, verify:
1. Are dependencies appropriate for grade level?
2. Are there obvious missing dependencies? (e.g., game scoring without variables)
3. Is progression smooth within topic?
4. Are cross-topic synergies identified?
5. Any orphan skills with no clear prerequisites?

## Workflow
1. Read `skills_T14_T24_extracted.json`
2. Read `dependencies_T06_T13.json` to understand gateway skills
3. For each topic T14-T24:
   - Analyze all skills in grade order (G1 → G8)
   - Identify within-topic dependencies
   - Map to T06-T13 programming core skills
   - Map to T01-T05 design skills where relevant
   - Map to other T14-T24 skills where relevant
4. Generate `dependencies_T14_T24.json`
5. Generate analysis reports (see below)

## Required Outputs

### 1. dependencies_T14_T24.json
Complete dependency records for all 346 skills

### 2. DEPENDENCIES_T14_T24_REPORT.md
Topic-by-topic analysis:
- Skill count and grade distribution
- Key dependency patterns
- Heavily used T06-T13 gateway skills
- Within-topic progression
- Quality issues found

### 3. DEPENDENCIES_T14_T24_SUMMARY.md
Executive summary:
- Total skills analyzed
- Dependency statistics (avg dependencies per skill, etc.)
- Gateway skills identified
- Capstone skills identified
- Quality issues summary
- Recommendations

### 4. CAPSTONE_SKILLS_T14_T24.md
List of high-integration skills:
- Skills with 5+ prerequisites from 3+ topics
- Grade distribution of capstones
- Assessment recommendations

### 5. CROSS_APPLICATION_PATTERNS.md
Common patterns across T14-T24:
- Shared game mechanics (T14, T17, T18, T19)
- Media/animation patterns (T15, T21)
- Interface patterns (T16, T22, T23)
- AI integration patterns (T21, T22, T23, T24)
- Recommendations for teaching sequences

## Success Criteria
- All 346 skills have dependency analysis
- Grade level conflicts identified and flagged
- No orphan skills (all have clear learning pathway)
- Capstone skills identified for assessment
- Cross-application patterns documented
- Recommendations for curriculum design

## Important Notes
- Print plain text progress, NOT objects (don't use console.log with objects)
- Focus on T06-T13 dependencies first - these are most critical
- Application skills should have HEAVY dependencies on programming core
- Not every skill needs T01-T05 dependencies (only where design thinking applies)
- Be specific in notes about WHY dependencies exist
- Flag any suspicious patterns (e.g., advanced skill with no prerequisites)
