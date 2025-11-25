# T23 AI Perception - Skill ID Mapping

## Quick Reference: Old → New Skill IDs

This document shows how original skill IDs map to optimized skill IDs, useful for tracking changes and updating references.

---

## Unchanged Skills (62 skills)

These skills kept the same ID and only had minor description or dependency updates:

### Kindergarten (3 skills)
- T23.GK.01 ✓
- T23.GK.02 ✓
- T23.GK.03 ✓

### Grade 1 (3 skills)
- T23.G1.01 ✓
- T23.G1.02 ✓
- T23.G1.03 ✓

### Grade 2 (3 skills)
- T23.G2.01 ✓
- T23.G2.02 ✓
- T23.G2.03 ✓

### Grade 3 (3 skills)
- T23.G3.01 ✓
- T23.G3.02 ✓
- T23.G3.03 ✓

### Grade 4 (3 skills)
- T23.G4.01 ✓
- T23.G4.02 ✓
- T23.G4.03 ✓

### Grade 5 (4 skills remain, 1 split)
- T23.G5.01 ✓
- T23.G5.02 ✓
- T23.G5.03 ✓
- T23.G5.04 ✓

### Grade 6 (26 skills remain, 2 removed, 3 split)
- T23.G6.01.01 ✓
- T23.G6.01.02 ✓
- T23.G6.01.03 ✓
- T23.G6.01.04 ✓
- T23.G6.02.01 ✓
- T23.G6.02.02 ✓
- T23.G6.02.03 ✓
- T23.G6.03.01 ✓
- T23.G6.03.02 ✓
- T23.G6.04.01 ✓
- T23.G6.04.03 ✓ (unchanged)
- T23.G6.04.04 ✓
- T23.G6.04.05 ✓
- T23.G6.04.06 ✓
- T23.G6.04.07 ✓
- T23.G6.06.01 ✓
- T23.G6.06.02 ✓
- T23.G6.06.03 ✓
- T23.G6.06.04 ✓
- T23.G6.07 ✓
- T23.G6.08 ✓
- T23.G6.09.02 ✓ (unchanged)
- T23.G6.09.03 ✓
- T23.G6.10.01 ✓ (unchanged)
- T23.G6.11 ✓
- T23.G6.12 ✓

### Grade 7 (9 skills)
- T23.G7.00 ✓
- T23.G7.01 ✓
- T23.G7.01.02 ✓
- T23.G7.02 ✓
- T23.G7.03 ✓
- T23.G7.04 ✓
- T23.G7.05 ✓
- T23.G7.06 ✓
- T23.G7.07 ✓
- T23.G7.08 ✓
- T23.G7.09 ✓

### Grade 8 (12 skills remain, 1 split)
- T23.G8.00 ✓
- T23.G8.01 ✓
- T23.G8.01.02 ✓
- T23.G8.01.03 ✓
- T23.G8.02.01 ✓
- T23.G8.02.02 ✓
- T23.G8.02.03 ✓
- T23.G8.03 ✓
- T23.G8.03.01 ✓
- T23.G8.04 ✓
- T23.G8.04.01 ✓
- T23.G8.05 ✓
- T23.G8.05.01 ✓
- T23.G8.06 ✓
- T23.G8.07 ✓
- T23.G8.08 ✓
- T23.G8.09 ✓
- T23.G8.10 ✓
- T23.G8.11 ✓

---

## Skills Broken Down (4 → 13)

### T23.G5.05 → T23.G5.05.01, T23.G5.05.02, T23.G5.05.03

**Original T23.G5.05**: "Identify what data hand, body, and face detection provides"

**Split into**:
1. **T23.G5.05.01**: Identify what data different detection types provide
   - Match detection types to data outputs using picture cards
   - Understand the three detection types and their outputs

2. **T23.G5.05.02**: Map detection data to table structures
   - Examine annotated table examples
   - Practice reading table diagrams
   - Identify specific rows/columns

3. **T23.G5.05.03**: Understand perception API workflow patterns
   - Learn start → read → process → stop pattern
   - Match API blocks to workflow steps
   - Picture-based workflow analysis

