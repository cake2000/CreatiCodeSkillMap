# T23 AI Perception - Visual Issues Map

## Legend
- ✅ **GREEN**: No issues, skill is good
- 🟡 **YELLOW**: Needs breakdown (too broad)
- 🔴 **RED**: Critical issue (structural/accuracy)
- 🔵 **BLUE**: Missing skill (scaffolding gap)
- ⚪ **WHITE**: Minor issue (dependencies, description)

---

## Grade K (3 skills) - ALL ✅

```
T23.GK.01 ✅ Match pictures of sensing
T23.GK.02 ✅ Point to where device looks/listens
T23.GK.03 ✅ Choose when to uncover helper
```

**Status**: Perfect - picture-based, unplugged, age-appropriate

---

## Grade 1 (3 skills) - ALL ✅

```
T23.G1.01 ✅ Find sensors on everyday devices
T23.G1.02 ✅ Match sensors to human senses
T23.G1.03 ✅ Choose what sensor can notice
```

**Status**: Perfect - picture-based, conceptual learning

---

## Grade 2 (3 skills) - ALL ✅

```
T23.G2.01 ✅ Pick the right sensor for a job
T23.G2.02 ✅ Spot when sensor data unclear
T23.G2.03 ✅ Notice that devices sometimes guess
```

**Status**: Perfect - scenario-based, decision-making

---

## Grade 3 (3 skills) - ALL ✅

```
T23.G3.01 ✅ Describe picture as grid of colors
T23.G3.02 ✅ Describe sound as wavy line
T23.G3.03 ✅ Tell if behavior uses sensing/guessing
```

**Status**: Good - hands-on coding starts here

---

## Grade 4 (3 skills) - ALL ✅

```
T23.G4.01 ✅ Trace how lighting changes pixel data
T23.G4.02 ✅ Choose good setup for mic/camera
T23.G4.03 ✅ Identify noise and simple fixes
```

**Status**: Good - hands-on with troubleshooting

---

## Grade 5 (7 skills) - 4 ✅, 3 ⚪

```
T23.G5.01 ✅ Compare people vs pixels
T23.G5.02 ✅ Explain why AI mis-hears/mis-sees
T23.G5.03 ✅ Choose safe ways to handle data
T23.G5.04 ✅ Identify unfair sensing

T23.G5.05.01 ⚪ Identify detection data types
T23.G5.05.02 ⚪ Map detection data to tables
T23.G5.05.03 ⚪ Understand API workflow patterns

[MISSING] 🔵 T23.G5.05.04 Trace speech workflow (MISSING SCAFFOLD)
```

**Issues**:
- G5.05.01-03: Need hands-on component (currently picture-based)
- Missing: G5.05.04 to bridge to G6

---

## Grade 6 (37 skills) - 27 ✅, 6 🟡, 3 🔴, 1 🔵

### Speech Recognition (5 skills) ✅ + 🔵

```
T23.G6.01.01 ✅ Capture single phrase with basic speech
T23.G6.01.02 ✅ Select language, observe accuracy
T23.G6.01.03 ✅ Use continuous speech recognition
[MISSING] 🔵 T23.G6.01.03.01 Detect empty speech result (MISSING SCAFFOLD)
T23.G6.01.04 ✅ Handle errors with retry logic
```

### Text-to-Speech (3 skills) ✅

```
T23.G6.02.01 ✅ Convert text to speech with settings
T23.G6.02.02 ✅ Control TTS playback (stop speaking)
T23.G6.02.03 ✅ Save and reuse TTS audio
```

### Voice Chatbot (2 skills) 🟡

```
T23.G6.03.01 🟡 Build voice chatbot loop
  └─ TOO BROAD: Combines speech→GPT→TTS→timing
     NEEDS: Break into .01 (speech→GPT), .02 (GPT→TTS), .03 (turn-taking)

T23.G6.03.02 ✅ Use OpenAI Whisper
```

### Hand Detection (8 skills) 🔴 + 🟡 + 🔵

```
T23.G6.04.01 ✅ Set up hand detection, view debug

T23.G6.04.02.01 🔴 Understand hand table structure
  └─ CRITICAL: Description incomplete (curl/dir only in rows 1-5)

T23.G6.04.02.02 ✅ Read finger curl values
T23.G6.04.02.03 ✅ Display hand data with monitors

[MISSING] 🔵 T23.G6.04.02.04 Detect single threshold gesture (MISSING SCAFFOLD)

T23.G6.04.03 ✅ Read finger direction data

T23.G6.04.04 🟡 Recognize basic gestures
  └─ TOO BROAD: 3-5 gestures, complex logic
     NEEDS: Break into .01 (fist), .02 (open), .03 (pointing), .04 (multi)

T23.G6.04.05 ✅ Drive UI with hand detection
T23.G6.04.06 ✅ Detect left/right hands
T23.G6.04.07 ✅ Track multiple hands
T23.G6.04.08 ⚪ Stop hand detection (minor: missing dependency on .04/.05)
```

