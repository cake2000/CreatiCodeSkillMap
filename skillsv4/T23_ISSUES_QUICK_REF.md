# T23 AI Perception - Issues Quick Reference

## At a Glance

**Total Issues**: 26 across 22 skills
**Status**: Optimization 70% complete, needs refinement

---

## 🔴 CRITICAL (Fix First)

### Structural Breaks
- **G8.01.02** → Wrong parent (should be G8.00.01) - KNN skills misplaced
- **G8.03.01** → Wrong parent (evaluation should come before simulation)
- **G8.01.03** → Wrong parent (should be G8.00.02)

### Core Description Errors
- **G6.04.02.01** → Hand table structure incomplete (curl/dir only in rows 1-5)
- **G6.09.01.02** → Body table structure incomplete (curl/dir only in limbs)

**Impact**: Breaks skill tree structure, causes confusion about API

---

## 🟡 HIGH IMPACT (Fix Soon)

### Skills Too Broad (Need Breakdown)
1. **G6.04.04** → 4 sub-skills (fist, open, pointing, multi-gesture)
2. **G6.09.02** → 4 sub-skills (distance, arms-up, squat, trigger)
3. **G6.03.01** → 3 sub-skills (speech→GPT, GPT→TTS, turn-taking)

### Missing Scaffolding (5 Gaps)
1. **G5.05.04** → Trace speech workflow (missing bridge G5→G6)
2. **G6.04.02.04** → Single threshold gesture (missing scaffold)
3. **G6.01.03.01** → Detect empty speech (missing scaffold)
4. **G8.00.01** → Understand KNN concept (missing scaffold)
5. **G8.08.04** → Evaluate NN performance (missing scaffold)

### Grade Issues
- **G5.05.01-03** → Picture-based, need hands-on component (violates G3+ rule)

---

## 🟢 MEDIUM (Improve Granularity)

### More Skills That Could Be Broken Down
- **G8.02.01** → 3 sub-skills (table design, UI, workflow)
- **G8.03.01** → 3 sub-skills (confusion matrix already broken down, but numbered wrong)
- **G7.06** → 3 sub-skills (mic calibration, camera calibration, wizard UI)
- **G8.03** → 3 sub-skills (multi-user design, parallel processing, logging)
- **G8.08** → 3 sub-skills (architecture, training, comparison)
- **G8.12.03** → 2 sub-skills (training docs, deployment docs)

---

## 🔵 LOW (Fine-Tuning)

### Dependency Issues
- **G7.00** → Violates X-2 rule (depends on G6 skills)
- **G6.01.01** → Duplicate T09.G5.01 dependency
- **G6.04.08** → Missing dependency on G6.04.04 or G6.04.05
- **All G6** → Depend on G5 skills (may violate X-2 if strict)

### Description Accuracy
- **G6.11** → NLP output not specified (what does table contain?)

---

## Quick Fixes Checklist

### Structural (2 hours)
- [ ] Renumber G8.01.02 → G8.00.01 (Practice KNN)
- [ ] Renumber G8.01.03 → G8.00.02 (Split train/test data)
- [ ] Renumber G8.03.01 → proper sequence (Evaluate classifier)
- [ ] Fix parent-child relationships

### Descriptions (2 hours)
- [ ] Correct G6.04.02.01 (hand table: curl/dir in rows 1-5 only)
- [ ] Correct G6.09.01.02 (body table: curl/dir in limb rows only)
- [ ] Clarify G6.11 (NLP table output format)

### Dependencies (2 hours)
- [ ] Fix G7.00 dependencies (use G5 skills)
- [ ] Remove G6.01.01 duplicate
- [ ] Add G6.04.08 missing dependency
- [ ] Review all G6→G5 dependencies for X-2

### Scaffolding (4 hours)
- [ ] Add G5.05.04 (trace speech workflow)
- [ ] Add G6.04.02.04 (single threshold gesture)
- [ ] Add G6.01.03.01 (detect empty speech)
- [ ] Add G8.00.01 (understand KNN)
- [ ] Add G8.08.04 (evaluate NN)

### Breakdown Top 3 (6 hours)
- [ ] Break G6.04.04 → .01-.04 (gestures)
- [ ] Break G6.09.02 → .01-.04 (poses)
- [ ] Break G6.03.01 → .01-.03 (voice chatbot)

### Grade-Appropriateness (2 hours)
- [ ] Add hands-on to G5.05.01 (observe examples)
- [ ] Add hands-on to G5.05.02 (read tables)
- [ ] Add hands-on to G5.05.03 (trace code)

**Total Estimated Time**: 18 hours for all fixes

---

## Skills That Are GOOD ✅

### All GK-G2 (9 skills)
Picture-based, unplugged, age-appropriate

### All G3-G4 (6 skills)
Hands-on coding, appropriate complexity

### Many G6 Skills (20+ skills)
Good granularity, accurate descriptions:
- Speech recognition sequence (G6.01.01-.04)
- TTS sequence (G6.02.01-.03)
- Hand detection sub-skills (G6.04.02.01-.03)
- Body detection sub-skills (G6.09.01.01-.04)
- Face detection sub-skills (G6.10.01, G6.10.02.01-.03)
- Smoothing techniques (G6.06.01-.04)
- Detection patterns (G6.07)
- Privacy controls (G6.08)

### All G7 Skills (11 skills)
Advanced integration, appropriate complexity

### Most G8 Skills (15+ skills)
ML concepts, advanced topics, good depth

---

## What Was Already Fixed ✅

- ❌ Removed G6.10.03 (facial expressions - NOT AVAILABLE)
- ❌ Removed G6.10.04 (age/gender - NOT AVAILABLE)
- ✅ Added G5.05.01-.03 (broke down G5.05)
- ✅ Added G6.04.02.01-.03 (broke down G6.04.02)
- ✅ Added G6.09.01.01-.04 (broke down G6.09.01)
- ✅ Added G6.10.02.01-.03 (broke down G6.10.02)
- ✅ Added G8.12.01-.03 (broke down G8.12)
- ✅ Added G6.04.08 (stop hand detection)

**Already improved**: 72 → 92 skills (+20 skills)

---

## Priority Order

1. **Fix numbering** (G8.01.02, G8.01.03, G8.03.01) - 1 hour
2. **Fix table descriptions** (G6.04.02.01, G6.09.01.02) - 1 hour
3. **Add 5 scaffolding skills** - 4 hours
4. **Break down top 3 broad skills** - 6 hours
5. **Fix dependencies** - 2 hours
6. **Add G5 hands-on** - 2 hours
7. **Break down remaining 6 skills** (optional) - 8 hours

**Core fixes**: 8 hours
**Full refinement**: 24 hours

---

## Files

- **Full analysis**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T23_REMAINING_ISSUES.md`
- **This quick ref**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T23_ISSUES_QUICK_REF.md`
- **Current optimized**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T23_optimized_complete.md`
- **Optimization summary**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T23_OPTIMIZATION_SUMMARY.md`
