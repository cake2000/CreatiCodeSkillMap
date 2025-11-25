# T23 AI Perception - Fix Checklist

**Use this document to track progress as you fix issues.**

---

## 🚨 PHASE 1: CRITICAL FIXES (6-8 hours)

### Structural Numbering Issues

- [ ] **ISSUE 1.1**: Renumber T23.G8.01.02 → T23.G8.00.01
  - Skill: Practice KNN classification with simple numeric data
  - Current parent: G8.01 (input modes) - WRONG
  - New parent: G8.00 (supervised learning) - CORRECT
  - Update dependencies in other skills that reference this

- [ ] **ISSUE 1.2**: Renumber T23.G8.01.03 → T23.G8.00.02
  - Skill: Split collected data into training and test sets
  - Current parent: G8.01 (input modes) - WRONG
  - New parent: G8.00 (supervised learning) - CORRECT
  - Update dependencies in other skills that reference this

- [ ] **ISSUE 1.3**: Renumber T23.G8.03.01 → T23.G8.02.04 or similar
  - Skill: Evaluate classifier performance using confusion matrices
  - Current parent: G8.03 (multi-user simulation) - WRONG
  - Should come: After G8.02.03 (deploy classifier) - CORRECT
  - This is part of the KNN workflow, not multi-user

### Core API Description Fixes

- [ ] **ISSUE 2.1**: Fix T23.G6.04.02.01 description
  - Current: Mentions hand table structure but doesn't specify curl/dir location
  - **ADD TO DESCRIPTION**:
    ```
    "Students understand that curl (0-180°) and dir (0-360°) are ONLY available
    in finger summary rows (rows 1-5). Rows 6-26 (2D landmarks) contain only
    [hand, part, x, y]. Rows 27-47 (3D landmarks) contain [hand, part, x, y, z].
    Curl and dir are NOT present in landmark rows."
    ```

- [ ] **ISSUE 2.2**: Fix T23.G6.09.01.02 description
  - Current: Mentions body table structure but doesn't specify curl/dir location
  - **ADD TO DESCRIPTION**:
    ```
    "Students understand that curl and dir are ONLY available for limb measurement
    rows (left_arm, right_arm, left_leg, right_leg - 4 rows total). Individual
    keypoint rows (nose, eyes, shoulders, etc. - 17 rows) contain only
    [id, part, x, y]. Curl and dir are NOT present in keypoint rows."
    ```

- [ ] **ISSUE 2.3**: Fix T23.G6.11 description
  - Current: Over-promises NLP capabilities
  - **ACTION**: Verify what `analyze sentence` actually returns
  - **UPDATE TO**:
    ```
    "Students use `analyze sentence [SENTENCE] and write into table [TABLENAME v]`
    to analyze sentence structure. They explore the table output to understand
    what linguistic information is provided (word tokens, part-of-speech tags,
    dependencies, or other features). They read table values to extract key
    information from sentences and implement simple text parsing applications."
    ```

### Dependency Fixes

- [ ] **ISSUE 3.1**: Remove duplicate dependency from T23.G6.01.01
  - Current: Lists T09.G5.01 twice (different skill names)
  - **ACTION**: Check which T09.G5.01 is correct, keep one, remove duplicate

- [ ] **ISSUE 3.2**: Fix T23.G7.00 dependencies (X-2 violation)
  - Current: Depends on T23.G6.03.01, T23.G6.04.05, T23.G6.09.02 (all G6)
  - **CHANGE TO**:
    - T23.G5.02 (explain mis-hear/mis-see)
    - T23.G5.05.03 (workflow patterns)
  - **REMOVE**: All G6 dependencies

- [ ] **ISSUE 3.3**: Add missing dependency to T23.G6.04.08
  - Current: Only depends on T23.G6.04.02.03
  - **ADD**: T23.G6.04.05 (drive UI with hand detection) or T23.G6.04.04 (recognize gestures)
  - Rationale: Should use hand detection before stopping it