### Smoothing Techniques (4 skills) ✅

```
T23.G6.06.01 ✅ Apply moving average
T23.G6.06.02 ✅ Use clamping to limit ranges
T23.G6.06.03 ✅ Implement debouncing
T23.G6.06.04 ✅ Create watchdog timers
```

### Detection Patterns (1 skill) ✅

```
T23.G6.07 ✅ Choose continuous vs event-driven
```

### Privacy & Ethics (1 skill) ✅

```
T23.G6.08 ✅ Add consent and privacy controls
```

### Body Detection (3 skills) 🔴 + 🟡

```
T23.G6.09.01.01 ✅ Set up 2D body detection
T23.G6.09.01.02 🔴 Understand body table structure
  └─ CRITICAL: Description incomplete (curl/dir only in limbs)

T23.G6.09.01.03 ✅ Read body keypoint positions
T23.G6.09.01.04 ✅ Stop body detection

T23.G6.09.02 🟡 Detect poses and trigger actions
  └─ TOO BROAD: Angle calc + multiple poses + actions
     NEEDS: Break into .01 (distance), .02 (arms up), .03 (squat), .04 (trigger)

T23.G6.09.03 ✅ Use 3D pose detection
```

### Face Detection (4 skills) ✅

```
T23.G6.10.01 ✅ Set up face detection
T23.G6.10.02.01 ✅ Understand face table structure
T23.G6.10.02.02 ✅ Read face position and tilt
T23.G6.10.02.03 ✅ Move sprite to follow face

[REMOVED] ❌ T23.G6.10.03 (expressions - not available)
[REMOVED] ❌ T23.G6.10.04 (age/gender - not available)
```

### NLP & Comparison (2 skills) ⚪

```
T23.G6.11 ⚪ Use NLP sentence analysis
  └─ Minor: Description vague about table output

T23.G6.12 ✅ Compare Azure vs Whisper
```

**Grade 6 Summary**:
- 27 good skills ✅
- 3 critical issues 🔴
- 3 skills need breakdown 🟡
- 2 missing scaffolds 🔵
- 2 minor issues ⚪

---

## Grade 7 (11 skills) - 8 ✅, 3 🟡

### Modality Selection (2 skills) ⚪

```
T23.G7.00 ⚪ Choose input modality for context
  └─ Minor: Violates X-2 rule (depends on G6 skills)
```

### Gesture Dictionary (2 skills) ✅

```
T23.G7.01 ✅ Define reusable gesture dictionary
T23.G7.01.02 ✅ Combine inputs with OR logic
```

### Multimodal Interactions (1 skill) ✅

```
T23.G7.02 ✅ Require multimodal confirmation (AND)
```

### Advanced Applications (2 skills) ✅

```
T23.G7.03 ✅ Score pose-based challenge
T23.G7.04 ✅ Monitor accuracy across users
```

### Fairness & Privacy (1 skill) ✅

```
T23.G7.05 ✅ Implement fairness safeguards
```

### Calibration & Optimization (3 skills) 🟡

```
T23.G7.06 🟡 Build calibration wizard
  └─ TOO BROAD: Multiple sensors, multiple steps
     NEEDS: Break into .01 (mic), .02 (camera), .03 (wizard UI)

T23.G7.07 ✅ Optimize perception performance
```

### Algorithm Selection (2 skills) ✅

```
T23.G7.08 ✅ Compare detection algorithms
T23.G7.09 ✅ Build error recovery systems
```

**Grade 7 Summary**:
- 8 good skills ✅
- 1 skill needs breakdown 🟡
- 1 minor dependency issue ⚪

---

## Grade 8 (22 skills) - 14 ✅, 5 🟡, 3 🔴, 1 🔵

### ML Foundations (3 skills) ✅ + 🔵

```
T23.G8.00 ✅ Understand supervised learning

[MISSING] 🔵 T23.G8.00.01 Understand how KNN finds neighbors (MISSING SCAFFOLD)

[WRONG PARENT] 🔴 T23.G8.01.02 → Should be T23.G8.00.01
  Currently: Practice KNN with numeric data

[WRONG PARENT] 🔴 T23.G8.01.03 → Should be T23.G8.00.02
  Currently: Split train/test data
```

### Accessibility & Modes (1 skill) ✅

```
T23.G8.01 ✅ Offer interchangeable input modes
```

### Data Collection & Training (4 skills) 🟡

```
T23.G8.02.01 🟡 Create data collection UI
  └─ TOO BROAD: Table design + UI + workflow
     NEEDS: Break into .01 (table), .02 (UI), .03 (workflow)

T23.G8.02.02 ✅ Train KNN classifier
T23.G8.02.03 ✅ Deploy trained classifier
```

### Multi-User & Evaluation (2 skills) 🔴 + 🟡

