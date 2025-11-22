# T23 New Skills - Quick Reference Guide

## 8 CRITICAL New Skills (Priority 1-2)

---

## T23.G6.01B: Use continuous speech recognition for real-time input

**Grade:** 6
**Category:** Speech Recognition - Continuous Mode
**Position:** After G6.01, before G6.02

### Skill Description
Students learn to use `start continuous speech recognition in [language] into list [list]` to capture ongoing speech in real-time. They understand the difference between single-shot (start/end) and continuous modes. They read the growing list of recognized phrases and display them as a live transcript. They handle the continuously growing list by limiting its size or processing new entries.

### Block Used
```
start continuous speech recognition in [English (United States) v] into list [transcript v]
stop speech recognition
```

### Key Concepts
- Continuous vs single-shot recognition
- Results go into a LIST (not reporter block)
- List grows continuously until stopped
- Need to manage list size (delete old items)

### Example Code
```scratch
when green flag clicked
delete all of [transcript v]
say [Say something! I'm listening...] for (2) secs
start continuous speech recognition in [English (United States) v] into list [transcript v]

forever
  if <(length of [transcript v]) > [0]> then
    set [latest v] to (item (length of [transcript v]) of [transcript v])
    say (latest) for (1) secs

    // Keep list size manageable
    if <(length of [transcript v]) > [20]> then
      delete (1) of [transcript v]
    end
  end
end

when [space v] key pressed
stop speech recognition
say [Stopped listening] for (2) secs
```

### Dependencies
- T23.G6.01: Use speech recognition blocks to capture voice input
- T10.G3.01: Create and use a list

### Leads To
- T23.G6.02: Map speech commands to UI widgets
- T23.G6.03: Build a two-way voice chatbot loop

### CSTA
AP-13-01, AP-16-02

---

## T23.G6.04B: Read hand detection finger directions (not just curl)

**Grade:** 6
**Category:** Hand Detection - Direction
**Position:** After G6.04

### Skill Description
Students learn to read both `curl` (angle) and `dir` (direction: Up/Down/Left/Right) columns from the hand detection table. They understand that curl tells if fingers are bent, while direction tells where they're pointing. They identify gestures using both: thumbs-up (thumb Up, others curled), pointing (index Up, others curled), peace sign (index+middle Up, others curled).

### Block Used
```
run hand detection table [hand_data v] debug [yes v] show video [no v]
// Read from table columns: part, x, y, curl, dir
```

### Key Concepts
- Curl = how bent (0-180 degrees)
- Dir = which way pointing (Up/Down/Left/Right)
- Both needed for accurate gesture recognition
- Table has 5 rows per hand (thumb, index, middle, ring, pinky)

### Example Code
```scratch
when green flag clicked
run hand detection table [hand_data v] debug [yes v] show video [no v]

forever
  // Check for thumbs up: thumb Up + thumb curl > 120
  set [thumb_curl v] to (value in table [hand_data v] column [curl] row where [part] = [thumb])
  set [thumb_dir v] to (value in table [hand_data v] column [dir] row where [part] = [thumb])

  if <<(thumb_dir) = [Up]> and <(thumb_curl) > [120]>> then
    say [Thumbs up detected!] for (1) secs
  end

  // Check for pointing: index Up + index curl > 150, others curled
  set [index_curl v] to (value in table [hand_data v] column [curl] row where [part] = [index])
  set [index_dir v] to (value in table [hand_data v] column [dir] row where [part] = [index])
  set [middle_curl v] to (value in table [hand_data v] column [curl] row where [part] = [middle])

  if <<<(index_dir) = [Up]> and <(index_curl) > [150]>> and <(middle_curl) < [90]>> then
    say [Pointing detected!] for (1) secs
  end
end
```

