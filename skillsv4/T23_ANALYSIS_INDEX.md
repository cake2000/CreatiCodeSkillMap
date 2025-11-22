# T23 AI Perception - Phase 1 Analysis Index

## Document Overview

This analysis identifies gaps, issues, and improvements needed for T23 (AI Perception) skills.

**Analysis Date:** 2025-11-21
**Current Skill Count:** 39 skills (K-8)
**Recommended Skill Count:** 47 skills (after critical fixes)
**Status:** Ready for Implementation

---

## Core Documents

### 1. **T23_changes_summary.md** (Main Analysis - 14,000 words)
**Purpose:** Comprehensive analysis of all T23 skills with detailed recommendations

**Contents:**
- Executive Summary
- Current skill distribution analysis
- 8 critical missing skills (detailed specifications)
- 6 recommended quality-of-life skills
- 3 overly broad skills requiring splits
- Block accuracy issues (5 skills)
- Grade appropriateness review (K-8)
- Intra-topic dependency violations (12 issues)
- Cross-topic dependency preservation
- Implementation priorities
- Final recommendations

**Key Findings:**
- ✅ Strong K-5 unplugged foundation
- ⚠️ 8 critical gaps in G6-G8
- ⚠️ 3 skills too broad
- ⚠️ 5 block descriptions inaccurate
- ⚠️ 12 dependency issues

**Use This For:** Understanding what's wrong and why

---

### 2. **T23_NEW_SKILLS_QUICK_REFERENCE.md** (Implementation Guide - 8,000 words)
**Purpose:** Ready-to-implement specifications for 8 critical new skills

**Contents:**
- Complete skill descriptions
- Block syntax with examples
- Key concepts for each skill
- Code examples (Scratch blocks)
- Dependencies and leads-to relationships
- CSTA alignment
- Integration points with existing skills

**New Skills Covered:**
1. T23.G6.01B: Use continuous speech recognition
2. T23.G6.04B: Read hand detection finger directions
3. T23.G6.08B: Compare single vs multi-person tracking
4. T23.G6.10: Use 3D pose detection
5. T23.G6.11: Use AR face camera
6. T23.G7.00A: Understand modality selection
7. T23.G8.00A: Understand KNN training
8. T23.G8.02B: Evaluate and tune KNN accuracy

**Use This For:** Writing new skills into allskills.md

---

### 3. **T23_ANALYSIS_INDEX.md** (This Document)
**Purpose:** Navigation and quick reference for analysis documents

**Use This For:** Finding what you need quickly

---

## Quick Reference Tables

### Current T23 Skill Distribution

| Grade | Current Count | After Critical Fixes | Skills Added |
|-------|--------------|---------------------|--------------|
| K     | 3            | 3                   | 0            |
| 1     | 3            | 3                   | 0            |
| 2     | 3            | 3                   | 0            |
| 3     | 3            | 3                   | 0            |
| 4     | 3            | 3                   | 0            |
| 5     | 4            | 4                   | 0            |
| **6** | **9**        | **14**              | **+5**       |
| **7** | **6**        | **7**               | **+1**       |
| **8** | **5**        | **7**               | **+2**       |
| TOTAL | 39           | 47                  | +8           |

---

### CreatiCode Feature Coverage

| Feature | Before | After | Status |
|---------|--------|-------|--------|
| Speech Recognition (single) | ✅ G6.01 | ✅ G6.01 | No change |
| Speech Recognition (continuous) | ❌ Missing | ✅ G6.01B | **NEW** |
| Face Detection (basic) | ✅ G6.09 | ✅ G6.09 | No change |
| AR Face Camera (3D mesh) | ❌ Missing | ✅ G6.11 | **NEW** |
| 2D Body Tracking | ✅ G6.08 | ✅ G6.08 | No change |
| Single vs Multi-person Mode | ⚠️ Mentioned | ✅ G6.08B | **NEW** |
| 3D Pose Detection | ⚠️ G7 only | ✅ G6.10 | **NEW** |
| Hand Detection (curl) | ✅ G6.04 | ✅ G6.04 | No change |
| Hand Detection (dir) | ❌ Missing | ✅ G6.04B | **NEW** |
| Hand Detection (x/y) | ✅ G6.05 | ✅ G6.05 | No change |
| KNN Classifier (basics) | ⚠️ Too broad | ✅ G8.00A | **NEW** |
| KNN Classifier (training) | ⚠️ G8.02 | ✅ G8.02 | Fixed |
| KNN Classifier (tuning) | ❌ Missing | ✅ G8.02B | **NEW** |
| Modality Selection | ❌ Missing | ✅ G7.00A | **NEW** |

