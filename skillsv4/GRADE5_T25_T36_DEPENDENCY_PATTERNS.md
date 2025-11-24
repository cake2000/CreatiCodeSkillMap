# Grade 5 T25-T36 Dependency Patterns

## Most Commonly Added Dependencies

### T10.G3.05 (Lists) - 19 additions
**Why:** Data representation, text parsing, and analysis skills heavily use lists and tables.

**Topics affected:**
- T25 (Data Representation) - 13 times
- T29 (Text & NLP) - 6 times

**Example skills:**
- T25.G5.01.01 - Design multi-type data structures on paper
- T25.G5.06.02 - Query tables by value
- T29.G5.02 - Populate data tables from text using split
- T29.G5.09 - Highlight keywords in text display

### T09.G3.03 (Variables) - 11 additions
**Why:** State tracking, data storage, and value management across multiple topics.

**Topics affected:**
- T25 (Data Representation) - 11 times

**Example skills:**
- T25.G5.01.02.01 - Define game state variables with initial values
- T25.G5.04 - Encode categorical values with numeric codes
- T25.G5.07 - Validate data types and ranges before storage

### T06.G3.01 (Events) - 7 additions
**Why:** Interactive features like dashboards, multiplayer, and mouse interactions.

**Topics affected:**
- T31 (Internet) - 3 times
- T27 (Data Analysis) - 3 times
- T30 (Hardware) - 1 time

**Example skills:**
- T27.G5.01 - Build a simple interactive dashboard with filter widgets
- T27.G5.00b - Respond to widget events in dashboards
- T31.G5.04 - Create and join a multiplayer game session
- T30.G5.05.01 - Enable mouse picking and hovering for 3D objects

### T07.G3.01 (Loops) - 6 additions
**Why:** Data validation, simulation iterations, and processing multiple items.

**Topics affected:**
- T25 (Data Representation) - 4 times
- T28 (Probability) - 2 times

**Example skills:**
- T25.G5.02.02.04 - Validate cleaned data against rules
- T28.G5.01.02 - Analyze compound event distributions
- T28.G5.08 - Track agent state for probabilistic simulations

### T26.G3.01, T30.G3.01, T34.G3.01 - 1 each
**Why:** X-2 rule violation fixes - replacing G2 dependencies with G3 equivalents.

## Dependency Pattern Summary

### T25 (Data Representation)
**Pattern:** Variables + Lists + Loops
- Most skills need T09.G3.03 (variables) for state/value tracking
- Most skills need T10.G3.05 (lists) for table/list operations
- Validation skills need T07.G3.01 (loops) for iteration

### T27 (Data Analysis)
**Pattern:** Events for interactivity
- Dashboard and widget skills need T06.G3.01 (events)

### T28 (Probability)
**Pattern:** Variables + Loops + Lists
- Simulation skills need T09.G3.03 (variables) for state tracking
- Simulation skills need T07.G3.01 (loops) for running trials
- Multi-agent skills need T10.G3.05 (lists) for tracking multiple entities

### T29 (Text & NLP)
**Pattern:** Lists for text processing
- All text parsing skills need T10.G3.05 (lists) because split operations produce lists

### T30 (Hardware)
**Pattern:** Events for interaction
- Interactive features (mouse picking) need T06.G3.01 (events)

### T31 (Internet)
**Pattern:** Events + Lists for multiplayer
- Multiplayer skills need T06.G3.01 (events) for interaction
- Listing features need T10.G3.05 (lists) for displaying game lists

## Implementation Priority

### High Priority (X-2 Violations)
1. T26.G5.02 - Replace T26.G2.05 with T26.G3.01
2. T30.G5.02 - Replace T30.G2.04 with T30.G3.01
3. T34.G5.03 - Replace T34.G2.03 with T34.G3.01

### Medium Priority (Core Data Skills)
4. T25.G5.x skills - Add T09.G3.03 and T10.G3.05 (23 additions)
5. T29.G5.x skills - Add T10.G3.05 (6 additions)

### Lower Priority (Specialized Features)
6. T28.G5.x skills - Add T09.G3.03, T07.G3.01, T10.G3.05 (6 additions)
7. T27.G5.x skills - Add T06.G3.01 (3 additions)
8. T31.G5.x skills - Add T06.G3.01, T10.G3.05 (4 additions)
9. T30.G5.05.01 - Add T06.G3.01 (1 addition)

## Quality Assurance Notes

- All suggested dependencies verified to exist in skill database
- All target skills verified to exist in skill database
- No circular dependencies introduced (all additions are from G3 to G5)
- Conservative approach: only coding skills, not purely conceptual ones
- Avoided redundancy: checked for existing topic dependencies before adding