### Gesture Recognition Patterns
| Gesture | Thumb | Index | Middle | Ring | Pinky |
|---------|-------|-------|--------|------|-------|
| Thumbs Up | Up, >120° | Any curled | Any curled | Any curled | Any curled |
| Pointing | Any | Up, >150° | <90° | <90° | <90° |
| Peace Sign | Curled | Up, >150° | Up, >150° | <90° | <90° |
| Open Hand | Up/Out, >150° | Up, >150° | Up, >150° | Up, >150° | Up, >150° |
| Fist | <90° | <90° | <90° | <90° | <90° |

### Dependencies
- T23.G6.04: Use hand detection blocks to track finger curl angles
- T10.G4.01: Read a cell value from a table

### Leads To
- T23.G7.01: Define a reusable gesture dictionary

### CSTA
AP-13-01, DA-07-01

---

## T23.G6.08B: Compare single-person vs multi-person body tracking modes

**Grade:** 6
**Category:** 2D Body Tracking - Modes
**Position:** After G6.08

### Skill Description
Students learn when to use single-person mode (faster, more accurate, one player games) vs multi-person mode (slower, tracks multiple people, multiplayer games). They test both modes and observe performance differences. They understand that single-person mode is optimized and should be preferred when only tracking one person. They make conscious design choices based on their app's needs.

### Block Used
```
run 2D body part recognition single person [yes v] table [body_data v] debug [yes v]
run 2D body part recognition single person [no v] table [body_data v] debug [yes v]
```

### Key Concepts
- Single-person mode: Optimized for one person
  - Faster processing
  - More accurate tracking
  - Lower CPU usage
- Multi-person mode: Tracks multiple people
  - Slower processing
  - Can track 2+ people simultaneously
  - Higher CPU usage
  - Each person gets separate rows in table

### Comparison Table
| Aspect | Single-Person Mode | Multi-Person Mode |
|--------|-------------------|-------------------|
| Speed | Fast (~30-60 FPS) | Slower (~15-30 FPS) |
| Accuracy | High | Medium |
| CPU Usage | Low | High |
| Max People | 1 | 2-6 (varies) |
| Use Case | Solo fitness, single-player games | Multiplayer games, group activities |

### Example Code
```scratch
// Single-person mode (recommended for most apps)
when green flag clicked
say [Single-person mode - faster!] for (2) secs
run 2D body part recognition single person [yes v] table [body_single v] debug [yes v]

forever
  set [nose_y v] to (value in table [body_single v] column [y] row where [part] = [nose])
  go to x: (0) y: (nose_y)
end

// Multi-person mode (for multiplayer)
when [m v] key pressed
say [Multi-person mode - can track 2+ people] for (2) secs
run 2D body part recognition single person [no v] table [body_multi v] debug [yes v]

forever
  // Each person's landmarks are grouped in table
  // Row 1-17: Person 1's 17 body parts
  // Row 18-34: Person 2's 17 body parts
  set [p1_nose_y v] to (value in table [body_multi v] column [y] row [1])
  set [p2_nose_y v] to (value in table [body_multi v] column [y] row [18])

  say (join [Person 1: ] (join (p1_nose_y) (join [ | Person 2: ] (p2_nose_y)))) for (1) secs
end
```

### Decision Guide
**Use Single-Person Mode When:**
- Tracking one player only
- Need high accuracy (fitness tracking, pose games)
- Need fast performance (real-time games)
- Device has limited CPU

**Use Multi-Person Mode When:**
- Tracking 2+ players simultaneously
- Building multiplayer games
- Comparing poses between players
- Group activities (dance-off, fitness class)

### Dependencies
- T23.G6.08: Use body pose detection blocks to track body positions
- T08.G4.01: Use a conditional to make a multi-way decision

### Leads To
- T23.G7.03: Score a pose-based challenge with coaching tips
- T19.G8.07: Optimize network traffic in multiplayer games

### CSTA
AP-13-01, AP-18-01 (efficiency considerations)

---

## T23.G6.10: Use 3D pose detection for depth-aware tracking

