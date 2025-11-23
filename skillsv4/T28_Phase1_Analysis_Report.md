# T28 (Chance & Simulations) Phase 1 Analysis Report

## CreatiCode Block Capabilities for T28

### Random Number Generation
1. **Basic Random**: Standard Scratch "pick random X to Y" block (standard operator, assumed available)
2. **Random Lists**:
   - `set [list] to (N) random whole numbers between (MIN) and (MAX) [allow/no repetition]`
   - `set [list] to (N) random numbers with seed (SEED)` - generates random numbers 0-1 with seed
3. **Shuffle**: `reshuffle [list] randomly`
4. **Random Selection**: Select N items from list (largest/smallest/random)
5. **Noise Function**: `noise at x (X) y (Y) seed (SEED)` - for terrain generation

### Variables & Lists
- Full variable support (create, set, modify, display)
- List operations (add, remove, insert, replace, length, contains)
- Variable monitors for display

### Control Flow
- Counted loops (repeat N)
- Conditional loops (repeat until)
- If/if-else statements
- Cloning with custom IDs

### Data Visualization
- Bar charts (single and side-by-side)
- Display variables on stage
- Table operations (sort, filter, aggregate)

### Advanced Features
- Broadcasting for sprite communication
- Collision detection
- Coordinate-based positioning
- Custom functions (though not explicitly documented)

### Limitations
- No explicit "seed random number generator" block for standard random (only for list generation)
- Statistical analysis must be coded manually (no built-in mean/median/mode for operators, but available for tables)
- No explicit probability distribution blocks

---

## HIGH PRIORITY ISSUES

### H1: Forward Reference within T28
**Issue**: T28.G3.05 depends on T28.G3.06, but G3.05 comes before G3.06
- **Skill**: T28.G3.05 "Describe randomness in games and simulate a simple game element"
- **Problem**: Depends on T28.G3.06 which comes after it
- **Fix**: Either swap the order of G3.05 and G3.06, OR remove T28.G3.06 from G3.05's dependencies and have it only depend on T28.G3.01

**Recommendation**: Remove T28.G3.06 from T28.G3.05 dependencies. G3.05 can be done after interpreting simulations (G3.01) alone.

### H2: Duplicate/Overlapping Skills - "Build a random generator"
**Issue**: Three skills essentially do the same thing:
- **T28.G3.07**: "Assemble blocks to build a random generator" - build from scratch, 2-3 outcomes, use 'say' block
- **T28.G4.01**: "Build a simple random generator" - uses 'pick random 1-4' with if-statements for 4 colors
- Both create a random generator with 'say' output and green flag script

**Problem**: These are functionally identical - both build random generators from scratch with multiple outcomes
**Fix**: Merge or clarify distinction. G4.01 adds if-statements which is the only difference.

**Recommendation**:
- Keep T28.G3.07 as simple generator (2-3 outcomes, direct 'say')
- Modify T28.G4.01 description to emphasize it's about using if-statements with random numbers, making this an application of conditionals rather than just "building a random generator"

### H3: Unclear Skill - "Track position and state for a single sprite"
**Issue**: T28.G5.08 "Track position and state for a single sprite"
- **Problem**: This skill seems misplaced in a Chance & Simulations topic. It's about sprite state management, not randomness or probability.
- **Current Description**: "create a sprite that maintains its position using x,y coordinate variables and tracks one additional state variable"
- **Context**: Used as prerequisite for G6.05 (grid world agent)

**Fix**: Either move this to a different topic (likely T05 Modeling & Sim or T09 Variables), OR reframe it specifically for probabilistic simulations

**Recommendation**: Move to T05 or T09. If kept in T28, rename to "Track agent state for probabilistic simulation" and emphasize the random/probabilistic aspects.

### H4: X-2 Rule Violations

#### H4a: T28.G3.01 (Grade 3) depends on T07.G3.01 (same grade)
- **Skill**: T28.G3.01 "Interpret provided simulation output"
- **Dependency**: T07.G3.01 "Use a counted repeat loop"
- **Problem**: Same grade dependency (X-2 rule requires X-2)
- **Fix**: Change dependency to T07.G1.01 "Follow repeat blocks in picture sequences" or accept that G3 students need prior G3 loop knowledge

#### H4b: T28.G4.01 depends on T08.G3.01 (X-1 violation)
- **Skill**: T28.G4.01 "Build a simple random generator" (Grade 4)
- **Dependency**: T08.G3.01 "Use a simple if in a script" (Grade 3)
- **Problem**: Only 1 grade apart (X-2 rule requires 2)
- **Fix**: Move T28.G4.01 to G5 OR change to depend on T08.G2.01 if it exists, OR accept X-1 for conditionals