---

## 🎯 PHASE 2: ADD SCAFFOLDING (4-6 hours)

### Missing Skill 1: Speech Workflow Code Reading

- [ ] **ADD**: T23.G5.05.04
  - **Skill**: Trace speech recognition workflow in example code
  - **Description**:
    ```
    Students examine annotated code examples showing speech recognition workflow:
    start detection → speak → wait → end → read text. They match each code
    block to workflow steps (start, end, read, display) and identify what each
    block does. They trace through the code with a teacher to understand the
    sequence. Picture-based code reading with no hands-on coding yet. Final
    preparation before G6 implementation.
    ```
  - **Dependencies**: T23.G5.05.03
  - **Grade**: 5

### Missing Skill 2: Single Threshold Gesture

- [ ] **ADD**: T23.G6.04.02.04
  - **Skill**: Detect single threshold-based gesture
  - **Description**:
    ```
    Students implement ONE simple gesture using a single threshold check:
    "finger extended" if curl > 150, "finger curled" if curl < 90. They use
    a simple if-block to check the condition for one finger (e.g., index finger)
    and display "extended" or "curled" result. Focus on understanding how threshold
    comparisons work with one concrete example before combining multiple conditions
    for complex gestures.
    ```
  - **Dependencies**: T23.G6.04.02.03
  - **Grade**: 6

### Missing Skill 3: Empty Speech Detection

- [ ] **ADD**: T23.G6.01.03.01
  - **Skill**: Detect when speech recognition returns empty result
  - **Description**:
    ```
    Students check if `text from speech` reporter returns empty text (no speech
    detected) using an if-block: "if text from speech = '' then say 'No speech
    detected'". They implement this simple error detection before adding complex
    retry logic. They understand common causes: speaking too quietly, too much
    background noise, not speaking close enough to microphone.
    ```
  - **Dependencies**: T23.G6.01.03
  - **Grade**: 6

### Missing Skill 4: KNN Conceptual Understanding

- [ ] **ADD**: T23.G8.00.01
  - **Skill**: Understand how KNN finds similar examples
  - **Description**:
    ```
    Students examine visual diagrams showing how K-Nearest Neighbors classification
    works: given a new data point, measure distance to all training examples,
    find the K closest examples, use majority vote among those K neighbors to
    predict the class. They practice with paper-based activity: plot data points
    on graph paper, measure distances with ruler, identify 3 nearest neighbors,
    predict class by majority vote. Conceptual understanding before coding.
    ```
  - **Dependencies**: T23.G8.00
  - **Grade**: 8

### Missing Skill 5: Neural Network Evaluation

- [ ] **ADD**: T23.G8.08.04
  - **Skill**: Evaluate neural network performance on test data
  - **Description**:
    ```
    Students test their trained neural network on reserved test data and calculate
    accuracy (correct predictions / total predictions). They compare accuracy to
    target metrics (e.g., 90% accuracy goal) and identify when the network needs
    more training vs when it's ready to deploy. They understand that high training
    accuracy but low test accuracy indicates overfitting. Prepares for model
    persistence (G8.09) by ensuring quality before saving.
    ```
  - **Dependencies**: T23.G8.08.03 (compare NN vs KNN)
  - **Grade**: 8

---

## 📦 PHASE 3: BREAK DOWN TOP 3 (6-8 hours)

### Breakdown 1: Gesture Recognition (T23.G6.04.04)

- [ ] **SPLIT**: T23.G6.04.04 → T23.G6.04.04.01-.04

- [ ] **CREATE**: T23.G6.04.04.01 - Detect fist gesture
  - Focus: ONE gesture (all fingers curl < 90)
  - Simple AND logic: if finger1 < 90 AND finger2 < 90...
  - Display "fist" or "not fist"

- [ ] **CREATE**: T23.G6.04.04.02 - Detect open hand gesture
  - Focus: ONE gesture (all fingers curl > 150)
  - Opposite threshold from fist
  - Understanding threshold direction