**Grade:** 6
**Category:** 3D Pose Detection
**Position:** After G6.08B

### Skill Description
Students learn to use `run 3D pose detection debug [ ] table [pose_3d v]` to track 33 body landmarks with x, y, and z coordinates. They understand that z represents depth (distance from camera). They read the pose_3d table and display 3D positions. They compare 2D vs 3D tracking and understand when depth information is valuable (AR apps, 3D games, depth-based interactions).

### Block Used
```
run 3D pose detection debug [yes v] table [pose_3d v]
// Table columns: part (33 landmarks), x, y, z, visibility
```

### Key Concepts
- 33 landmarks (vs 17 in 2D mode)
- z-axis = depth (distance from camera)
  - Negative z = closer to camera
  - Positive z = farther from camera
- All coordinates relative to camera center
- Visibility score (0-1) for each landmark

### 3D vs 2D Comparison
| Feature | 2D Body Tracking | 3D Pose Detection |
|---------|------------------|-------------------|
| Landmarks | 17 | 33 |
| Coordinates | x, y | x, y, z |
| Depth Info | ❌ No | ✅ Yes |
| Speed | Faster | Slower |
| Use Case | 2D games, fitness | 3D games, AR, depth-based |

### Example Code
```scratch
when green flag clicked
say [Starting 3D pose detection] for (2) secs
run 3D pose detection debug [yes v] table [pose_3d v]

forever
  // Get 3D position of right hand
  set [hand_x v] to (value in table [pose_3d v] column [x] row where [part] = [right wrist])
  set [hand_y v] to (value in table [pose_3d v] column [y] row where [part] = [right wrist])
  set [hand_z v] to (value in table [pose_3d v] column [z] row where [part] = [right wrist])

  // Move sprite to match hand position
  go to x: (hand_x * 2) y: (hand_y * 2)

  // Use z for size (closer = bigger)
  set size to ((100) - (hand_z * 50)) %

  // Display depth info
  say (join [Depth (z): ] (round (hand_z))) for (0.5) secs
end
```

### 33 Landmarks (Key Points)
- **Face:** nose, left/right eye (inner, outer), left/right ear
- **Upper Body:** shoulders, elbows, wrists
- **Hands:** thumb, index, middle, ring, pinky tips
- **Lower Body:** hips, knees, ankles
- **Feet:** heel, foot index

### Use Cases for 3D Pose
1. **3D Avatar Control:** Map real body to 3D character
2. **AR Interactions:** Place objects in 3D space relative to body
3. **Depth-Based Games:** Reach forward/backward to interact
4. **Gesture Volume:** Detect gestures in 3D space (not just 2D plane)
5. **Perspective Games:** Use depth to trigger different zones

### Dependencies
- T23.G6.08B: Compare single-person vs multi-person body tracking modes
- T14.G6.01: Understand 3D coordinate systems

### Leads To
- T23.G7.03: Score a pose-based challenge with coaching tips
- T14.G8.*: 3D avatar control with pose data

### CSTA
AP-13-01, AP-16-02

---

## T23.G6.11: Use AR face camera for 3D face mesh tracking

**Grade:** 6
**Category:** AR Face Tracking
**Position:** After G6.09 (face detection)

### Skill Description
Students learn to use `run AR face camera` to enable 3D face mesh tracking. They understand this is different from basic face detection - it provides a detailed 3D mesh of the face for AR effects. They access face position and rotation data. They understand that AR face camera is more resource-intensive than basic face detection. They use it to attach 3D objects to faces (AR glasses, masks, hats).

### Block Used
```
run AR face camera
stop AR face camera
// Provides real-time 3D face mesh with 468 landmarks
```

### Key Concepts
- 468 face mesh points (vs ~6 in basic face detection)
- Real-time 3D face tracking
- Includes face rotation (pitch, yaw, roll)
- More CPU-intensive than basic face detection
- Used for AR effects and filters