```
T23.G8.03 🟡 Multi-user cooperative simulation
  └─ TOO BROAD: Design + parallel + logging
     NEEDS: Break into .01 (design), .02 (parallel), .03 (logging)

[WRONG PARENT] 🔴 T23.G8.03.01 → Should come BEFORE G8.03
  Currently: Evaluate classifier performance (confusion matrix)
  This is evaluation, should be in sequence with G8.02.03
```

### Privacy & Impact (2 skills) ✅

```
T23.G8.04 ✅ Publish privacy and deployment plan

T23.G8.04.01 ✅ Experiment with K values in KNN
```

### Societal Impact & Feature Engineering (2 skills) ✅

```
T23.G8.05 ✅ Evaluate societal impacts

T23.G8.05.01 ✅ Apply feature engineering
```

### Neural Networks (5 skills) 🟡 + 🔵

```
T23.G8.06 ✅ Intro to neural networks vs KNN

T23.G8.07 ✅ Practice pre-trained NN models

T23.G8.08 🟡 Build custom NN for gestures
  └─ TOO BROAD: Architecture + training + comparison
     NEEDS: Break into .01 (architecture), .02 (training), .03 (comparison)

[MISSING] 🔵 T23.G8.08.04 Evaluate NN performance (MISSING SCAFFOLD)

T23.G8.09 ✅ Save and load NN models
```

### Advanced NLP (2 skills) ✅

```
T23.G8.10 ✅ Use semantic search for intents
T23.G8.11 ✅ Implement content moderation
```

### ML Workflow (3 skills) 🟡

```
T23.G8.12.01 ✅ Define ML problem and metrics
T23.G8.12.02 ✅ Plan data collection strategy

T23.G8.12.03 🟡 Document ML workflow
  └─ STILL BROAD: All 7 stages in one skill
     NEEDS: Break into .03.01 (training docs), .03.02 (deployment docs)
```

**Grade 8 Summary**:
- 14 good skills ✅
- 5 skills need breakdown 🟡
- 3 critical numbering issues 🔴
- 2 missing scaffolds 🔵

---

## Overall Summary

### By Status:
```
✅ Good Skills:         62 / 92  (67%)
🟡 Need Breakdown:       9 / 92  (10%)
🔴 Critical Issues:      6 / 92  (7%)
🔵 Missing Skills:       5       (scaffolding gaps)
⚪ Minor Issues:         5 / 92  (5%)
```

### By Grade:
```
GK: ✅✅✅ (100% good)
G1: ✅✅✅ (100% good)
G2: ✅✅✅ (100% good)
G3: ✅✅✅ (100% good)
G4: ✅✅✅ (100% good)
G5: ✅✅✅✅ ⚪⚪⚪ + 🔵 (57% good)
G6: ✅✅✅✅✅✅✅✅✅✅ (27/37) + 🟡🟡🟡 + 🔴🔴🔴 + 🔵🔵 (73% good)
G7: ✅✅✅✅✅✅✅✅ + 🟡 + ⚪ (80% good)
G8: ✅✅✅✅✅✅✅✅✅✅✅✅✅✅ (14/22) + 🟡🟡🟡🟡🟡 + 🔴🔴🔴 + 🔵🔵 (64% good)
```

### Critical Issues (Must Fix):
1. **G8.01.02** → Renumber to G8.00.01
2. **G8.01.03** → Renumber to G8.00.02
3. **G8.03.01** → Renumber to proper sequence
4. **G6.04.02.01** → Fix hand table description
5. **G6.09.01.02** → Fix body table description
6. **G6.11** → Clarify NLP output

### High Priority (Should Fix):
7. **G6.04.04** → Break into 4 sub-skills
8. **G6.09.02** → Break into 4 sub-skills
9. **G6.03.01** → Break into 3 sub-skills
10. Add 5 missing scaffolding skills

### Medium Priority (Nice to Have):
11. Break down remaining 6 broad skills
12. Fix dependency issues (X-2 rule, duplicates)
13. Add hands-on to G5 skills

---

## Progress Tracking

### Already Completed ✅
- [x] Removed unavailable features (expressions, demographics)
- [x] Broke down T23.G5.05 → 3 sub-skills
- [x] Broke down T23.G6.04.02 → 3 sub-skills
- [x] Broke down T23.G6.09.01 → 4 sub-skills
- [x] Broke down T23.G6.10.02 → 3 sub-skills
- [x] Broke down T23.G8.12 → 3 sub-skills
- [x] Added T23.G6.04.08 (stop hand detection)
- [x] Improved 72 → 92 skills (+28%)

### Remaining Work
- [ ] Fix 6 critical issues (structure & descriptions)
- [ ] Add 5 missing scaffolding skills
- [ ] Break down 9 overly broad skills → 30+ sub-skills
- [ ] Fix 5 dependency/minor issues
- [ ] Add hands-on to 3 G5 skills

**Completion**: 70% → Target: 95%+
