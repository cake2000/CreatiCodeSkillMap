# Grade 5 Topics T25-T36 Cross-Topic Dependency Analysis

## Executive Summary

Analyzed **99 Grade 5 skills** across topics T25-T36 (Data & CS Concepts) for cross-topic dependency issues.

### Key Findings

- **46 dependencies to add** - Missing critical cross-topic prerequisites
- **3 dependencies to remove** - X-2 rule violations (G5 depending on G2)
- **3 X-2 violations identified** - All have replacement suggestions

## Critical Issues: X-2 Rule Violations

The following skills violate the X-2 rule (Grade 5 cannot depend on Grade 2):

1. **T26.G5.02** - "Plan sampling strategies"
   - Remove: T26.G2.05
   - Add: T26.G3.01

2. **T30.G5.02** - "Plan safe device-handling procedures for group work"
   - Remove: T30.G2.04
   - Add: T30.G3.01

3. **T34.G5.03** - "Conduct interviews about technology changes"
   - Remove: T34.G2.03
   - Add: T34.G3.01

## Missing Dependencies by Topic

### T25 - Data Representation (23 additions)

Most T25 skills work with data structures and require:
- **T09.G3.03** (Variables) - for state tracking and data storage
- **T10.G3.05** (Lists) - for list/table operations
- **T07.G3.01** (Loops) - for data validation and iteration

Key affected skills:
- T25.G5.01.x - Game state variable series
- T25.G5.02.x - Data cleaning series
- T25.G5.06.x - Table operations series

### T28 - Probability (6 additions)

Simulation skills need:
- **T09.G3.03** (Variables) - for tracking simulation state
- **T07.G3.01** (Loops) - for running multiple trials
- **T10.G3.05** (Lists) - for multi-agent tracking

Key affected skills:
- T28.G5.01.02 - Compound event distributions
- T28.G5.04 - Simulation planning
- T28.G5.08 - Agent state tracking

### T29 - Text & NLP (6 additions)

Text parsing operations require:
- **T10.G3.05** (Lists) - split operations produce lists

Key affected skills:
- T29.G5.01 - Table schemas for text
- T29.G5.02 - Populate tables from text
- T29.G5.03.02 - Stop-word filters
- T29.G5.04.01 - Sentiment word lists
- T29.G5.06 - Parse sentence
- T29.G5.09 - Keyword highlighting

### T27 - Data Analysis (3 additions)

Interactive dashboards require:
- **T06.G3.01** (Events) - for widget interactions

Key affected skills:
- T27.G5.01 - Interactive dashboards
- T27.G5.00b - Widget events
- T27.G5.04 - Presentation features

### T31 - Internet (4 additions)

Multiplayer and interactive features need:
- **T06.G3.01** (Events) - for event-based interaction
- **T10.G3.05** (Lists) - for listing available games

Key affected skills:
- T31.G5.04 - Create/join multiplayer sessions
- T31.G5.04.01 - List available games
- T31.G5.05 - Connection status

### T30 - Hardware (2 additions)

1 X-2 violation fix + 1 legitimate addition:
- T30.G5.05.01 needs **T06.G3.01** for mouse picking events

## Analysis Methodology

**Conservative approach:**
1. Only added dependencies for hands-on coding skills (not purely conceptual)
2. Verified skills explicitly mention the prerequisite concept
3. Avoided redundant additions (if topic already has dependency from that area)
4. Focused on clear, necessary prerequisites

**Topic coverage:**
- T25: Data Representation ✓
- T26: Data Collection ✓
- T27: Data Analysis ✓
- T28: Probability ✓
- T29: Text & NLP ✓
- T30: Hardware ✓
- T31: Internet ✓
- T32: Security ✓ (no additions needed)
- T33: APIs ✓ (no additions needed - already complete)
- T34: Computing History ✓ (X-2 fix only)
- T35: Social Impacts ✓ (no additions needed)
- T36: Ethics ✓ (no additions needed)

## Files Generated

1. **GRADE5_T25_T36_ANALYSIS.json** - Full structured results
2. **GRADE5_T25_T36_EXECUTIVE_SUMMARY.md** - This document

## Next Steps

1. Review and validate the suggested additions
2. Apply the X-2 violation fixes (high priority)
3. Add missing cross-topic dependencies
4. Run validation to ensure no circular dependencies
5. Test that all suggested dependencies exist in the skill database