**Coverage:** 10/14 features → 14/14 features (100%)

---

### Priority Breakdown

#### Priority 1: CRITICAL FIXES (Must Do)
**Impact:** Blocks skill progression, missing foundations, inaccurate descriptions

1. ✅ Add T23.G6.10 (3D pose intro) - blocks G7.03
2. ✅ Add T23.G8.00A (KNN foundation) - blocks G8.02
3. ⚠️ Split T23.G6.03 → G6.03A + G6.03B (too complex)
4. ⚠️ Split T23.G8.02 → G8.00A + G8.02 + G8.02B (too broad)
5. ⚠️ Fix 12 dependency violations (see summary doc)
6. ⚠️ Fix 5 block description inaccuracies (see summary doc)

**Estimated Effort:** 8 hours

---

#### Priority 2: IMPORTANT GAPS (Should Do)
**Impact:** Major features missing, incomplete scaffolding

7. ✅ Add T23.G6.01B (continuous speech) - major feature
8. ✅ Add T23.G6.04B (hand direction) - incomplete coverage
9. ✅ Add T23.G6.08B (single vs multi-person) - critical decision
10. ✅ Add T23.G6.11 (AR face camera) - complete feature missing
11. ✅ Add T23.G7.00A (modality selection) - missing foundation
12. ✅ Add T23.G8.02B (KNN tuning) - separated from G8.02

**Estimated Effort:** 6 hours

---

#### Priority 3: QUALITY IMPROVEMENTS (Nice to Have)
**Impact:** Better error handling, edge cases, advanced techniques

13. T23.G6.01C: Handle speech recognition errors
14. T23.G6.05B: Track multiple hands simultaneously
15. T23.G7.04B: Create accessibility testing logs
16. T23.G7.05B: Implement alternative input fallbacks
17. T23.G8.01B: Handle sensor failures
18. T23.G8.04B: Implement rate limiting

**Estimated Effort:** 4 hours (if implemented)

---

## Issues Summary

### Missing Skills (8 critical, 6 recommended)

**Critical:**
1. Continuous speech recognition (different mode, different blocks)
2. Hand direction (dir column never taught)
3. Single vs multi-person tracking (critical performance decision)
4. 3D pose detection (mentioned in G7 but never introduced)
5. AR face camera (complete feature missing)
6. Modality selection (no guidance on choosing)
7. KNN training foundation (jumps straight to advanced use)
8. KNN tuning/evaluation (combined with training in G8.02)

**Recommended:**
9. Speech error handling
10. Multiple hand tracking
11. Accessibility testing logs
12. Alternative input fallbacks
13. Sensor failure handling
14. Perception rate limiting

---

### Overly Broad Skills (3 skills need splitting)

1. **T23.G6.03: Build two-way voice chatbot**
   - Combines: Speech input + ChatGPT + TTS + loop
   - Split into: G6.03A (speech + text) + G6.03B (add TTS)

2. **T23.G7.03: Score pose-based challenge**
   - Uses 3D pose without introduction
   - Fix: Add G6.10 prerequisite (not a split, just missing foundation)

3. **T23.G8.02: Train and deploy KNN classifier**
   - Combines: Understanding training + collecting data + creating classifier + tuning K + evaluating
   - Split into: G8.00A (foundation) + G8.02 (train/deploy) + G8.02B (tune/evaluate)

---

### Block Accuracy Issues (5 skills)

1. **T23.G6.01:** Incomplete explanation of `text from speech` reporter
2. **T23.G6.04:** Missing `dir` column, only covers `curl`
3. **T23.G6.08:** Incorrect block syntax, should specify 17 landmarks
4. **T23.G7.03:** Uses 3D pose without prior introduction
5. **T23.G8.02:** Missing K parameter in block syntax

---

### Dependency Issues (12 intra-topic violations)

| Skill | Missing Dependency | Fix |
|-------|-------------------|-----|
| T23.G6.02 | T23.G6.01 | Add G6.01 (uses speech blocks) |
| T23.G6.05 | T23.G6.04 | Add G6.04 (uses hand blocks) |
| T23.G6.06 | T23.G6.01, G6.04, G6.08 | Add all (smooths multiple sensors) |
| T23.G7.01 | T23.G6.04B (NEW) | Add G6.04B (uses dir column) |
| T23.G7.02 | T23.G6.08 | Add G6.08 (mentions pose) |
| T23.G7.03 | T23.G6.10 (NEW) | Add G6.10 (uses 3D pose) |
| T23.G7.05 | T23.G7.04 | Add G7.04 (should monitor before fixing) |
| T23.G8.02 | T23.G8.00A (NEW) | Add G8.00A (needs training foundation) |

