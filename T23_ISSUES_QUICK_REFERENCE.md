# T23 AI Perception - Issues Quick Reference
**Analysis Date:** 2025-11-23
**Total Issues Found:** 26 (6 HIGH, 11 MEDIUM, 9 LOW)

---

## QUICK ACTION LIST

### 🔴 DO IMMEDIATELY (HIGH Priority - 6 hours)

| # | Issue | Fix | Time |
|---|-------|-----|------|
| 1 | G5→G6 transition too steep | Add T23.G5.06: Understand perception API patterns | 2h |
| 2 | 3D pose (G6.10) introduced too late | Move G6.10 earlier, add G6 practice skill | 1h |
| 3 | KNN jumps to advanced without practice | Add T23.G8.01A: Train simple KNN from provided data | 2h |
| 4 | G6.02 missing TTS dependency | Add T23.G6.02.01 to dependencies | 5m |
| 5 | G6.06 missing detection dependencies | Add T23.G6.04.02 to dependencies | 5m |
| 6 | Face table columns not specified | Add column names to G6.09.01 description | 15m |

**Total: ~6 hours**

---

### 🟡 DO SOON (MEDIUM Priority - 9 hours)

| # | Issue | Fix | Time |
|---|-------|-----|------|
| 7 | No multimodal practice before complex skills | Add T23.G7.01B: Combine modalities with OR logic | 1.5h |
| 8 | No gesture practice before UI integration | Add T23.G6.04.04: Recognize basic hand gestures | 1.5h |
| 9 | No continuous vs. event-driven pattern taught | Add T23.G6.06B: Choose continuous vs. event detection | 1.5h |
| 10 | No performance optimization taught | Add T23.G7.06B: Optimize perception performance | 1.5h |
| 11 | Privacy skills overlap (G6.07, G7.05, G8.04) | Clarify boundaries in descriptions | 1h |
| 12 | Body pose landmark list incomplete | Add all 17 landmarks to G6.08.01 | 15m |
| 13 | 3D pose landmark count unclear (33 vs 17) | Explain relationship in G6.10 | 15m |
| 14 | Speech error handling not mentioned | Add error cases to G6.01.x | 30m |

**Total: ~9 hours**

---

### 🟢 DO LATER (LOW Priority - 5 hours)

| # | Issue | Fix | Time |
|---|-------|-----|------|
| 15 | Hand table structure not detailed | Add table row/column layout to G6.04.01 | 15m |
| 16 | TTS parameter defaults not specified | Add default/range values to G6.02.01 | 10m |
| 17 | G5.05 may be too abstract | Make more concrete with examples | 1h |
| 18 | G7.04 lacks assessment criteria | Add specific metrics/quantities | 30m |
| 19 | G8.02B may be too advanced | Simplify (remove confusion matrix term) | 30m |
| 20 | Multi-hand detection not covered | Add T23.G6.04.05: Track multiple hands | 1h |
| 21 | Face advanced features missing (TBD) | Verify CreatiCode capabilities, add if present | 1h |
| 22 | Low-resource environments not addressed | Enhance G7.05 or add G8.05B | 30m |

**Total: ~5 hours**

---

## NEW SKILLS TO ADD

### HIGH Priority New Skills (3 skills)

**T23.G5.06: Understand perception API patterns**
- Where: After T23.G5.05, before G6
- Why: Bridge G5 conceptual to G6 hands-on
- Content: Introduce start→process→end pattern
- Time: 2 hours to write

**T23.G6.10 (REPOSITION): Use 3D pose detection**
- Where: Move from end of G6 to after G6.08.02
- Why: G7.03 needs it, should practice in G6
- Content: Already exists, just reorder + add practice
- Time: 1 hour

**T23.G8.01A: Train simple KNN from provided data**
- Where: After T23.G8.00A, before G8.02
- Why: Practice before building full system
- Content: Use pre-filled table, focus on train/predict
- Time: 2 hours to write

---

### MEDIUM Priority New Skills (4 skills)

**T23.G6.04.04: Recognize basic hand gestures**
- Where: After T23.G6.04.03, before G6.05
- Why: Practice gesture recognition before UI
- Content: If-blocks for 3-4 simple gestures
- Time: 1.5 hours

**T23.G6.06B: Choose continuous vs. event-driven detection**
- Where: After T23.G6.06 or as standalone in G6
- Why: Important pattern not taught
- Content: Forever loop vs. single call, performance
- Time: 1.5 hours

**T23.G7.01B: Combine independent modalities with OR logic**
- Where: After T23.G7.01, before G7.02
- Why: Practice multimodal before complex state
- Content: Voice OR gesture triggers action (simple)
- Time: 1.5 hours

**T23.G7.06B: Optimize perception performance**
- Where: After T23.G7.06 or as standalone in G7
- Why: Student apps run slowly without optimization
- Content: Resolution, frame skipping, debug mode
- Time: 1.5 hours

---

### LOW Priority New Skills (1 skill)

**T23.G6.04.05: Track multiple hands simultaneously**
- Where: After T23.G6.04.03
- Why: Enable two-handed interactions
- Content: Left/right hand, two-handed gestures
- Time: 1 hour

---

## DEPENDENCY FIXES

### Add Dependencies

| Skill | Missing Dependency | Reason |
|-------|-------------------|--------|
| T23.G6.02 | T23.G6.02.01 | Uses TTS for fallback messages |
| T23.G6.06 | T23.G6.04.02 | Smooths wrist positions from hand detection |
| T23.G7.02 | T23.G7.01 | Should reuse gesture dictionary |

### Reorder Skills

