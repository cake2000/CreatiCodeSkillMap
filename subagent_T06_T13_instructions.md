# Subagent Task: Analyze Dependencies for T06-T13 Programming Core Skills

## Context
You are analyzing 265 skills across 8 programming core topics (T06-T13) to add dependency mappings for a K-8 coding skill map.

## Input Files
- `/tmp/skills_T06_T13.json` - 265 skills from topics T06-T13
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/dependencies_T01_T05.json` - Completed dependency mappings for foundational topics

## Topics to Analyze (in order)
1. **T06: Events & Sequencing in Programs** (~30 skills)
2. **T07: Loops & Repetition** (~35 skills)
3. **T08: Conditionals & Logic** (~35 skills)
4. **T09: Variables & Expressions** (~35 skills)
5. **T10: Lists, Tables & Structured Data** (~30 skills)
6. **T11: Functions & Modularization** (~35 skills)
7. **T12: Program Organization, Style & Readability** (~30 skills)
8. **T13: Testing, Debugging & Error Handling** (~35 skills)

## Critical Dependency Patterns to Apply

### T06 (Events) - FOUNDATION FOR ALL PROGRAMMING
- G1 skills: No dependencies (foundational)
- G2 skills: Depend on G1 events + T01.G2 (algorithms)
- G3+ skills: Events are the GATEWAY to actual coding - most other programming topics will depend on appropriate-grade T06 skills
- **Key principle**: You can't code without understanding event-driven execution

### T07 (Loops)
- All loop skills depend on T06 (events) at same or lower grade
- Depend on T04 (pattern recognition) - recognizing repetition
- Depend on T01 (repetition in algorithms)
- Nested loops depend on basic loops
- Loop iteration with lists depends on T10 (lists)

### T08 (Conditionals)
- All conditional skills depend on T06 (events) at same or lower grade
- Depend on T01 (if/then thinking)
- Complex conditionals (nested, multiple conditions) depend on basic conditionals
- Logical operators (AND/OR/NOT) are higher-level dependencies

### T09 (Variables)
- All variable skills depend on T06 (events) at same or lower grade
- Used BY many other topics (loops, conditionals, functions, lists)
- Variable scope depends on understanding functions (T11)
- Expressions depend on basic variables

### T10 (Lists)
- All list skills depend on T09 (variables) - lists are variable containers
- List iteration depends on T07 (loops)
- List operations depend on T06 (events)
- 2D arrays/tables depend on 1D lists

### T11 (Functions)
- All function skills depend on T06 (events) at same or lower grade
- Depend on T03 (decomposition) - breaking problems into reusable parts
- Parameters depend on T09 (variables)
- Return values are higher-level than basic functions
- Recursion is advanced (grade 7-8)

### T12 (Program Organization)
- Depends on T03 (decomposition)
- Depends on T11 (functions) for modular organization
- Comments and naming are foundational
- Code style depends on having written code (T06+)

### T13 (Testing)
- Depends on T02 (tracing) - fundamental to debugging
- Can work with ANY programming construct (events, loops, conditionals, etc.)
- Test planning depends on T03 (decomposition)
- Debugging strategies are grade-progressive

## Quality Checks for Each Skill

1. **Within-topic progression**: Does each skill build logically on earlier skills in the same topic?
2. **Cross-topic dependencies**: Are dependencies on other T06-T13 topics identified?
3. **Foundation dependencies**: Are dependencies on T01-T05 identified?
4. **Grade consistency**: Can a student at grade N reasonably do this with dependencies from grade N or below?
5. **Gateway skills**: Is this a skill that many other skills will depend on?
6. **Redundancy**: Is this skill too similar to another skill?
7. **Scope**: Is this skill too broad (should be split) or too narrow?

## Output Format

Create a JSON file with this structure for EACH of the 265 skills:

```json
[
  {
    "id": "T06.G1.01",
    "dependencies": [],
    "cross_domain_dependencies": [],
    "notes": "Foundational - first exposure to event-driven programming",
    "grade_level_ok": true,
    "quality_issues": [],
    "gateway_skill": true,
    "related_skills": ["T01.G1.01"]
  },
  {
    "id": "T06.G3.02",
    "dependencies": ["T06.G3.01"],
    "cross_domain_dependencies": ["T07.G3.01", "T01.G3.01"],
    "notes": "Combines events with loops - requires understanding both concepts",
    "grade_level_ok": true,
    "quality_issues": [],
    "gateway_skill": false,
    "related_skills": ["T07.G3.01", "T08.G3.01"]
  }
]
```

## Process

1. Read both input files
2. For T06-T13 in order:
   a. Analyze all skills in the topic by grade (1-8)
   b. Identify within-topic dependencies
   c. Identify cross-topic dependencies (within T06-T13 and to T01-T05)
   d. Check grade-level consistency
   e. Flag quality issues
   f. Identify gateway skills (skills many others depend on)
3. Output `/media/binyu/USB2/dev/CreatiCodeSkillMap/dependencies_T06_T13.json`
4. Create comprehensive report

## Key Metrics to Track
- Total skills analyzed: 265
- Gateway skills identified (critical dependencies)
- Quality issues found
- Cross-topic dependency density
- Grade progression smoothness

## Notes
- Print progress as plain text (no objects)
- Focus on accuracy over speed
- Gateway skills in T06 are especially critical
- Grade 3 skills bridge unplugged (1-2) to coding - check carefully
- Be conservative with dependencies - only add if truly necessary