---

## Implementation Checklist

### Phase 1: Critical Fixes (Priority 1)
- [ ] Write T23.G6.10 (3D pose intro)
- [ ] Write T23.G8.00A (KNN foundation)
- [ ] Split T23.G6.03 → G6.03A + G6.03B
- [ ] Split T23.G8.02 → keep G8.02, extract G8.00A and G8.02B
- [ ] Fix 12 dependency violations in existing skills
- [ ] Fix 5 block description inaccuracies
- [ ] Update skill IDs (G6.03A, G6.03B, G8.00A, G8.02B)
- [ ] Test dependency chains (no cycles, X-2 rule)

### Phase 2: Important Gaps (Priority 2)
- [ ] Write T23.G6.01B (continuous speech)
- [ ] Write T23.G6.04B (hand direction)
- [ ] Write T23.G6.08B (single vs multi-person)
- [ ] Write T23.G6.11 (AR face camera)
- [ ] Write T23.G7.00A (modality selection)
- [ ] Update dependencies for new skills
- [ ] Test progression flow (K through 8)

### Phase 3: Quality Improvements (Priority 3 - Optional)
- [ ] Write 6 quality-of-life skills
- [ ] Integrate with existing skills
- [ ] Test edge cases and error handling

### Phase 4: Validation
- [ ] Verify all CreatiCode features covered
- [ ] Verify all block syntax accurate
- [ ] Verify no circular dependencies
- [ ] Verify X-2 rule compliance
- [ ] Verify grade-appropriate complexity
- [ ] Cross-check with T21 (AI Media) and T22 (ChatGPT)
- [ ] Cross-check with T19 (Multiplayer) for performance skills

---

## Cross-Topic Integration Points

### T23 Depends On:
- **T01-T03:** Basic CS concepts (K-2 unplugged)
- **T06:** Events (all perception needs event handlers)
- **T07:** Loops (for continuous processing)
- **T08:** Conditionals (for threshold checks)
- **T09:** Variables (for storing sensor data)
- **T10:** Tables (perception data stored in tables)
- **T11:** Custom blocks (for reusable helpers)
- **T14:** 3D coordinates (for pose and AR)
- **T16:** UI widgets (for controls and display)
- **T21:** AI Speaker (for TTS in voice chatbot)
- **T22:** ChatGPT (for voice chatbot)

### T23 Enables:
- **T14:** 3D avatar control with pose data
- **T19:** Multiplayer gesture controls
- **Accessible apps:** Multiple input modalities
- **AR apps:** Face and pose tracking
- **Fitness apps:** Body tracking
- **Voice apps:** Speech recognition
- **Gesture apps:** Hand detection
- **ML apps:** Custom classifiers

---

## Key Terminology

### Perception Modalities
- **Speech Recognition:** Converting voice to text (single or continuous)
- **Face Detection:** Locating faces with basic landmarks
- **AR Face Camera:** 3D face mesh with 468 points for AR effects
- **2D Body Tracking:** 17 body landmarks (x, y coordinates)
- **3D Pose Detection:** 33 body landmarks (x, y, z coordinates)
- **Hand Detection:** 21 hand keypoints with curl/direction per finger
- **Multimodal:** Combining multiple perception types

### Machine Learning
- **KNN Classifier:** K-Nearest-Neighbors algorithm for classification
- **Training:** Teaching AI by showing labeled examples
- **Label:** The correct answer/category
- **Features:** Measurements used for classification
- **K Value:** Number of neighbors to check
- **Accuracy:** Percentage of correct predictions
- **Tuning:** Adjusting parameters to improve performance

### Table Columns
- **Hand Detection:** part, x, y, curl, dir
- **2D Body Tracking:** part (17 landmarks), x, y, visibility
- **3D Pose Detection:** part (33 landmarks), x, y, z, visibility
- **Face Detection:** face_id, x, y, width, height, landmarks
- **KNN Training:** label, feature1, feature2, ...

---

## Related Documents

### Within T23:
- `T23_changes_summary.md` - Main analysis (this index points to)
- `T23_NEW_SKILLS_QUICK_REFERENCE.md` - Implementation specs
- `T23_ANALYSIS_INDEX.md` - This navigation document

### Related Topics:
- `T21_changes_summary.md` - AI Media (ChatGPT, DALL-E, TTS)
- `T22_changes_summary.md` - ChatGPT specific (for voice chatbot)
- `T19_changes_summary.md` - Multiplayer (for perception in multi-user games)
- `T14_changes_summary.md` - 3D Graphics (for pose-controlled avatars)