#### H4c: T28.G4.02.01 depends on T07.G3.01 (X-1 violation)
- **Skill**: T28.G4.02.01 "Log trial results to a list" (Grade 4)
- **Dependency**: T07.G3.01 "Use a counted repeat loop" (Grade 3)
- **Problem**: Only 1 grade apart
- **Fix**: Accept this or change to T07.G2.01 if it exists

#### H4d: T28.G5.03 depends on T08.G4.01 (X-1 violation)
- **Skill**: T28.G5.03 "Use Monte Carlo sampling" (Grade 5)
- **Dependency**: T08.G4.01 "Choose actions based on user input or sensor values" (Grade 4)
- **Problem**: Only 1 grade apart
- **Fix**: Move to G6 OR find G3 conditional dependency

#### H4e: T28.G6.05 depends on T08.G5.01 (X-1 violation)
- **Skill**: T28.G6.05 "Model a simple agent in a grid world" (Grade 6)
- **Dependency**: T08.G5.01 "Use a simple if in a script" (Grade 5)
- **Problem**: Only 1 grade apart, and T08.G5.01 seems like a duplicate of T08.G3.01
- **Fix**: Likely T08.G5.01 is an error - should be T08.G3.01

#### H4f: T28.G6.07 depends on T08.G5.01 (X-1 violation)
- Same issue as H4e

#### H4g: T28.G7.01 depends on T28.G6.08 and T28.G6.09 (X-1 violations)
- **Skill**: T28.G7.01 "Create a two-agent interaction simulation" (Grade 7)
- **Dependencies**: T28.G6.08, T28.G6.09 (both Grade 6)
- **Problem**: Only 1 grade apart within T28
- **Fix**: Accept these as closely related scaffolding OR move G7.01 to G8

### H5: Missing T08.G5.01 Investigation
**Issue**: T08.G5.01 "Use a simple if in a script" is referenced but seems like a duplicate of T08.G3.01
- **Problem**: This appears to be a data error - conditionals are introduced in G3, not G5
- **Skills affected**: T28.G6.05, T28.G6.07
- **Fix**: Change these dependencies to T08.G3.01 or T08.G4.01

---

## MEDIUM PRIORITY ISSUES

### M1: Grade Appropriateness - G2 Skills Need Physical Component
**Issue**: G2 skills are supposed to be picture-based, but some descriptions involve coding concepts

#### M1a: T28.G2.02 "Conduct a picture-based chance experiment"
- **Current**: "use a physical spinner (with a pencil and paperclip) or manipulative"
- **Good**: Uses physical materials as intended
- **Status**: Appropriate ✓

#### M1b: T28.G2.04 "Predict and observe outcomes"
- **Current**: "five physical coin flips (using real coins)"
- **Good**: Uses physical materials
- **Status**: Appropriate ✓

### M2: Too Vague - Needs More Specificity

#### M2a: T28.G5.08 "Track position and state for a single sprite"
- **Problem**: Vague and seems disconnected from probability/chance
- **Current**: "create a sprite that maintains position using x,y variables and tracks one additional state variable"
- **Fix**: Add specific context about random/probabilistic behavior OR move to T05/T09

#### M2b: T28.G6.02 "Use random seeds for reproducibility"
- **Problem**: Description is good, but CreatiCode only has seeded random for LIST generation, not standard random
- **Current**: "set a seed value before running simulation"
- **Issue**: The block `set [list] to (N) random numbers with seed (SEED)` only works for lists, not individual random calls
- **Fix**: Update description to specify: "Students populate a list with seeded random numbers, then draw from that list to ensure reproducible random sequences"

#### M2c: T28.G8.06 "Distinguish random from pseudorandom"
- **Problem**: Very theoretical, hard to make actionable in CreatiCode
- **Current**: "investigate how computers generate 'random' numbers"
- **Fix**: Make more concrete - have students compare results from list-based seeded random vs standard random

### M3: Missing Scaffolding Skills

#### M3a: Need skill for basic "pick random" block
- **Gap**: T28.G3.02 explains "pick random" but students haven't used it yet
- **Missing**: Between G2.04 (physical coins) and G3.02 (explain pick random)
- **Recommendation**: Add skill in early G3: "Use pick random block to simulate a die roll or coin flip"

#### M3b: Need skill for basic list operations before T28.G4.02.01
- **Gap**: G4.02.01 "Log trial results to a list" assumes list operations
- **Current dependency**: T10.G3.03 "Add and remove items from a list" ✓ (already present)
- **Status**: Covered ✓