**Rationale**: Original skill combined conceptual knowledge (what data exists), structural knowledge (how it's organized), and workflow knowledge (how to use it). Breaking into three skills provides better scaffolding before G6 coding.

---

### T23.G6.04.02 → T23.G6.04.02.01, T23.G6.04.02.02, T23.G6.04.02.03

**Original T23.G6.04.02**: "Read and display finger curl angles from hand detection"

**Split into**:
1. **T23.G6.04.02.01**: Understand hand detection table structure
   - Learn 47 rows per hand (5 summaries + 21 2D + 21 3D)
   - Understand curl (0-180°), dir (0-360°), x/y/z
   - Practice locating specific data rows

2. **T23.G6.04.02.02**: Read finger curl values from hand detection table
   - Use table read blocks to extract curl values
   - Understand curl measurement scale
   - Read specific fingers from rows 1-5

3. **T23.G6.04.02.03**: Display hand detection data using variable monitors
   - Display curl values on screen
   - Basic gesture detection with thresholds
   - Real-time updating display

**Rationale**: Original skill combined understanding table structure, reading values, and displaying/using them. Each is a distinct skill that should be learned separately for IXL-style granularity.

---

### T23.G6.09.01 → T23.G6.09.01.01, T23.G6.09.01.02, T23.G6.09.01.03, T23.G6.09.01.04

**Original T23.G6.09.01**: "Set up 2D body pose detection and read keypoint positions"

**Split into**:
1. **T23.G6.09.01.01**: Set up 2D body detection and view debug output
   - Start detection with the block
   - Explore debug visualization
   - Understand single vs multi-person mode

2. **T23.G6.09.01.02**: Understand body detection table structure
   - Learn 17 keypoints + 4 limbs
   - Understand occlusion and confidence
   - Table columns: id, part, x, y, curl, dir

3. **T23.G6.09.01.03**: Read body keypoint positions from the table
   - Extract keypoint x/y coordinates
   - Implement basic pose visualization
   - Draw stick figure from keypoints

4. **T23.G6.09.01.04**: Stop body detection when no longer needed
   - Proper cleanup and resource management
   - Detection lifecycle: start → use → stop
   - Prevent resource leaks

**Rationale**: Original skill combined setup, understanding structure, reading data, and visualization. Added stop skill for workflow completion. Four distinct skills for better granularity.

---

### T23.G6.10.02 → T23.G6.10.02.01, T23.G6.10.02.02, T23.G6.10.02.03

**Original T23.G6.10.02**: "Read face data and trigger actions based on detection"

**Split into**:
1. **T23.G6.10.02.01**: Understand face detection table structure
   - Learn 13 rows per face (1 tilt + 12 landmarks)
   - Table columns: ID, variable, value
   - Understand lighting effects

2. **T23.G6.10.02.02**: Read face position and tilt angle from table
   - Extract face center coordinates
   - Read tilt angle
   - Display values with variable monitors

3. **T23.G6.10.02.03**: Move a sprite to follow detected face
   - Implement face-following behavior
   - Handle edge cases (multiple faces, partial frames)
   - Error handling for "no face detected"

**Rationale**: Original skill combined understanding table structure, reading values, and implementing behavior. Each step is a separate learning objective.

---

### T23.G8.12 → T23.G8.12.01, T23.G8.12.02, T23.G8.12.03

**Original T23.G8.12**: "Design end-to-end ML workflow from data collection to deployment"

**Split into**:
1. **T23.G8.12.01**: Define ML problem and success metrics
   - Clear problem statement
   - Success metrics (accuracy, latency, fairness)
   - Requirements and assumptions

2. **T23.G8.12.02**: Plan data collection strategy with quality checks
   - Sample size and diversity
   - Quality checks and protocols
   - Documentation for team use

3. **T23.G8.12.03**: Document ML workflow and deployment plan
   - Complete 7-stage documentation
   - Testing and benchmarks
   - Deployment and maintenance plans

**Rationale**: Original skill was a massive capstone combining all ML workflow stages. Breaking into three manageable skills allows assessment of each stage independently while maintaining the end-to-end workflow concept.

---

## Skills Added (1 new workflow skill)

### T23.G6.04.08 (NEW)
**Skill**: Stop hand detection when no longer needed
**Description**: Implements proper cleanup for hand detection by stopping when no longer needed. Understands resource management and detection lifecycle.

**Rationale**: Original skills covered starting and using hand detection but didn't explicitly teach stopping it. Important for:
- Resource management (camera, CPU)
- Multi-modal applications (switching input modes)
- Good coding practices (cleanup)
- Completes the workflow: start → use → stop

---

## Skills Removed (2 unavailable features)

### T23.G6.10.03 ❌ REMOVED
**Original Skill**: "Detect facial expressions and emotions from face data"
**Reason**: CreatiCode does NOT support facial expression or emotion detection. Face detection only provides:
- Face position (x, y)
- Face tilt angle
- 6 facial landmarks (eyes, nose, mouth, ears) with x/y coordinates

**Impact**: Skills that incorrectly referenced expression/emotion detection have been removed. No replacement needed as feature doesn't exist.

---

### T23.G6.10.04 ❌ REMOVED
**Original Skill**: "Track face attributes like age, gender, and accessories"
**Reason**: CreatiCode does NOT support demographic attribute detection. Face detection does NOT provide:
- Age estimation
- Gender classification
- Glasses detection
- Facial hair detection
- Accessories detection

**Impact**: Skills that incorrectly referenced demographic attributes have been removed. No replacement needed as feature doesn't exist.

---

## Summary Statistics

| Change Type | Count | Details |
|-------------|-------|---------|
| Unchanged skills | 62 | Only minor description/dependency updates |
| Skills broken down | 4 → 13 | Better granularity (net +9) |
| Skills added | 1 | T23.G6.04.08 (workflow completion) |
| Skills removed | 2 | Unavailable features (expression, demographics) |
| **Total skills** | **72 → 79** | **Net +7 skills** |

### By Grade
- GK-G4: No changes (15 skills)
- G5: 5 → 7 skills (+2 from breaking down T23.G5.05)
- G6: 28 → 31 skills (+3 net: +6 from breakdowns, +1 new, -2 removed, -2 absorbed)
- G7: 9 → 9 skills (no changes)
- G8: 15 → 17 skills (+2 from breaking down T23.G8.12)

---

## Skill Numbering Notes

### Sub-skill ID Format
All sub-skills use the format: **T23.Gx.yy.zz**
- `T23`: Topic 23 (AI Perception)
- `Gx`: Grade level (GK, G1-G8)
- `yy`: Main skill number (01-99)
- `zz`: Sub-skill number (01-99)

### Examples
- T23.G5.05.01, T23.G5.05.02, T23.G5.05.03 (three parts of original T23.G5.05)
- T23.G6.04.02.01, T23.G6.04.02.02, T23.G6.04.02.03 (three parts of original T23.G6.04.02)
- T23.G6.09.01.01, T23.G6.09.01.02, T23.G6.09.01.03, T23.G6.09.01.04 (four parts of original T23.G6.09.01)

### Numbering Gaps
Some skill numbers appear to have gaps (e.g., no T23.G6.05). This is intentional:
- Preserves original numbering for unchanged skills
- Allows room for future additions
- Makes tracking changes easier (compare old vs new by ID)

---

## Migration Guide

### For Curriculum Developers
1. Update any lesson plans referencing removed skills (T23.G6.10.03, T23.G6.10.04)
2. Split existing activities for broken-down skills into sub-activities
3. Add new activity for T23.G6.04.08 (stop hand detection)
4. Review scaffolding for G5.05 skills - now three separate lessons

### For Assessment Creators
1. Remove questions about facial expressions/emotions
2. Remove questions about age/gender/accessory detection
3. Create separate assessments for each sub-skill (more granular evaluation)
4. Ensure assessments test ONE concept per skill (IXL-style)

### For Dependency Updates
All dependencies have been updated in the optimized version. If manually integrating:
1. Check X-2 rule for cross-topic dependencies
2. Remove redundant same-grade dependencies
3. Update references to broken-down skills (e.g., T23.G6.04.02 → T23.G6.04.02.03)
4. Update references to removed skills (find alternatives or remove)

---

## File Locations

- **Full optimized skills**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T23_optimized_complete.md`
- **Detailed summary**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T23_OPTIMIZATION_SUMMARY.md`
- **This mapping**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T23_SKILL_MAPPING.md`
