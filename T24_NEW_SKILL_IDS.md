# T24 New Skill IDs - Prioritized List

## PRIORITY 1: Critical Additions (Must Add)

### ChatGPT Essential Features
- **T24.G5.07.04**: Adjust response length with max tokens parameter
- **T24.G5.07.05**: Understand session continuity (new chat vs continue)
- **T24.G5.07.06**: Cancel ongoing ChatGPT requests
- **T24.G6.08.02**: Use system instructions to configure ChatGPT behavior
- **T24.G6.08.03**: Understand multiple chatbot sessions (1-4)

### Neural Network Predictions (CRITICAL GAP)
- **T24.G8.09.05**: Make predictions with trained neural networks
- **T24.G8.09.06**: Evaluate model accuracy on test data

### Scaffolding for Complex Features
- **T24.G5.05.02**: Read and filter data from multi-row tables
- **T24.G5.08.02**: Practice reading and using CV coordinates
- **T24.G6.07.05**: Practice simple two-turn ChatGPT conversations

**Total Priority 1: 10 skills**

---

## PRIORITY 2: Important Breakdowns (Should Add)

### Face Detection Breakdown (G5.09)
- **T24.G5.09.01**: Enable face detection with debug visualization
- **T24.G5.09.02**: Understand face detection table structure (13 rows)
- **T24.G5.09.03**: Read facial feature coordinates

### Hand Detection Breakdown (G6.10)
- **T24.G6.10.04**: Read 2D keypoint coordinates for hand position
- **T24.G6.10.05**: Read 3D keypoint coordinates for depth sensing
- **T24.G6.10.06**: Build single-hand gesture controls

### Body Detection Breakdown (G6.11)
- **T24.G6.11.04**: Read limb curl and direction values
- **T24.G6.11.05**: Detect simple movements (jumping, arm raising)
- **T24.G6.11.06**: Build basic body-controlled interactions

### 3D Pose Detection Breakdown (G7.08)
- **T24.G7.08.05**: Calculate 3D distances between body parts
- **T24.G7.08.06**: Calculate angles between joints
- **T24.G7.08.07**: Detect simple poses (T-pose, arms raised)
- **T24.G7.08.08**: Detect complex poses (yoga, jumping)
- **T24.G7.08.09**: Build full-body pose-based games

### Neural Network Architecture Breakdown (G8.08)
- **T24.G8.08.03**: Choose activation functions (relu, sigmoid, softmax)
- **T24.G8.08.04**: Choose loss functions (crossentropy, MSE)
- **T24.G8.08.05**: Choose optimizers and learning rate
- **T24.G8.08.06**: Compile model with loss and optimizer

### Neural Network Training Breakdown (G8.09)
- **T24.G8.09.02b**: Configure batch size and understand effects
- **T24.G8.09.03b**: Configure epochs and understand convergence

### Semantic Search Expansion (G8.10-11)
- **T24.G8.10.01**: Understand vector embeddings and Pinecone
- **T24.G8.10.03**: Populate semantic database with content
- **T24.G8.11.03**: Build complex filters with SQL-like conditions
- **T24.G8.11.04**: Compare semantic vs keyword search results

### RAG Systems Breakdown (G8.12)
- **T24.G8.12.03**: Add web search to retrieval pipeline
- **T24.G8.12.04**: Rank and deduplicate retrieval results
- **T24.G8.12.05**: Format retrieved context for ChatGPT
- **T24.G8.12.07**: Build specialized domain knowledge chatbots

### Neural Network Prep (G7.15)
- **T24.G7.15.01**: Analyze simple neural network architectures
- **T24.G7.15.02**: Compare KNN and neural network approaches

**Total Priority 2: 28 skills**

---

## PRIORITY 3: Nice-to-Have Additions (Consider)

### File Handling
- **T24.G7.13.01**: Handle file selection and parse multiple paths

### Moderation Systems
- **T24.G6.07.04**: Build complete content validation systems

### Debug Mode
- **T24.G7.07.03A**: Toggle debug mode for production vs testing

### Advanced Comparisons
- **T24.G8.01.04**: Compare LLM model options (small vs large)
- **T24.G8.11.05**: Understand ChatGPT limitations without context

**Total Priority 3: 5 skills**

---

## REORGANIZATION: Existing Skills That Need Renumbering

### Face Detection (T24.G5.09 → T24.G5.09.04)
**Current:**
- T24.G5.09: Explore face detection and coordinate system
- T24.G5.09.01: Read single face features from detection tables
- T24.G5.10: Use face position to control sprites

**Proposed:**
- T24.G5.09.01: Enable face detection with debug (NEW!)
- T24.G5.09.02: Understand table structure (NEW!)
- T24.G5.09.03: Read facial features (NEW!)
- **T24.G5.09.04**: Read single face features (was G5.09.01)
- T24.G5.10: Use face position to control sprites (unchanged)

---

### Hand Detection (T24.G6.10 → Renumber)
**Current:**
- T24.G6.10.01: Understand hand detection table structure
- T24.G6.10.02: Read curl and direction values
- T24.G6.10.03: Build basic hand gesture controls

**Proposed:**
- T24.G6.10.01: Enable hand detection (revised)
- T24.G6.10.02: Table structure overview (revised)
- T24.G6.10.03: Finger curl & direction (revised)
- T24.G6.10.04: 2D keypoints (NEW!)
- T24.G6.10.05: 3D keypoints (NEW!)
- T24.G6.10.06: Single-hand gestures (NEW!)

---