### AR Face vs Basic Face Detection
| Feature | Basic Face Detection | AR Face Camera |
|---------|---------------------|----------------|
| Landmarks | ~6 key points | 468 mesh points |
| 3D Info | ❌ No | ✅ Yes (rotation, depth) |
| Speed | Fast | Slower |
| CPU Usage | Low | High |
| Use Case | Detect faces, basic tracking | AR filters, 3D effects |

### Example Code
```scratch
when green flag clicked
say [Starting AR face camera] for (2) secs
run AR face camera

// Create 3D glasses sprite
create 3D sprite named [glasses] as [model]
load 3D model [glasses.glb] for sprite [glasses]

forever
  if <face detected> then
    // Get face position and rotation
    set [face_x v] to (AR face x)
    set [face_y v] to (AR face y)
    set [face_z v] to (AR face z)
    set [face_yaw v] to (AR face yaw)
    set [face_pitch v] to (AR face pitch)
    set [face_roll v] to (AR face roll)

    // Position 3D glasses on face
    go to 3D x: (face_x) y: (face_y + 20) z: (face_z)
    set rotation style [3D v]
    set 3D rotation yaw: (face_yaw) pitch: (face_pitch) roll: (face_roll)
  else
    say [No face detected] for (0.5) secs
  end
end

when [space v] key pressed
stop AR face camera
say [Stopped AR camera] for (2) secs
```

### AR Face Effects Examples
1. **3D Glasses:** Position on face, follow rotation
2. **Face Mask:** Attach to face mesh
3. **Party Hat:** Position above head
4. **Face Paint:** Project texture onto face mesh
5. **Beard/Mustache:** Position below nose, follow mouth

### Performance Tips
- Use AR face camera ONLY when needed
- Stop AR camera when not in use
- Don't run AR face + multiple other perception features simultaneously
- Test on target device (AR face is resource-intensive)

### Dependencies
- T23.G6.09: Use face detection blocks to locate faces and landmarks
- T14.G6.01: Understand 3D coordinate systems

### Leads To
- T14.G8.*: AR face effects with 3D models
- T23.G7.*: Multimodal systems with face tracking

### CSTA
AP-13-01, IC-20-01 (AR technology)

---

## T23.G7.00A: Understand when to use each perception modality

**Grade:** 7
**Category:** Multimodal - Foundation
**Position:** Beginning of Grade 7, before G7.01

### Skill Description
Students learn to choose the appropriate perception modality for different tasks. They understand trade-offs: speech (hands-free but noisy), hand detection (precise but requires visible hands), pose detection (full-body but needs space), face detection (identity/emotion but privacy concerns). They create decision charts matching use cases to modalities. They explain why multimodal (combining multiple) is sometimes necessary.