- [ ] **CREATE**: T23.G6.04.04.03 - Detect pointing gesture
  - Focus: Compound conditions (index > 170 AND others < 90)
  - Multiple finger checks with AND
  - More complex logic than single gesture

- [ ] **CREATE**: T23.G6.04.04.04 - Build multi-gesture system
  - Focus: Combining checks with if-else
  - State management (which gesture active)
  - Display logic for multiple options

- [ ] **UPDATE**: All skills that depend on T23.G6.04.04
  - Change to depend on T23.G6.04.04.04 (final multi-gesture)

### Breakdown 2: Pose Detection (T23.G6.09.02)

- [ ] **SPLIT**: T23.G6.09.02 → T23.G6.09.02.01-.04

- [ ] **CREATE**: T23.G6.09.02.01 - Calculate distance between keypoints
  - Focus: Reading two keypoints, computing distance
  - Math: distance = sqrt((x2-x1)^2 + (y2-y1)^2) or simple |y2-y1|
  - Understanding coordinate math

- [ ] **CREATE**: T23.G6.09.02.02 - Detect "arms up" pose
  - Focus: ONE pose (wrists above shoulders)
  - Simple y-coordinate comparison: wrist.y < shoulder.y
  - Display "arms up" or "arms down"

- [ ] **CREATE**: T23.G6.09.02.03 - Detect "squat" pose
  - Focus: ONE pose (knees below hips)
  - Y-coordinate comparison: knee.y > hip.y
  - Understanding vertical position

- [ ] **CREATE**: T23.G6.09.02.04 - Trigger actions on pose
  - Focus: Event-driven programming
  - When pose detected → trigger action
  - State management across pose changes

- [ ] **UPDATE**: All skills that depend on T23.G6.09.02
  - Change to depend on T23.G6.09.02.04 (final action triggering)

### Breakdown 3: Voice Chatbot (T23.G6.03.01)

- [ ] **SPLIT**: T23.G6.03.01 → T23.G6.03.01.01-.03

- [ ] **CREATE**: T23.G6.03.01.01 - Connect speech to ChatGPT
  - Focus: Speech recognition → text variable → ChatGPT request
  - Data flow: `text from speech` → variable → GPT prompt
  - Understanding the pipeline

- [ ] **CREATE**: T23.G6.03.01.02 - Connect ChatGPT to TTS
  - Focus: ChatGPT response → text variable → TTS
  - Data flow: GPT result → variable → `say` block
  - Voice parameter selection

- [ ] **CREATE**: T23.G6.03.01.03 - Implement turn-taking
  - Focus: State management (listen → process → speak → repeat)
  - Timing: wait for TTS to complete before listening again
  - Preventing overlapping speech

- [ ] **UPDATE**: All skills that depend on T23.G6.03.01
  - Change to depend on T23.G6.03.01.03 (final turn-taking)

---

## 🔧 PHASE 4: ADDITIONAL REFINEMENT (8-12 hours, optional)

### More Breakdowns

- [ ] Break T23.G8.02.01 (data collection UI) → 3 sub-skills
- [ ] Break T23.G7.06 (calibration wizard) → 3 sub-skills
- [ ] Break T23.G8.03 (multi-user simulation) → 3 sub-skills
- [ ] Break T23.G8.08 (custom NN) → 3 sub-skills
- [ ] Break T23.G8.12.03 (ML workflow docs) → 2 sub-skills
- [ ] Renumber T23.G8.03.01 properly (currently wrong parent)

### Grade-Appropriateness

- [ ] **UPDATE**: T23.G5.05.01 - Add hands-on component
  - Change from: "match detection types using picture cards"
  - Change to: "Use provided example projects in CreatiCode to observe different detection types in action. They run hand detection, body detection, and face detection demos and identify what data each provides by viewing the output tables."

