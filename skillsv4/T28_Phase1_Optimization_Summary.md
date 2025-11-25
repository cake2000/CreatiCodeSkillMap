# T28 (Chance & Simulations) Phase 1 Optimization Summary

## Overview
Completed comprehensive optimization of Topic T28 (Chance & Simulations) covering Grades 2-8 with 54 skills.

## Key Changes Made

### 1. Topic Name Standardization
- Changed all topic labels from "T28 – Chance & Simulations: G2–8 Skill List" to simply "T28 – Chance & Simulations" for consistency.

### 2. Dependency Cleanup (Major)

**Removed 50+ irrelevant dependencies**, particularly in Grade 4 skills that had excessive dependencies to unrelated topics:
- T28.G4.01 reduced from 13 dependencies to 2 relevant ones
- T28.G4.02.01 reduced from 10 dependencies to 3 relevant ones
- T28.G4.02.02 reduced from 9 dependencies to 3 relevant ones

**Removed dependencies that violated topic relevance:**
- T02.G2.01, T02.G2.02 (box diagrams - not directly relevant)
- T04.G2.01, T04.G2.02, T04.G2.03, T04.G3.02 (pattern recognition - only indirectly relevant)
- T05.G3.01, T05.G3.02, T05.G5.03, T05.G5.04 (human-centered design - not relevant)
- T06.G2.01, T06.G2.02, T06.G2.03 (basic events - too elementary)
- T07.G2.01 (repeat vs do once - too elementary for G4+ skills)

**Added missing intra-topic dependencies:**
- T28.G2.02 now depends on T28.G2.01 (proper sequence)
- T28.G2.03 now depends on T28.G2.02 (builds on chance experiments)
- T28.G3.01 now depends on T28.G2.04 (connects to predictions)
- T28.G3.05 now depends on T28.G3.04 (proper progression)
- Many more logical progressions established

### 3. Skill Description Improvements

**Grade 2 (Picture-Based):**
- T28.G2.01: Added clear definitions of certain/possible/impossible with specific examples
- T28.G2.02: Clarified physical materials (pencil/paperclip spinner) and process
- T28.G2.03: Added specific examples of equal vs uneven spinner slices
- T28.G2.04: Made coin flip activity more concrete with tracking correct/incorrect guesses

**Grade 3 (Transition to Coding):**
- T28.G3.02: Renamed from vague "explain what pick random does" to "Explore the 'pick random' operator block" with specific test questions
- T28.G3.03: Made more concrete with exact script description students will use
- T28.G3.04: Added specific prediction format and calculation
- T28.G3.05: Simplified from overly broad "describe randomness AND simulate AND explain" to focused "Identify random elements in familiar games"
- T28.G3.06: Added specific starter script students receive
- T28.G3.07: Step-by-step instructions for building from scratch

**Grade 4 (Core Simulation Skills):**
- T28.G4.01: Clearer example (1=red, 2=blue mapping)
- T28.G4.02.01-03: Clearer algorithm steps for logging, counting, percentages
- T28.G4.03: Added concrete example numbers (50 vs 500 trials comparison)
- T28.G4.04: Specific bug examples (duplicate entries, wrong range)
- T28.G4.05: Exact coordinate ranges and visual expectation
- T28.G4.06: Concrete probability examples with conversions
- T28.G4.07: Algorithm for random-without-replacement

**Grade 5 (Probability Theory):**
- T28.G5.01.01: Exact script for two-dice simulation
- T28.G5.01.02: Explained why 7 is most common (6 combinations)
- T28.G5.02: A/B test scenario with verification
- T28.G5.03: Monte Carlo estimation of π as engaging example
- T28.G5.04: 5-part planning template
- T28.G5.05: P(event) formula with worked examples
- T28.G5.06: Specific comparison questions
- T28.G5.08: "Random walker" sprite with energy mechanic
- T28.G5.09: Expected value formula with worked examples
- T28.G5.10: Gambler's fallacy with coin flip streak example
- T28.G5.11: Law of large numbers with specific trial counts

**Grade 6 (Advanced Simulations):**
- T28.G6.01.01: Concrete game balance testing example
- T28.G6.01.02: Nested loop output format
- T28.G6.02: Exact CreatiCode block syntax for seeded random
- T28.G6.03: Percent error formula with thresholds
- T28.G6.04: Synthetic sensor data generation example
- T28.G6.05: Grid coordinate system details (mod 4 for direction)
- T28.G6.06: Marble drawing without replacement example
- T28.G6.07: Walls list data structure
- T28.G6.08: Scoring system (+10 goal, -1 step, -5 wall)
- T28.G6.09: Cat/mouse chase dynamics
- T28.G6.10: Three sampling methods with comparison questions
- T28.G6.11: Conditional probability notation P(A|B)

**Grade 7 (Multi-Agent & Fairness):**
- T28.G7.01: Predator-prey with energy/hunger mechanics
- T28.G7.02: Learning agent preference table explanation
- T28.G7.03: Fairness testing with synthetic player profiles
- T28.G7.04: Permutation test with worked example
- T28.G7.05: Model card template with 4 required sections
- T28.G7.06.01: Clone-based multi-agent with state lists
- T28.G7.06.02: Population-level metrics dashboard
- T28.G7.07: Historical examples (1970 draft lottery)

**Grade 8 (Professional Practices):**
- T28.G8.01: End-to-end pipeline with table structure
- T28.G8.02: Bootstrap sampling with confidence intervals
- T28.G8.03: AI integration with critical evaluation
- T28.G8.04: Policy brief template with ethics section
- T28.G8.05: Environment bias analysis connecting to AI training
- T28.G8.06: Pseudorandom deep dive with real-world applications

### 4. CreatiCode Block Alignment

Added specific references to CreatiCode blocks:
- `pick random 1 to 6` - standard random operator
- `set [list] to (N) random numbers with seed (SEED)` - seeded random for reproducibility
- Clone creation for multi-agent simulations
- List operations for data logging

### 5. Cross-Topic Dependencies Preserved

All dependencies to other topics (T01, T03, T06, T07, T08, T09, T10, T11, T13, T22, T27, T35) were preserved or updated to more appropriate skills within those topics.

## Skill Count
- **Total T28 skills:** 54 (unchanged)
- **Grade 2:** 4 skills
- **Grade 3:** 7 skills
- **Grade 4:** 7 skills
- **Grade 5:** 11 skills
- **Grade 6:** 11 skills
- **Grade 7:** 8 skills (including 7.06.01 and 7.06.02)
- **Grade 8:** 6 skills

## Progression Summary

```
G2: Physical activities (spinners, coins, marbles)
  ↓
G3: Transition to digital (observe → modify → build simple random generators)
  ↓
G4: Data collection (logging, counting, percentages, variability)
  ↓
G5: Probability theory (theoretical vs experimental, expected value, independence)
  ↓
G6: Advanced simulations (parameters, seeds, grid agents, conditional probability)
  ↓
G7: Multi-agent systems (interactions, learning, fairness testing)
  ↓
G8: Professional practices (pipelines, policy briefs, AI integration)
```

## Quality Improvements

1. **Actionable descriptions:** Each skill now has concrete steps or algorithms
2. **Assessable outcomes:** Clear success criteria for each skill
3. **Grade-appropriate complexity:** K-2 unplugged, G3+ block-based
4. **Proper scaffolding:** Each skill builds logically on prerequisites
5. **Real-world connections:** Examples relevant to student interests
6. **CreatiCode alignment:** Skills reference actual platform capabilities

## Files Modified
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` (lines 25457-26040)

## Backup Created
- `allskills_backup_before_T28_phase1_*.md`