### Reference Documents:
- `allskills.md` - Main skill database
- Block specification docs (blockdes8.txt or similar)
- CreatiCode documentation (external)

---

## Visual Skill Progression (After Fixes)

```
GRADE K (Unplugged - Sensor Awareness)
├─ GK.01: Match pictures of sensing
├─ GK.02: Point to device sensors
└─ GK.03: Choose when to uncover sensors

GRADE 1 (Unplugged - Sensor Identification)
├─ G1.01: Find sensors on devices
├─ G1.02: Match sensors to human senses
└─ G1.03: Choose what sensors can notice

GRADE 2 (Unplugged - Sensor Selection)
├─ G2.01: Pick right sensor for job
├─ G2.02: Spot unclear sensor data
└─ G2.03: Notice devices sometimes guess

GRADE 3 (Conceptual - Data Representation)
├─ G3.01: Describe picture as pixel grid
├─ G3.02: Describe sound as waveform
└─ G3.03: Tell if behavior uses sensing + guessing

GRADE 4 (Applied Concepts - Input Quality)
├─ G4.01: Trace lighting changes on pixels
├─ G4.02: Choose good setup for sensors
└─ G4.03: Identify noise and fixes

GRADE 5 (Critical Thinking - Human vs AI)
├─ G5.01: Compare human vs pixel perception
├─ G5.02: Explain AI mis-hear/mis-see
├─ G5.03: Choose safe sensor data handling
└─ G5.04: Identify unfair AI sensing

GRADE 6 (Hands-On - Perception Blocks) ← MOST NEW SKILLS HERE
├─ G6.01: Speech recognition (single)
├─ G6.01B: Speech recognition (continuous) ← NEW
├─ G6.02: Map speech to UI
├─ G6.03A: Speech input + text output ← NEW (split from G6.03)
├─ G6.03B: Add TTS for voice loop ← NEW (split from G6.03)
├─ G6.04: Hand detection (curl)
├─ G6.04B: Hand detection (direction) ← NEW
├─ G6.05: Drive UI with hand
├─ G6.06: Smooth noisy sensor data
├─ G6.07: Add consent and privacy controls
├─ G6.08: 2D body tracking basics
├─ G6.08B: Single vs multi-person mode ← NEW
├─ G6.10: 3D pose detection ← NEW
├─ G6.09: Face detection (basic)
└─ G6.11: AR face camera (3D mesh) ← NEW

GRADE 7 (Multimodal Systems)
├─ G7.00A: Choose perception modality ← NEW
├─ G7.01: Define gesture dictionary
├─ G7.02: Multimodal confirmation (voice + gesture)
├─ G7.03: Score pose challenge with coaching
├─ G7.04: Monitor detection accuracy
├─ G7.05: Implement fairness safeguards
└─ G7.06: Build calibration wizard

GRADE 8 (Advanced Integration)
├─ G8.01: Interchangeable input modes
├─ G8.00A: Understand KNN training ← NEW
├─ G8.02: Train and deploy KNN ← REVISED (narrowed scope)
├─ G8.02B: Evaluate and tune KNN ← NEW
├─ G8.03: Fuse multimodal into simulation
├─ G8.04: Publish privacy plan
└─ G8.05: Evaluate societal impacts
```

---

## Change Log

### Version 1.0 (2025-11-21)
- Initial analysis completed
- Identified 8 critical missing skills
- Identified 6 recommended quality-of-life skills
- Identified 3 overly broad skills requiring splits
- Identified 5 block accuracy issues
- Identified 12 dependency violations
- Created implementation specifications for 8 critical skills
- Estimated 14 hours for full implementation

---

## Next Steps

1. **Review Analysis:**
   - Read T23_changes_summary.md (comprehensive analysis)
   - Review T23_NEW_SKILLS_QUICK_REFERENCE.md (implementation specs)

2. **Prioritize:**
   - Decide: Priority 1 + 2 (14 new skills) or Priority 1 only (2 new skills)
   - Consider timeline and resources

3. **Implement:**
   - Follow implementation checklist above
   - Use quick reference for skill specifications
   - Test after each phase

4. **Validate:**
   - Cross-check with CreatiCode documentation
   - Test skill progression (can students actually follow the path?)
   - Verify no broken dependencies

5. **Document:**
   - Update allskills.md with changes
   - Create change log
   - Update any affected cross-topic dependencies

---

**Document Version:** 1.0
**Created:** 2025-11-21
**Purpose:** Navigation and quick reference for T23 Phase 1 analysis
**Status:** Complete and ready for implementation
**Estimated Implementation Time:** 14 hours (Priority 1 + 2)