- [ ] **UPDATE**: T23.G5.05.02 - Add hands-on component
  - Change from: "examine annotated table examples"
  - Change to: "Read sample table data in CreatiCode from saved hand/body/face detection results. They navigate tables to find specific data (which row has index finger curl? which column has x-coordinate?) using table blocks."

- [ ] **UPDATE**: T23.G5.05.03 - Add hands-on component
  - Change from: "match API blocks to workflow steps using diagrams"
  - Change to: "Trace through example code in CreatiCode (remix provided projects) showing perception API workflows. They identify start, read, process, and stop blocks in working code and observe what each does."

### Dependency Review

- [ ] Review all G6 dependencies on G5 skills (X-2 rule)
  - If strict X-2: Change to G4 dependencies
  - If foundational exception: Keep G5 dependencies
  - Document decision

- [ ] Verify all skill IDs in dependencies exist
- [ ] Check for circular dependencies
- [ ] Ensure linear progression within grade

---

## ✅ COMPLETION CRITERIA

### Phase 1 Complete When:
- [ ] No numbering conflicts (G8 KNN skills properly parented)
- [ ] All table structure descriptions are accurate and complete
- [ ] All dependencies are valid (no duplicates, no obvious X-2 violations)
- [ ] No critical blockers remain

### Phase 2 Complete When:
- [ ] 5 new scaffolding skills added and integrated
- [ ] All dependencies updated to include new skills
- [ ] No obvious progression gaps remain

### Phase 3 Complete When:
- [ ] Top 3 broad skills broken into 11 sub-skills total
- [ ] Each sub-skill has ONE clear learning objective
- [ ] All dependencies updated for sub-skills
- [ ] Numbering is consistent

### Phase 4 Complete When:
- [ ] All remaining broad skills broken down
- [ ] G5 skills have hands-on components
- [ ] All dependency issues resolved
- [ ] Comprehensive quality check passed

---

## TESTING CHECKLIST

After making changes, verify:

- [ ] Every skill ID is unique
- [ ] Every dependency references an existing skill ID
- [ ] Every skill has a description
- [ ] Every G6+ skill has dependencies
- [ ] Grade separators are in place ("---" and "## GRADE X SKILLS")
- [ ] Format is consistent with other topics
- [ ] No skills reference unavailable features (expressions, age/gender)
- [ ] Table structure descriptions match actual API output
- [ ] Skills progress from simple to complex within each grade
- [ ] GK-G2 are picture-based, G3+ are hands-on

---

## PROGRESS TRACKING

### Current Status
- **Original**: 72 skills
- **After first optimization**: 92 skills
- **After this fix (target)**: 108-130 skills (depending on phase)

### Issues Remaining
- **Phase 1**: 6 critical issues
- **Phase 2**: 5 scaffolding gaps
- **Phase 3**: 3 major breakdowns (→11 sub-skills)
- **Phase 4**: 6 additional breakdowns + refinements (→23 sub-skills)

**Total**: 26 issues → 108-130 skills when complete

---

## NOTES

### X-2 Rule Interpretation Needed
**Question**: Does X-2 rule apply to foundational skills (T05-T11, T15)?

**Option A** (Strict): All cross-topic dependencies must be 2+ grades earlier
- G6 skills can only depend on G4 or earlier from other topics
- Need to change many G6 dependencies from G5 to G4

**Option B** (Foundational Exception): X-2 applies to advanced skills, not foundations
- G6 skills can depend on G5 foundational skills (T05-T11)
- Current dependencies are OK
- X-2 applies mainly to cross-topic advanced dependencies (e.g., T23 → T22)

**Decision needed before Phase 1 completion**

### NLP Block Output Format Needed
**Question**: What does `analyze sentence` actually return in the table?

**Need to verify**:
- What are the column names?
- What are the row contents?
- Does it provide POS tags? Dependencies? Tokens?

**Action**: Test the block or check documentation before finalizing T23.G6.11 description

---

**Last Updated**: 2025-11-25
**Status**: Ready for implementation
**Next**: Start Phase 1, Issue 1.1 (renumber G8.01.02)