| Skill | Current Position | New Position | Reason |
|-------|-----------------|--------------|--------|
| T23.G6.10 | After G6.09 (near end) | After G6.08.02 | G7.03 needs it, needs G6 practice |

---

## DESCRIPTION UPDATES

### Add Technical Details

**T23.G6.09.01** - Add face table columns:
```
Columns: face_id, x, y, width, height, [and any additional facial attributes]
```

**T23.G6.08.01** - Add all 17 body landmarks:
```
17 landmarks: nose (0), left/right eye (1-2), left/right ear (3-4), left/right shoulder (5-6),
left/right elbow (7-8), left/right wrist (9-10), left/right hip (11-12), left/right knee (13-14),
left/right ankle (15-16) with x/y coordinates.
```

**T23.G6.10** - Clarify 33 landmarks:
```
33 body landmarks (includes all 17 from 2D mode plus 16 additional hand/foot detail points)
with depth information (x, y, z coordinates).
```

**T23.G6.02.01** - Add TTS parameter defaults:
```
Speed/pitch/volume parameters: default 100, range 50-200 (percentage)
```

**T23.G6.04.01** - Add hand table structure:
```
Result table contains 21 rows (one per hand keypoint) with columns: part (wrist, thumb_tip,
index_tip, etc.), x, y, curl (0-180), and dir (direction).
```

---

### Add Error Handling Context

**T23.G6.01.01, G6.01.02, G6.01B** - Add to descriptions:
```
They learn to handle empty results (no speech detected) using if-blocks to check if the
text is empty before proceeding.
```

---

### Clarify Skill Boundaries

**T23.G6.07** - Focus on basic consent:
```
Clear permission requests, on/off toggle buttons, and basic data clearing (clear table after use).
```

**T23.G7.05** - Focus on adaptive fairness (remove "multiple attempts"):
```
Adaptive thresholds that adjust to user patterns, user feedback collection for system
improvement, and alternative input methods when sensors struggle.
```

**T23.G8.02B** - Simplify for grade 8 (remove "confusion matrix" term):
```
They document which gestures get confused with each other and explain how K affects
performance: low K = very sensitive to nearest example (noisy), high K = averages many
examples (smoother but less precise).
```

---

## VERIFICATION NEEDED

1. **Face Detection Table Columns** - Check actual CreatiCode face detection output
   - Does it provide: face_id, x, y, width, height?
   - Does it provide: age, emotion, landmarks?
   - Update descriptions accordingly

2. **3D Pose Landmark Count** - Verify actual 3D pose output
   - Is it 33 landmarks or different number?
   - What are the additional landmarks beyond 2D's 17?

3. **Hand Detection Multi-Hand Support** - Verify CreatiCode capability
   - Can it detect both hands simultaneously?
   - How are they distinguished in the table?

---

## IMPLEMENTATION PRIORITY

### Week 1: Critical Fixes (HIGH Priority)
- [ ] Add T23.G5.06 (perception API patterns bridge)
- [ ] Move T23.G6.10 earlier in G6 sequence
- [ ] Add T23.G8.01A (simple KNN practice)
- [ ] Fix dependencies (G6.02, G6.06)
- [ ] Add face table columns to G6.09.01

**Outcome:** Unblocks progression, fixes critical gaps

---

### Week 2: Important Improvements (MEDIUM Priority)
- [ ] Add T23.G6.04.04 (gesture practice)
- [ ] Add T23.G6.06B (continuous vs. event pattern)
- [ ] Add T23.G7.01B (simple multimodal)
- [ ] Add T23.G7.06B (performance optimization)
- [ ] Clarify privacy skill boundaries
- [ ] Add body pose landmark list
- [ ] Add speech error handling

**Outcome:** Complete scaffolding, professional quality

---

### Week 3: Quality Polish (LOW Priority - optional)
- [ ] Add hand table structure details
- [ ] Add TTS parameter defaults
- [ ] Refine G5.05 (make more concrete)
- [ ] Add assessment criteria to G7.04
- [ ] Simplify G8.02B language
- [ ] Add T23.G6.04.05 (multi-hand) if desired
- [ ] Verify and add face advanced features

**Outcome:** Comprehensive coverage, handles edge cases

---

## IMPACT SUMMARY

### Before Fixes
- ❌ Steep G5→G6 transition
- ❌ 3D pose appears too late
- ❌ KNN too complex too fast
- ❌ Missing practice skills
- ❌ Some dependency errors
- ⚠️ Technical details incomplete

### After HIGH Priority Fixes (~6 hours)
- ✅ Smooth G5→G6 transition
- ✅ 3D pose properly scaffolded
- ✅ KNN has practice before advanced
- ✅ All critical dependencies correct
- ✅ Face detection fully documented
- ⚠️ Still missing some practice skills (MEDIUM priority)

### After HIGH + MEDIUM Fixes (~15 hours)
- ✅ Complete scaffolding throughout
- ✅ Practice skills between all major jumps
- ✅ Continuous vs. event pattern taught
- ✅ Performance optimization covered
- ✅ All technical details complete
- ✅ Privacy skills clearly bounded
- ⚠️ Some quality improvements remain (LOW priority)

### After All Fixes (~20 hours)
- ✅ Production-ready skill set
- ✅ Comprehensive coverage
- ✅ Handles edge cases
- ✅ Clear assessment criteria
- ✅ Multi-hand and advanced features
- ✅ Grade-appropriate throughout

---

## CONTACT/QUESTIONS

For questions about specific issues, see **T23_COMPREHENSIVE_ISSUES_ANALYSIS.md** for detailed explanations.

**Document Version:** 1.0
**Created:** 2025-11-23
**Status:** READY FOR IMPLEMENTATION
