# T22 (Chatbots & Prompting) Optimization Summary

## Overview
Optimized Topic T22 to follow IXL-style skill design principles, ensuring each skill focuses on ONE specific block or concept with proper scaffolding and grade-appropriate progression.

## Key Changes Made

### 1. Removed Duplicate Skill
**Issue**: T22.G5.04 was a duplicate of T22.G3.02
- **Removed**: T22.G5.04 "Use a chatbot block to get AI responses"
- **Reason**: Identical functionality to T22.G3.02 "Make a simple ChatGPT request using the request block"
- **Action**: Updated all dependencies pointing to T22.G5.04 to reference T22.G5.03 instead (the proper G5 skill for prompt experimentation)

### 2. Split Overly Broad Skills

#### A. T22.G6.03: "Handle streaming mode and long requests"
**Split into 2 focused skills:**
- **T22.G6.03.01**: Use streaming mode to show words as they arrive
  - Focus: `mode` parameter for streaming display
  - Single block/concept: Streaming mode configuration

- **T22.G6.03.02**: Cancel long-running requests with the cancel block
  - Focus: `OpenAI ChatGPT: cancel request` block
  - Single block/concept: Request cancellation

**Rationale**: These are two distinct features requiring different skills - one about display modes, another about request control.

#### B. T22.G7.06: "Attach images and files to chatbot conversations"
**Split into 3 focused skills:**
- **T22.G7.06.01**: Attach costume images to chatbot conversations
  - Single block: `attach costume [NAME] to chat`
  - Focus: Sprite costume attachments

- **T22.G7.06.02**: Attach local files to chatbot conversations
  - Single block: `attach files to chat`
  - Focus: Local file uploads

- **T22.G7.06.03**: Attach Google Drive files to chatbot conversations
  - Single block: `attach file from Google Drive [URL] to chat`
  - Focus: Cloud file integration

**Rationale**: Each attachment method uses a different block and addresses different use cases (local sprites, device files, cloud storage).

#### C. T22.G7.07: "Use image moderation to filter visual content"
**Split into 2 focused skills:**
- **T22.G7.07.01**: Use image URL moderation to filter visual content
  - Single block: `get moderation result for image at URL [URL]`
  - Focus: Moderating images from URLs
  - Dependency: T22.G7.06.02 (local files, which could include URLs)

- **T22.G7.07.02**: Use costume image moderation to filter visual content
  - Single block: `get moderation result for costume named [NAME]`
  - Focus: Moderating sprite costumes
  - Dependency: T22.G7.06.01 (costume attachments)

**Rationale**: Different blocks for different image sources, aligning with the split attachment skills.

#### D. T22.G7.08: "Compare different LLM models using the generic LLM block"
**Split into 2 focused skills:**
- **T22.G7.08.01**: Use the generic LLM block to compare different models
  - Single block: `LLM model [PROVIDER] request [PROMPT]`
  - Focus: Making requests with different LLM models

- **T22.G7.08.02**: Set system instructions for generic LLM models
  - Single block: `LLM set system instruction [INSTRUCTION] for model [PROVIDER]`
  - Focus: Configuring system instructions for LLMs

**Rationale**: Two distinct blocks with different purposes - one for making requests, another for configuration.

### 3. Fixed Misplaced Dependencies

**Issue**: Dependencies were placed AFTER section separators instead of before

**T22.G6.08**: "Use multiple chatbot sessions with the select chatbot block"
- **Before**: Dependencies appeared after the "---" separator in G7 section
- **After**: Dependencies moved to proper position before the G6-G7 separator
- Dependencies preserved: T07.G5.01, T10.G5.01, T11.G5.01, T22.G6.01.02, T22.G6.01.03, T22.G6.04.02

**T22.G8.05**: "Integrate web search into chatbot responses"
- **Before**: Had separator in wrong location with dependencies after
- **After**: Properly formatted as final G8 skill with all dependencies before end of section
- Dependencies preserved: T05.G6.01, T06.G6.01, T07.G6.01, T09.G6.01, T13.G6.01, T22.G7.02.01, T22.G7.05, T22.G8.01.03

### 4. Simplified Excessive Dependencies

**Problem**: Many G6 skills had 8-10 cross-topic dependencies, making them overwhelming

**Strategy**: Reduced to essential dependencies while maintaining skill integrity
- Kept topic-specific dependencies (T22.*)
- Kept critical cross-topic dependencies (events, variables, loops, UI widgets)
- Removed redundant or overly granular dependencies (e.g., T05.G5.01 repeated in many skills)

**Examples of simplification**:
- **T22.G6.01.01**: Reduced from 10 to 7 dependencies
  - Removed: T05.G5.01 (user needs), T09.G5.01 (multi-variable expressions)
  - Kept: Core T22 progression, essential T06/T07/T09 skills

