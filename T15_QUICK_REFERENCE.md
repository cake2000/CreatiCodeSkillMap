# T15 Optimization Quick Reference

**Quick checklist for implementing the T15 optimization**

## Delete (1 skill)
- [ ] T15.G3.10 - Enhanced say with styling (redundant)

## Add (14 new skills)
- [ ] T15.G3.04.01 - Style speech bubbles for mood and emphasis
- [ ] T15.G3.11.01 - Position labels for titles and UI elements
- [ ] T15.G3.11.02 - Update label text for dynamic displays
- [ ] T15.G3.12.01 - Create timed and sprite-relative text
- [ ] T15.G3.12.02 - Clear printed text for scene changes
- [ ] T15.G4.02.01 - Program sprite responses to scene broadcasts
- [ ] T15.G5.09.01 - Draw ovals and circles on vector costumes
- [ ] T15.G5.09.02 - Create dynamic visual effects with shape drawing
- [ ] T15.G5.10.01 - Draw bezier curves on vector costumes
- [ ] T15.G5.10.02 - Draw text on vector costumes
- [ ] T15.G5.12.01 - Select languages and voice types for text-to-speech
- [ ] T15.G5.12.02 - Adjust speech characteristics for expression
- [ ] T15.G5.13.01 - Format text inside widgets
- [ ] T15.G5.13.02 - Create cohesive widget themes for story atmosphere

## Modify (12 skills)
- [ ] T15.G3.01 - Remove dependency on G3.00.03
- [ ] T15.G3.04 - Teach styled say block (not basic)
- [ ] T15.G3.05 - Teach styled think block (not basic)
- [ ] T15.G3.05.01 - Update dependencies (G3.10 → G3.04.01)
- [ ] T15.G3.11 - Simplify to widget creation
- [ ] T15.G3.12 - Simplify to print basics
- [ ] T15.G4.02 - Focus on broadcast mechanism
- [ ] T15.G5.09 - Focus on rectangles only
- [ ] T15.G5.10 - Focus on straight lines only
- [ ] T15.G5.11 - Update dependencies, clarify clearing
- [ ] T15.G5.12 - Simplify to basic TTS
- [ ] T15.G5.13 - Focus on colors/borders

## Critical Fixes
1. **Remove illogical dependency**: G3.01 should NOT depend on G3.00.03 (paint editor)
2. **Fix say/think blocks**: Teach actual styled blocks, not non-existent basic versions
3. **Delete redundant G3.10**: Only styled say exists, teach it in G3.04
4. **Break down complex skills**: Each skill = one focused concept

## Implementation Order
1. Delete T15.G3.10 first
2. Update all dependencies referencing G3.10
3. Modify existing skills (descriptions + dependencies)
4. Add new sub-skills in numerical order
5. Verify all dependencies resolve correctly

## Final Stats
- Before: 70 skills
- After: 83 skills
- Net: +13 skills (+19%)

See T15_OPTIMIZATION_SUMMARY.md for complete details.