#### M3c: Need skill for iterating through lists before counting frequencies
- **Gap**: T28.G4.02.02 "Count frequencies of each outcome" requires looping through lists
- **Missing**: No explicit dependency on list iteration
- **Recommendation**: Add T10 dependency for "iterate through list items" or T07 for "repeat with list"

#### M3d: Need skill for basic bar chart creation
- **Gap**: T28.G4.03 "Show how sample size changes variability" requires plotting bar charts
- **Current dependency**: T27.G3.04 "Create side-by-side bar charts" ✓
- **Status**: Covered, though might be too advanced (side-by-side vs single chart)

### M4: Skills Too Broad

#### M4a: T28.G7.05 "Communicate simulation assumptions and limitations"
- **Problem**: This is a writing/documentation skill, not a coding skill
- **Current**: "create a 'model card' document"
- **Issue**: Very broad, unclear success criteria
- **Fix**: Add specific rubric - "document must include at least 2 assumptions, 1 limitation, and 1 stakeholder impact statement"

#### M4b: T28.G8.04 "Publish simulation-backed policy briefs"
- **Problem**: This is a full writing assignment, very broad
- **Current**: "write a structured policy brief (1-2 pages)"
- **Issue**: More about writing than coding
- **Fix**: Clarify this is an integration skill combining T28 coding with communication. Consider moving to a separate "Communication" topic.

### M5: Dependency Issues (Non-X-2)

#### M5a: T28.G5.07 depends on T27.G4.02c
- **Skill**: T28.G5.07 "Create frequency distributions" (Grade 5)
- **Dependency**: T27.G4.02c "Calculate median and mode using code" (Grade 4)
- **Problem**: Frequency distributions don't require median/mode calculation - this seems like an unnecessary dependency
- **Fix**: Remove T27.G4.02c dependency, keep only T28.G5.01.02

#### M5b: T28.G6.01.01 has redundant dependencies
- **Skill**: T28.G6.01.01 "Manually test parameters and log results" (Grade 6)
- **Dependencies**: T09.G4.04, T09.G5.01, T28.G5.04
- **Problem**: T09.G5.01 likely subsumes T09.G4.04 (modify variables subsumes use variables)
- **Fix**: Remove T09.G4.04, keep T09.G5.01

#### M5c: T28.G6.02 has excessive dependencies
- **Skill**: T28.G6.02 "Use random seeds for reproducibility" (Grade 6)
- **Dependencies**: T07.G5.01, T08.G4.01, T09.G4.04, T09.G5.01, T28.G5.04
- **Problem**: Too many dependencies, some redundant
- **Fix**: Simplify to: T28.G5.04 (document plans), T09.G5.01 (modify variables), T07.G5.01 (loops)

---

## LOW PRIORITY ISSUES

### L1: Minor Description Improvements

#### L1a: T28.G2.01 "Sort events into certain/possible/impossible"
- **Current**: "illustrated events"
- **Suggestion**: Specify that this is a worksheet/offline activity to clarify it's picture-based
- **Add**: "using printed illustrations or digital slides"

#### L1b: T28.G3.03 "Record experimental data with teacher-provided blocks"
- **Current**: "copy the generated table into their notebook"
- **Issue**: Unclear if this means write by hand, screenshot, or export data
- **Fix**: Specify the recording method - "copy output into their digital or physical notebook"

#### L1c: T28.G4.04 "Debug an 'unfair' simulation"
- **Current**: "one outcome is favored (duplicate entries, wrong range)"
- **Good**: Specific examples ✓
- **Suggestion**: Add one more example - "unequal ranges in if-statements"

#### L1d: T28.G4.06 "Interpret probabilities as fractions and percentages"
- **Problem**: No coding - this is pure math
- **Current**: "express likelihood using both fraction and percentage notation"
- **Fix**: Add CreatiCode context - "use variables to convert between fraction and percentage representations in code"

#### L1e: T28.G5.02 "Randomly assign participants to conditions"
- **Current**: "write a function that tags each simulated user"
- **Problem**: CreatiCode doesn't have traditional functions, uses sprites/scripts
- **Fix**: Change to "write a script that tags each simulated user"

#### L1f: T28.G5.04 "Document simulation plans before coding"
- **Current**: "create a written simulation plan template"
- **Good**: Clear structure with 5 elements ✓
- **Suggestion**: Mention this could be done in a text file, document, or CreatiCode project notes

### L2: Success Criteria Could Be More Specific

