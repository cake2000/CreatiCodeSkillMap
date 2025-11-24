# T17 (2D Motion & Physics) - Changes Summary
**Date:** 2025-11-23
**Status:** ✅ All HIGH and MEDIUM priority fixes completed

---

## Overview

Topic T17 (2D Motion & Physics) has been optimized with **13 changes** applied to improve clarity, completeness, and pedagogical effectiveness. The topic remains exemplary with an overall assessment of **8.5/10**.

**New skill count:** 77 → **81 skills** (4 new skills added)

---

## Changes Made

### ✅ 4 New Skills Added

1. **T17.G5.06.A.01** - Use debug mode to visualize collision shapes (Grade 5)
   - Teaches students to enable debug mode to see collision shape outlines
   - Critical for understanding why collisions happen or don't happen

2. **T17.G6.02.01.02** - Read velocity reporters for verification (Grade 6)
   - Teaches students to use velocity reporter blocks (x speed, y speed, speed)
   - Essential for debugging and verifying motion changes

3. **T17.G6.02.01.03** - Set rotation speed directly (Grade 6)
   - Teaches direct rotation control using 'physics set rotation speed'
   - Parallel to linear velocity control, moved from Grade 7

4. **T17.G7.04.01.01** - Apply torque impulse for instant rotation (Grade 7)
   - Teaches instant rotational "kick" using 'physics apply torque impulse'
   - Separates impulse from continuous torque

### ✅ 6 Skill Descriptions Enhanced

5. **T17.G6.07.01** - World border friction/restitution (clarified)
   - Now focuses ONLY on friction and restitution properties
   - Removed collision group mentions (moved to skill below)

6. **T17.G6.07.02** - World border collision groups (clarified)
   - Now focuses ONLY on collision groups for borders
   - Removed friction/restitution mentions

7. **T17.G7.04.01** - Use continuous torque (updated title & description)
   - Changed from "rotation speed and torque" to "continuous torque" only
   - Focuses exclusively on 'physics add torque' block
   - Updated dependencies to include T17.G6.02.01.03

8. **T17.G7.01.02** - Enhanced CCD explanation
   - Added explanation of "tunneling" problem before CCD solution
   - Better pedagogical approach: observe problem → understand cause → apply solution

9. **T17.G6.04.01** - Enhanced collision end examples
   - Added specific examples: lava damage, button release, exit zones
   - Provides concrete use cases for when END is better than START

10. **T17.G6.05** - Enhanced collision groups explanation
    - Added detailed 3-step process for setting up collision groups
    - Clarified bidirectional filter requirement
    - Included concrete example with players and power-ups

### ✅ 3 Dependency Updates

11. **T17.G5.06.01** - Updated dependency
    - Changed from T17.G5.06.A to T17.G5.06.A.01

12. **T17.G7.04.01** - Added dependency
    - Added T17.G6.02.01.03 (rotation speed basics before torque)

13. **T17.G7.04.01.01** - New skill dependencies
    - Depends on T17.G7.04.01 + T17.G5.08.02

---

## Impact Summary

### Coverage
- ✅ **100% block coverage maintained** - All 47 physics blocks taught
- ✅ **No skills deleted** - Only improvements and additions
- ✅ **Better granularity** - Overly broad skills properly split

### Pedagogy
- ✅ **Clearer progression** - Each skill focuses on ONE block/concept
- ✅ **Better scaffolding** - Debug mode and velocity reporters added where needed
- ✅ **Enhanced explanations** - CCD, collision end, collision groups now clearer

### Quality
- ✅ **No duplicates** - Each skill remains distinct
- ✅ **Proper dependencies** - All within-topic dependencies follow X-2 rule
- ✅ **Picture-based K-2** - All 4 early skills remain picture-based
- ✅ **Block-based G3+** - All 77 advanced skills remain hands-on coding

---

## Key Strengths Preserved

1. **Manual physics first** (G5.02-G5.04) before introducing physics engine
2. **Flexible learning paths** - Students can choose manual vs. engine approach
3. **Real-world applications** - Physics modeling, game design, optimization
4. **Excellent scaffolding** - Smooth K-8 progression maintained

---

## Files Modified

- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` (T17 section, lines ~10760-11500)

---

## Detailed Analysis Available

For complete analysis with all issues, block inventory, and recommendations:
- **Full Analysis:** `T17_ANALYSIS_2025-11-23_NEW.md` (35KB)
- **Quick Reference:** `T17_SUMMARY.md` (3.3KB)

---

## Status: COMPLETE ✅

All HIGH and MEDIUM priority issues within Topic T17 have been fixed. The topic now serves as an exemplary model for other topics in the skill map.

**Next Steps:**
- Continue to other topics following the same optimization process
- Phase 2: Cross-topic dependency optimization (acknowledged G6-G7 gaps to T07/T08/T09.G3)