### Body Detection (T24.G6.11 → Renumber)
**Current:**
- T24.G6.11.01: Understand 2D body detection table structure
- T24.G6.11.02: Read body part positions and detect movements
- T24.G6.11.03: Build interactive games with body tracking

**Proposed:**
- T24.G6.11.01: Enable 2D body detection (revised)
- T24.G6.11.02: Table structure (revised)
- T24.G6.11.03: Body part positions (revised)
- T24.G6.11.04: Limb curl & direction (NEW!)
- T24.G6.11.05: Simple movements (NEW!)
- T24.G6.11.06: Body-controlled interactions (NEW!)

---

### 3D Pose (T24.G7.08 → Major Renumber)
**Current:**
- T24.G7.08.01: Understand 3D pose with 33 parts
- T24.G7.08.02: Calculate angles and distances
- T24.G7.08.03: Detect specific poses
- T24.G7.08.04: Build full-body pose-based games

**Proposed:**
- T24.G7.08.01: Enable + coordinate system (revised)
- T24.G7.08.02: Table structure (revised)
- T24.G7.08.03: Upper body positions (NEW!)
- T24.G7.08.04: Lower body positions (NEW!)
- T24.G7.08.05: 3D distance calculations (NEW!)
- T24.G7.08.06: Angle calculations (NEW!)
- T24.G7.08.07: Simple poses (NEW!)
- T24.G7.08.08: Complex poses (NEW!)
- T24.G7.08.09: Full-body games (NEW!)

---

### Neural Networks (T24.G8.08-09 → Major Reorganization)
**Current:**
- T24.G8.08.01: Create models and add layers
- T24.G8.08.02: Compile with loss and optimizer
- T24.G8.09.01: Prepare datasets
- T24.G8.09.02: Configure training parameters
- T24.G8.09.03: Train and monitor
- T24.G8.09.04: Save and load

**Proposed:**
- T24.G8.08.01: Create model (unchanged)
- T24.G8.08.02: Add layers (revised)
- T24.G8.08.03: Activation functions (NEW!)
- T24.G8.08.04: Loss functions (NEW!)
- T24.G8.08.05: Optimizers (NEW!)
- T24.G8.08.06: Compile model (NEW!)
- T24.G8.09.01: Prepare datasets (unchanged)
- T24.G8.09.02: Batch size (revised)
- T24.G8.09.03: Epochs (revised)
- T24.G8.09.04: Train & monitor (revised)
- T24.G8.09.05: Make predictions (NEW!)
- T24.G8.09.06: Evaluate accuracy (NEW!)
- T24.G8.09.07: Save/load (was .04)

---

## SUMMARY BY GRADE

### Grade 5 Additions
**New Skills:** 6
- G5.05.02: Table filtering
- G5.07.04: Max tokens
- G5.07.05: Sessions
- G5.07.06: Cancel
- G5.08.02: CV coordinates
- G5.09.01-03: Face detection breakdown

**New Total:** 18 → 24 (+6)

---

### Grade 6 Additions
**New Skills:** 9
- G6.07.04: Content validation
- G6.07.05: Two-turn practice
- G6.08.02: System instructions
- G6.08.03: Multiple chatbots
- G6.10.04-06: Hand detection breakdown
- G6.11.04-06: Body detection breakdown

**New Total:** 21 → 30 (+9)

---

### Grade 7 Additions
**New Skills:** 9
- G7.07.03A: Debug toggle
- G7.08.05-09: 3D pose breakdown
- G7.13.01: Multiple files
- G7.15.01-02: NN prep

**New Total:** 16 → 25 (+9)

---

### Grade 8 Additions
**New Skills:** 19
- G8.01.04: LLM models
- G8.08.03-06: NN architecture breakdown
- G8.09.02b-03b: Training breakdown
- G8.09.05-06: Predictions + evaluation
- G8.09.07: Save/load renumber
- G8.10.01,03: Semantic breakdown
- G8.11.03-05: Search expansion
- G8.12.03-05,07: RAG breakdown

**New Total:** 24 → 43 (+19)

---

## GRAND TOTAL

**Current Total:** 107 skills
**Priority 1:** +10 skills
**Priority 2:** +28 skills
**Priority 3:** +5 skills

**New Total:** 107 + 43 = **150 skills**

---

## IMPLEMENTATION PHASES

### Phase 1: Critical Gaps (2-3 weeks)
Implement Priority 1 (10 skills)
- ChatGPT essential features (5 skills)
- Neural network predictions (2 skills)
- Scaffolding basics (3 skills)

### Phase 2: Computer Vision Breakdown (4-5 weeks)
Implement CV breakdowns from Priority 2 (18 skills)
- Face detection (3 skills)
- Hand detection (3 skills)
- Body detection (3 skills)
- 3D pose (5 skills)
- NN prep (2 skills)
- Semantic/RAG basics (2 skills)

### Phase 3: Neural Networks Deep Dive (2-3 weeks)
Implement NN breakdowns from Priority 2 (6 skills)
- Architecture details (4 skills)
- Training parameters (2 skills)

### Phase 4: Advanced Systems (2-3 weeks)
Implement semantic/RAG from Priority 2 (4 skills)
- Semantic search expansion (2 skills)
- RAG pipeline breakdown (4 skills)

### Phase 5: Polish (1-2 weeks)
Implement Priority 3 (5 skills)
- File handling, debug mode, comparisons

**Total Timeline: 11-16 weeks**

---

*This is a PLANNING DOCUMENT - no files modified*