### Key Concepts
- Each modality has strengths and weaknesses
- Choose based on: use case, environment, privacy, performance
- Multimodal = combining multiple modalities
- Accessibility requires alternatives (don't rely on one sense)

### Modality Comparison

| Modality | Strengths | Weaknesses | Best For |
|----------|-----------|------------|----------|
| **Speech** | Hands-free, natural, fast input | Noisy environments, privacy, accents | Voice commands, dictation, accessibility |
| **Hand Detection** | Precise, intuitive gestures | Hands must be visible, limited range | Drawing, precise control, sign language |
| **2D Pose** | Full-body tracking, exercise | Needs space, whole body visible | Fitness, dance, full-body games |
| **3D Pose** | Depth info, 3D interactions | Slower, more CPU | 3D games, AR, depth-based |
| **Face Detection** | Identity, emotion, AR effects | Privacy concerns, face must be visible | AR filters, emotion detection, login |
| **AR Face** | Detailed mesh, AR effects | Very CPU-intensive | AR filters, face effects |

### Decision Chart

```
Use Case → Best Modality

ACCESSIBILITY & INCLUSION
- User can't use hands → Speech
- User can't speak → Hand/Pose
- User has low vision → Speech + audio feedback
- Multiple accessibility needs → MULTIMODAL (offer all)

GAME CONTROLS
- Menu navigation → Speech OR Hand OR Buttons
- Character movement → Pose (full-body) OR Hand (gestures)
- Quick actions → Hand (fast gestures)
- Confirmations → MULTIMODAL (voice + gesture for safety)

CREATIVE APPS
- Drawing/Painting → Hand (precise control)
- Music/Dance → Pose (full-body movement)
- Voice recording → Speech
- AR effects → Face/AR Face

SOCIAL/COMMUNICATION
- Video calls → Face (emotion detection)
- Sign language → Hand (detailed gestures)
- Voice chat → Speech
- AR social → AR Face (filters)

EDUCATION
- Language learning → Speech (pronunciation)
- Fitness tracking → Pose (body tracking)
- Interactive stories → Speech OR Hand
- Science simulations → Hand (manipulate objects)
```

### Multimodal Examples

**Example 1: Accessible Game Menu**
```
Primary: Speech ("Start game")
Fallback 1: Hand gesture (thumbs up)
Fallback 2: Face gesture (nod)
Fallback 3: Keyboard (Enter)
→ User can use ANY method
```

**Example 2: Safety-Critical Confirmation**
```
Primary: Voice command ("Confirm delete")
Secondary: Hand gesture (specific pattern)
→ BOTH required to prevent accidents
```

**Example 3: Fitness Coach App**
```
Primary: Pose detection (track exercise)
Secondary: Speech ("Start workout", "Pause")
Tertiary: Face detection (detect fatigue from expressions)
→ Each modality serves different purpose
```

### Exercise: Matching Use Cases

Students complete matching exercise:
1. Space shooter game controls → ?
2. Voice-controlled smart home → ?
3. Sign language learning app → ?
4. AR face filter app → ?
5. Accessible drawing app → ?

**Answers:**
1. Hand detection (precise aiming) OR Pose (body as controller)
2. Speech (hands-free commands)
3. Hand detection (detailed finger tracking)
4. AR Face Camera (3D face mesh)
5. MULTIMODAL: Hand (drawing) + Speech (commands) + Buttons (backup)

### Dependencies
- All G6 perception skills (T23.G6.01-11)
- T05.G5.01: Map user needs to features

### Leads To
- T23.G7.01: Define a reusable gesture dictionary
- T23.G7.02: Require multimodal confirmation (voice + gesture)

### CSTA
AP-13-01, IC-20-01, IC-20-03 (accessibility)

---

## T23.G8.00A: Understand KNN classifier training process

**Grade:** 8
**Category:** Machine Learning - KNN Foundation
**Position:** Before G8.02

### Skill Description
Students learn what "training" means for machine learning: collecting labeled examples, storing them in a table, and using them to create a classifier. They understand that more examples = better accuracy. They prepare a training dataset: collect gesture samples (5-10 examples per gesture), label each sample, store in a table with `label` column. They understand the table format required for KNN training.

### Key Concepts
- **Training:** Teaching the AI by showing examples
- **Label:** The correct answer (gesture name)
- **Features:** The measurements (curl angles, x/y positions)
- **Training Data:** Table of labeled examples
- More examples = better accuracy
- Need examples of ALL gestures you want to recognize

### Training Data Table Format

```
label       | feature1 | feature2 | feature3 | feature4 | feature5
------------|----------|----------|----------|----------|----------
"thumbs_up" | 45       | 120      | 90       | 80       | 75
"thumbs_up" | 48       | 115      | 95       | 85       | 78
"thumbs_up" | 50       | 118      | 92       | 82       | 76
"peace"     | 160      | 170      | 45       | 40       | 38
"peace"     | 165      | 175      | 48       | 42       | 40
"peace"     | 162      | 172      | 46       | 41       | 39
"fist"      | 30       | 25       | 28       | 32       | 30
"fist"      | 28       | 22       | 26       | 30       | 28
```

**Columns:**
- `label`: The gesture name (what you're trying to recognize)
- `feature1-5`: Measurements (e.g., thumb curl, index curl, middle curl, ring curl, pinky curl)

### Example Code: Collecting Training Data

```scratch
when green flag clicked
say [Let's collect training data for gestures!] for (3) secs

// Create empty training table
delete all rows of table [training_data v]
add column [label] to table [training_data v]
add column [thumb_curl] to table [training_data v]
add column [index_curl] to table [training_data v]
add column [middle_curl] to table [training_data v]
add column [ring_curl] to table [training_data v]
add column [pinky_curl] to table [training_data v]

// Start hand detection
run hand detection table [hand_data v] debug [yes v] show video [yes v]

say [Make a THUMBS UP gesture] for (3) secs
repeat (5) times
  say (join [Sample ] (join (counter) [ of 5])) for (1) secs

  // Read current hand data
  set [thumb_curl v] to (value in table [hand_data v] column [curl] row where [part] = [thumb])
  set [index_curl v] to (value in table [hand_data v] column [curl] row where [part] = [index])
  set [middle_curl v] to (value in table [hand_data v] column [curl] row where [part] = [middle])
  set [ring_curl v] to (value in table [hand_data v] column [curl] row where [part] = [ring])
  set [pinky_curl v] to (value in table [hand_data v] column [curl] row where [part] = [pinky])

  // Add to training table
  append to table [training_data v] values ["thumbs_up", (thumb_curl), (index_curl), (middle_curl), (ring_curl), (pinky_curl)]

  wait (0.5) secs
end

say [Now make a PEACE SIGN gesture] for (3) secs
repeat (5) times
  say (join [Sample ] (join (counter) [ of 5])) for (1) secs

  // Read current hand data
  set [thumb_curl v] to (value in table [hand_data v] column [curl] row where [part] = [thumb])
  set [index_curl v] to (value in table [hand_data v] column [curl] row where [part] = [index])
  set [middle_curl v] to (value in table [hand_data v] column [curl] row where [part] = [middle])
  set [ring_curl v] to (value in table [hand_data v] column [curl] row where [part] = [ring])
  set [pinky_curl v] to (value in table [hand_data v] column [curl] row where [part] = [pinky])

  // Add to training table
  append to table [training_data v] values ["peace", (thumb_curl), (index_curl), (middle_curl), (ring_curl), (pinky_curl)]

  wait (0.5) secs
end

say [Training data collected! Ready to create classifier.] for (3) secs
show table [training_data v]
```

### Best Practices for Training Data

**1. Quantity:**
- Minimum: 3-5 examples per gesture
- Recommended: 10-20 examples per gesture
- More examples = better accuracy

**2. Variety:**
- Collect examples with slight variations
- Different hand positions
- Different angles
- Different lighting
- Different people (if possible)

**3. Balance:**
- Collect SAME number of examples for each gesture
- If thumbs_up has 20 examples, peace should also have 20

**4. Quality:**
- Make sure gestures are clear and distinct
- Don't collect bad/unclear examples
- Label accurately

### Common Mistakes

❌ **Too Few Examples**
```
"thumbs_up": 2 examples → Classifier won't learn pattern
```
✅ **Solution:** Collect at least 5-10 examples

❌ **Unbalanced Dataset**
```
"thumbs_up": 20 examples
"peace": 3 examples → Classifier biased toward thumbs_up
```
✅ **Solution:** Equal examples for all gestures

❌ **Unlabeled or Mislabeled Data**
```
"thumbs_up", 120, 90, ... (correct)
"", 165, 172, ... (missing label - ERROR)
"peace", 30, 25, ... (this is actually a fist - ERROR)
```
✅ **Solution:** Double-check labels

### Dependencies
- T23.G7.01: Define a reusable gesture dictionary (manual classification)
- T10.G5.04: Read a cell value from a table
- T09.G5.05: Use the accumulator pattern to compute running totals (for collecting samples)

### Leads To
- T23.G8.02: Train and deploy a custom gesture classifier

### CSTA
AP-13-01, DA-08-01 (collect data for analysis)

---

## T23.G8.02B: Evaluate and tune KNN classifier accuracy

**Grade:** 8
**Category:** Machine Learning - KNN Tuning
**Position:** After G8.02

### Skill Description
Students test their trained KNN classifier with new samples and measure accuracy. They understand what K means (number of neighbors to check) and how it affects classification. They experiment with different K values (3, 5, 7) and observe accuracy changes. They identify which gestures are confused (misclassified) and add more training data for those. They document: K value chosen, accuracy percentage, which gestures work well vs poorly.

### Key Concepts
- **K:** Number of nearest neighbors to check (in K-Nearest-Neighbors)
- **Accuracy:** Percentage of correct predictions
- **Confusion:** When classifier mistakes one gesture for another
- **Tuning:** Adjusting parameters to improve performance
- **Testing:** Always test on NEW data (not training data)

### What is K?

KNN classifies by looking at the K nearest training examples:
- **K=1:** Look at 1 closest example → Fast but noisy
- **K=3:** Look at 3 closest examples, majority vote → Balanced
- **K=5:** Look at 5 closest examples → More stable
- **K=7+:** Look at 7+ closest examples → Very stable but slower

**Rule of thumb:** Start with K=3 or K=5

### Example Code: Testing and Tuning

```scratch
when green flag clicked
say [Testing KNN classifier accuracy] for (2) secs

// Load trained classifier (from previous skill)
create KNN number classifier from table [training_data v] K (3) named [gesture_classifier]

// Prepare test data (10 new samples not in training)
delete all rows of table [test_data v]
// ... collect 10 new gesture samples into test_data ...

// Test classifier
set [correct v] to [0]
set [total v] to [0]

repeat (number of rows in table [test_data v])
  set [total v] to ((total) + (1))

  // Get expected label (correct answer)
  set [expected v] to (value in table [test_data v] column [label] row (counter))

  // Get classifier prediction
  use KNN classifier [gesture_classifier] to predict label from table [test_data v] show neighbors [no v]
  set [predicted v] to (value in table [test_data v] column [predicted_label] row (counter))

  // Check if correct
  if <(predicted) = (expected)> then
    change [correct v] by (1)
    say (join [✓ Correct: ] (predicted)) for (0.5) secs
  else
    say (join [✗ Wrong: predicted ] (join (predicted) (join [ (should be ] (join (expected) [)])))) for (1) secs
  end
end

// Calculate accuracy
set [accuracy v] to (((correct) / (total)) * (100))
say (join [Accuracy: ] (join (round (accuracy)) [%])) for (3) secs

// Tuning: Try different K values
say [Now testing different K values...] for (2) secs

// Test K=1
create KNN number classifier from table [training_data v] K (1) named [gesture_k1]
test classifier [gesture_k1] → set [accuracy_k1 v]

// Test K=3
create KNN number classifier from table [training_data v] K (3) named [gesture_k3]
test classifier [gesture_k3] → set [accuracy_k3 v]

// Test K=5
create KNN number classifier from table [training_data v] K (5) named [gesture_k5]
test classifier [gesture_k5] → set [accuracy_k5 v]

// Test K=7
create KNN number classifier from table [training_data v] K (7) named [gesture_k7]
test classifier [gesture_k7] → set [accuracy_k7 v]

// Compare results
say (join [K=1: ] (join (accuracy_k1) [%])) for (2) secs
say (join [K=3: ] (join (accuracy_k3) [%])) for (2) secs
say (join [K=5: ] (join (accuracy_k5) [%])) for (2) secs
say (join [K=7: ] (join (accuracy_k7) [%])) for (2) secs

say (join [Best K value: ] (best_k)) for (3) secs
```

### Tuning Process (Step-by-Step)

**Step 1: Initial Training**
- Collect 10 examples per gesture
- Create classifier with K=5
- Test accuracy

**Step 2: Measure Baseline**
```
Gesture      | Correct | Total | Accuracy
-------------|---------|-------|----------
Thumbs Up    | 8       | 10    | 80%
Peace Sign   | 9       | 10    | 90%
Fist         | 6       | 10    | 60%  ← Needs work!
Open Hand    | 10      | 10    | 100%
-------------|---------|-------|----------
TOTAL        | 33      | 40    | 82.5%
```

**Step 3: Identify Problems**
- "Fist" is being confused with "Thumbs Up" (both have curled fingers)
- Need to collect more fist examples with varying curl angles

**Step 4: Improve Training Data**
- Add 10 more fist examples
- Add examples with different hand positions
- Re-train classifier

**Step 5: Test Different K Values**
```
K Value | Accuracy | Speed
--------|----------|-------
K=1     | 75%      | Fast
K=3     | 85%      | Medium
K=5     | 90%      | Medium  ← Best balance!
K=7     | 88%      | Slower
K=9     | 85%      | Slower
```

**Step 6: Choose Best K**
- K=5 gives best accuracy (90%)
- Deploy with K=5

### Common Tuning Patterns

**Pattern 1: Accuracy Improves with More K**
```
K=1: 70% → K=3: 80% → K=5: 85% → K=7: 87%
```
**Solution:** Use K=7 (more stable)

**Pattern 2: Accuracy Peaks Then Drops**
```
K=1: 75% → K=3: 85% → K=5: 90% → K=7: 85% → K=9: 80%
```
**Solution:** Use K=5 (optimal point)

**Pattern 3: Low Accuracy Regardless of K**
```
K=1: 50% → K=3: 52% → K=5: 55% → K=7: 53%
```
**Solution:** Problem with training data, not K. Collect more/better examples.

### Dependencies
- T23.G8.02: Train and deploy a custom gesture classifier
- T09.G6.01: Model real-world quantities using variables and formulas (calculate percentages)

### Leads To
- T23.G8.03: Fuse voice, pose, and UI widgets into cooperative simulation

### CSTA
AP-17-01 (systematically test and refine), DA-08-01

---

## Summary: Integration with Existing Skills

### New Skills Fit Into Grade 6-8 Progression:

**Grade 6 (add 5 skills):**
- G6.01 → **G6.01B (continuous speech)** → G6.02
- G6.04 → **G6.04B (hand direction)** → G6.05
- G6.08 → **G6.08B (single vs multi-person)** → **G6.10 (3D pose)** → G6.09 → **G6.11 (AR face)**

**Grade 7 (add 1 skill):**
- **G7.00A (modality selection)** → G7.01 → G7.02 → G7.03

**Grade 8 (add 2 skills):**
- **G8.00A (KNN training)** → G8.02 → **G8.02B (KNN tuning)** → G8.03

**Total:** 8 critical new skills

---

## Quick Comparison: Before vs After

### Before (39 skills):
- Grade 6: 9 skills
- Grade 7: 6 skills
- Grade 8: 5 skills

**Gaps:**
- ❌ Continuous speech not covered
- ❌ Hand direction (dir column) not covered
- ❌ 3D pose mentioned but never taught
- ❌ AR face camera completely missing
- ❌ KNN training process not explained
- ❌ Modality selection not taught

### After (47 skills):
- Grade 6: 14 skills (+5)
- Grade 7: 7 skills (+1)
- Grade 8: 7 skills (+2)

**Coverage:**
- ✅ All perception modes covered
- ✅ All table columns explained
- ✅ ML foundation taught before advanced use
- ✅ Decision-making skills for modality selection

---

**Document Version:** 1.0
**Created:** 2025-11-21
**Purpose:** Quick reference for implementing 8 critical new T23 skills
**Status:** Ready for review and implementation