#### L2a: T28.G3.02 "Explain what 'pick random' does"
- **Current**: "write what the block does in their own words"
- **Add**: "Explanation must include: the range of possible values and that each value has equal likelihood"

#### L2b: T28.G3.04 "Compare predictions to simulated data"
- **Current**: "compute the difference between prediction and actual counts"
- **Add**: "Students explain why differences occurred (randomness, not enough trials, etc.)"

#### L2c: T28.G5.10 "Recognize independence and gambler's fallacy"
- **Current**: "identify and explain gambler's fallacy in real-world scenarios"
- **Add**: "Students provide at least 2 real-world examples of gambler's fallacy"

### L3: Terminology Consistency

#### L3a: "Simulation" vs "Experiment"
- Throughout T28, skills use both "simulation" (G3.01, G5.03) and "experiment" (G2.02, G3.03)
- **Recommendation**: Use "experiment" for G2-G4 (simpler), "simulation" for G5+ (more technical)

#### L3b: "Script" vs "Code"
- Mix of "write a script" (G4.01, G5.08) and "write code" (G4.02.02)
- **Recommendation**: Use "script" consistently in CreatiCode context

### L4: Minor Ordering Improvements

#### L4a: G5 skills are out of logical order
- G5.08 "Track position and state" seems disconnected, comes after probability skills
- **Current order**: G5.01-G5.07 (probability), G5.08 (sprite state), G5.09-G5.11 (probability)
- **Recommendation**: Move G5.08 to end or beginning of G5 sequence

---

## SUMMARY OF RECOMMENDED FIXES

### Critical Fixes (Do First)
1. **Fix H1**: Remove T28.G3.06 from T28.G3.05 dependencies (forward reference)
2. **Fix H3**: Move T28.G5.08 to T05 or T09, or reframe for T28
3. **Fix H5**: Change T08.G5.01 references to T08.G3.01 or T08.G4.01
4. **Fix H2**: Clarify distinction between T28.G3.07 and T28.G4.01

### X-2 Rule Fixes (Review with Stakeholders)
- **Option A**: Accept X-1 for foundational skills (loops, conditionals)
- **Option B**: Adjust grade levels for affected T28 skills
- **Recommendation**: Option A - loops and conditionals are foundational and can be used in same/next grade

### Content Improvements
1. Fix M2b: Update T28.G6.02 description for list-based seeded random
2. Fix M3c: Add list iteration dependency to T28.G4.02.02
3. Fix M5a: Remove unnecessary T27.G4.02c dependency from T28.G5.07
4. Fix M5b, M5c: Simplify redundant dependencies

### Documentation Improvements
1. Add specific success criteria (L2a, L2b, L2c)
2. Improve terminology consistency (L3a, L3b)
3. Add clarity to descriptions (L1a-L1f)

---

## SKILLS THAT ARE CORRECT ✓

The following skills are well-structured and appropriate:
- T28.G2.01, G2.02, G2.03, G2.04 (picture-based, age-appropriate)
- T28.G3.03, G3.04, G3.06, G3.07 (clear progression)
- T28.G4.02.03, G4.03, G4.05, G4.07 (good scaffolding)
- T28.G5.01.01, G5.01.02, G5.05, G5.06, G5.09, G5.11 (probability concepts)
- T28.G6.03, G6.04, G6.06, G6.10, G6.11 (advanced concepts)
- T28.G7.02, G7.03, G7.04, G7.06.01, G7.06.02 (multi-agent, analysis)
- T28.G8.01, G8.02, G8.03, G8.05 (integration, real-world application)

---

## MISSING SKILLS NEEDED

1. **Early G3**: "Use pick random block for basic events" (between G2.04 and G3.02)
2. **G4**: "Iterate through list items to process data" (before G4.02.02) - may exist in T10
3. **G4**: "Create a simple bar chart from data" (before G4.03) - may exist in T27
4. **G5**: "Use if-statements with compound conditions" (for Monte Carlo) - may exist in T08

---

## TOTAL ISSUE COUNT

- **HIGH Priority**: 5 main issues (H1-H5, with H4 having 7 sub-issues) = 11 total
- **MEDIUM Priority**: 5 main issues (M1-M5, with multiple sub-issues) = 14 total
- **LOW Priority**: 4 main issues (L1-L4, with multiple sub-issues) = 15 total

**GRAND TOTAL**: 40 issues identified

---

## NEXT STEPS

1. Review and approve critical fixes (H1, H3, H5)
2. Decide on X-2 rule policy for foundational skills
3. Update skill descriptions based on approved fixes
4. Cross-reference with T05, T07, T08, T09, T10, T27 to verify dependencies exist
5. Create backup before making changes