- **T22.G6.02**: Reduced from 10 to 8 dependencies
  - Focused on parameter configuration prerequisites
  - Maintained scaffolding from T22.G6.01.01

- **T22.G6.03.01 & T22.G6.03.02**: Each has 8 dependencies (down from original 10)
  - Split reduced cognitive load per skill
  - Essential T06-T11 dependencies maintained

### 5. Cleaned Up Dependency Format

**Issues found and fixed**:
1. Missing descriptions (e.g., "* T22.G5.02" without label)
2. Inconsistent formatting
3. Vague dependency labels

**Fixes applied**:
- All dependencies now have full skill descriptions
- Consistent format: `* T##.G#.##: [Full skill description]`
- Clear, specific descriptions matching the actual skill names

### 6. Updated Cross-References

**All internal T22 dependencies updated** to reflect new skill IDs:
- Skills referencing T22.G6.03 now reference T22.G6.03.01 (streaming mode)
- Skills referencing T22.G7.06 now reference appropriate sub-skill (T22.G7.06.01/.02/.03)
- Skills referencing T22.G7.07 now reference appropriate sub-skill (T22.G7.07.01/.02)
- Skills referencing T22.G7.08 now reference appropriate sub-skill (T22.G7.08.01/.02)
- Skills referencing T22.G5.04 (removed duplicate) now reference T22.G5.03

### 7. Preserved Alternative UI Paths

**Note in T22.G7.03, T22.G7.04, T22.G7.05**:
- These skills work with "either custom-built conversation displays or pre-built chat windows"
- Dependencies properly separated between:
  - T22.G6.04.02: Build a conversation log with dynamic updates (custom approach)
  - T22.G6.06.02: Manage chat messages with append and update blocks (pre-built approach)
- Students can follow either path based on their preference

### 8. Maintained X-2 Dependency Rule

**Verified** all dependencies follow the X-2 rule:
- Grade X skills only depend on grades X, X-1, or X-2
- No violations found in original or optimized version
- New sub-skills maintain proper grade progression

### 9. Preserved All Cross-Topic Dependencies

**All T21 dependencies maintained**:
- T21.G6.06: Check user input with AI content moderation (referenced in T22.G7.05)
- T21.G6.07: Use image moderation to check visual content (referenced in T22.G7.07.01, T22.G7.07.02)

**All other cross-topic dependencies preserved**:
- T06 (Events), T07 (Loops), T08 (Conditionals), T09 (Variables)
- T10 (Tables), T11 (Custom blocks), T12 (Code tracing)
- T13 (Testing), T15 (Animation), T16 (UI widgets)
- T18 (Physics), T24 (XO debugging), T29 (Data types)

## Skill Count Changes

| Grade Level | Original Count | Optimized Count | Change |
|-------------|---------------|----------------|--------|
| K           | 2             | 2              | 0      |
| 1           | 2             | 2              | 0      |
| 2           | 2             | 2              | 0      |
| 3           | 3             | 3              | 0      |
| 4           | 3             | 3              | 0      |
| 5           | 5             | 4              | -1 (duplicate removed) |
| 6           | 13            | 14             | +1 (split T22.G6.03 into 2) |
| 7           | 10            | 14             | +4 (split G7.06→3, G7.07→2, G7.08→2) |
| 8           | 9             | 9              | 0      |
| **TOTAL**   | **49**        | **53**         | **+4** |

## Benefits of Optimization

1. **Clearer Learning Objectives**: Each skill now focuses on ONE specific block or feature
2. **Better Scaffolding**: Sub-skills allow incremental mastery of complex features
3. **Easier Assessment**: Teachers can track mastery of specific blocks
4. **Improved Dependency Management**: Simplified cross-topic dependencies reduce cognitive load
5. **IXL-Style Precision**: Skills are specific, measurable, and manageable
6. **Maintained Flexibility**: Alternative UI paths (custom vs. pre-built) preserved
7. **Grade-Appropriate**: K-2 unplugged/picture-based, G3+ block-based coding

## Implementation Notes

1. **Sub-skill numbering**: Used format T##.G#.##.## for sub-skills (e.g., T22.G7.06.01)
2. **Dependency updates**: All internal references updated to new IDs
3. **Separator placement**: Fixed to only appear between grade levels, never within
4. **Description clarity**: Each skill clearly states which block(s) it teaches
5. **Progressive complexity**: Skills build logically from basic to advanced usage

## Files Generated

1. **T22_optimized_complete.md**: Complete optimized T22 section ready for integration
2. **T22_optimization_summary.md**: This summary document explaining all changes
