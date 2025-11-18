# AI Skills Topic Assignments
**Date:** 2025-11-17
**Purpose:** Clear mapping of new AI skills to existing topics with rationale

---

## Overview

**Total New Skills:** 31
**Topics Modified:** 6 (T02, T04, T21, T23, T24, T35)
**New Topics Created:** 0
**Approach:** Integrate new AI skills into existing topics to maintain 36-topic structure

---

## Topic-by-Topic Assignments

### T02: Representing & Tracing Algorithms

**Topic Description:** How to represent problems, algorithms, and data structures
**Why this topic?** T02 focuses on representation and reasoning - perfect for AI4K12 Category B skills
**New Skills Added:** 11 (5 K-2 + 3 G3-5 + 3 G6-8)

#### New Skills in T02

##### Binary Decision-Making (AI4K12 Category B)
| Skill ID | Grade | Title | Skill Type | Activity Type |
|----------|-------|-------|------------|---------------|
| T02.GK.05 | K | Yes or No Game: Guess My Picture | picture_based | click_select |
| T02.G1.05 | 1 | Follow the Yes/No Path to Choose | picture_based | click_path |
| T02.G2.05 | 2 | Create a Yes/No Helper for Friends | picture_based | build_tree |

**Rationale:** Binary decision-making is fundamentally about representation (decision trees) and reasoning. Placing here (rather than T22 Chatbots) establishes the foundational concept before applying it to conversational AI.

**Dependencies:**
- T02.GK.05: None (foundational)
- T02.G1.05: T02.GK.05
- T02.G2.05: T02.G1.05

**Integration:** These become the .05 series in T02, following existing T02.GK.01-04, T02.G1.01-04, T02.G2.01-04

---

##### Creating Representations (AI4K12 Category B)
| Skill ID | Grade | Title | Skill Type | Activity Type |
|----------|-------|-------|------------|---------------|
| T02.GK.06 | K | Draw to Show What You See | picture_based | simple_draw |
| T02.G1.06 | 1 | Picture a Story in Order | picture_based | select_sequence |
| T02.G2.06 | 2 | Map Your Space | picture_based | build_map |
| T02.G3.06 | 3 | Design a Map for Navigation | standard | N/A |
| T02.G4.06 | 4 | Choose What Matters in Your Representation | standard | N/A |
| T02.G5.06 | 5 | Compare Representations for Different Tasks | standard | N/A |
| T02.G6.06 | 6 | Design an Infographic | standard | N/A |
| T02.G7.06 | 7 | Representation Tradeoffs: Detail vs. Simplicity | standard | N/A |
| T02.G8.06 | 8 | Feature Vectors for AI Classification | standard | N/A |

**Rationale:** Perfect fit for T02's focus on representation. These skills extend T02 from algorithmic representation to data representation, directly supporting AI/ML understanding. The G8 skill explicitly bridges to feature engineering for AI.

**Dependencies:**
- K-2: Sequential within grade (GK.06 → G1.06 → G2.06)
- G3-5: Build on T02.G2.06 + relevant decomposition/data skills
- G6-8: Build on prior representation skills + data analysis skills from T25, T27
- T02.G8.06: Bridges to T21.G7+ (AI), T25.G7+ (data)

**Integration:** These become the .06 series in T02, creating a complete K-8 progression on representation

**Visual Progression:**
```
K-2: Concrete representation (shapes, pictures, maps)
  ↓
G3-5: Abstract representation (navigation, feature selection, comparison)
  ↓
G6-8: Critical/AI representation (design, tradeoffs, feature vectors)
```

---

### T04: Patterns & Abstraction

**Topic Description:** Recognizing patterns, abstracting concepts, and generalizing solutions
**Why this topic?** T04 focuses on pattern recognition - foundational for machine learning concepts
**New Skills Added:** 3 (all K-2)

#### New Skills in T04

##### Pattern Learning (AI4K12 Category C - Machine Learning)
| Skill ID | Grade | Title | Skill Type | Activity Type |
|----------|-------|-------|------------|---------------|
| T04.GK.05 | K | Sort Pictures by What You See | picture_based | sort_categories |
| T04.G1.05 | 1 | Show the Computer What You Mean | picture_based | select_examples |
| T04.G2.05 | 2 | More Pictures Help AI Learn Better | picture_based | experiment_compare |

**Rationale:** Placed in T04 (not T21 AI Media) because these focus on pattern recognition and learning from examples - core pattern/abstraction concepts. They provide foundations that are later applied to AI media creation in T21.

**Dependencies:**
- T04.GK.05: None (foundational)
- T04.G1.05: T04.GK.05
- T04.G2.05: T04.G1.05, T21.G2.01

**Integration:** These become the .05 series in T04, complementing existing pattern recognition skills

**Connection to Later AI Topics:**
- T04.GK-G2.05 provide foundations for T21.G3.02+ (training data concepts)
- Pattern recognition here supports T25+ (data representation and analysis)

---

### T21: AI Media Tools & Creative Assets

**Topic Description:** Using AI tools to generate images, audio, and creative content
**Why this topic?** T21 covers practical AI use - perfect for understanding human role in AI creation
**New Skills Added:** 7 (all G3-8)

#### New Skills in T21

##### Human Role in Creating AI (AI4K12 Category D)
| Skill ID | Grade | Title | Description Summary |
|----------|-------|-------|---------------------|
| T21.G3.05 | 3 | The AI Team: Who Does What? | Identify roles: designer, data collector, trainer, tester, user |
| T21.G4.05 | 4 | What is Data Labeling? | Learn about data labeling work and its importance |
| T21.G5.05 | 5 | From Idea to Trained Model | Trace full AI creation process with human decisions |
| T21.G6.05 | 6 | Data Curation Matters | Explore how data curation affects AI quality |
| T21.G7.05 | 7 | Data Labeling Shapes AI Behavior | Understand how labeling choices introduce bias |
| T21.G8.05 | 8 | Design an AI Project Plan | Plan complete AI project with all human roles |

**Rationale:** T21 is where students actively use AI media tools (image generation, etc.). Understanding the human roles behind these tools fits perfectly - students learn WHO creates the AI they're using and HOW those human decisions affect what they experience.

**Dependencies:**
- T21.G3.05: T35.G2.05 (K-2 human role foundation), T21.G2.01
- G4-G8: Sequential progression + existing T21 skills about AI use
- T21.G8.05: Capstone requiring understanding from G3-G7

**Integration:** These become the .05 series in T21.G3-G8, interleaving with existing AI media skills

**Connection to Other Topics:**
- Builds on: T35.GK-G2.05 (K-2 "humans create AI" foundation)
- Supports: T24.G3-G8.05 (ethical AI creation)
- Informs: T25-T27 data skills (understanding data pipeline)

**Why not create a separate "Human Role in AI" topic?**
- Only 7 skills (G3-8) - not enough for standalone topic
- Conceptually fits within existing AI use context
- Students learn human role while using the AI tools those humans created
- Maintains 36-topic structure

---

### T23: Voice/Vision/Gesture AI

**Topic Description:** AI systems that perceive through vision, voice, and gestures
**Why this topic?** T23 covers AI perception - perfect for introducing sensing concepts
**New Skills Added:** 3 (all K-2)

#### New Skills in T23

##### Sensing (AI4K12 Category C - Machine Learning)
| Skill ID | Grade | Title | Skill Type | Activity Type |
|----------|-------|-------|------------|---------------|
| T23.GK.01 | K | Match Senses to Sensors | picture_based | match_pairs |
| T23.G1.01 | 1 | What Can Computers Sense? | picture_based | click_select |
| T23.G2.01 | 2 | Computers Need Sensors to Know Things | picture_based | match_pairs |

**Rationale:** Perfect fit for T23, which already covers vision AI (G3+), voice AI (G4+), and gesture recognition. These K-2 skills provide the foundational understanding: computers need sensors (cameras, microphones) to perceive the world, just like humans use senses.

**Dependencies:**
- T23.GK.01: None (foundational)
- T23.G1.01: T23.GK.01
- T23.G2.01: T23.G1.01

**Integration:** These become the first skills in T23 (previously started at G3)

**Progression to Existing T23 Skills:**
```
K-2: Understand sensors (eyes→camera, ears→microphone)
  ↓
G3-G5: Use vision AI and voice AI (existing T23 skills)
  ↓
G6-G8: Advanced multimodal AI (existing T23 skills)
```

**Why this placement works:**
- T23 currently starts at G3 with practical vision/voice AI use
- Adding K-2 foundation creates complete K-8 progression
- K-2 students learn conceptual foundations before hands-on use

---

### T24: Coding with AI (XO & AI-Supported Coding)

**Topic Description:** Programming with AI tools, AI-assisted coding, and building with AI
**Why this topic?** T24 covers AI programming - perfect for ethical AI system creation
**New Skills Added:** 6 (all G3-8)

#### New Skills in T24

##### Ethical AI System Design and Programming (AI4K12 Category E)
| Skill ID | Grade | Title | Description Summary |
|----------|-------|-------|---------------------|
| T24.G3.05 | 3 | Design AI for Everyone | User-centered AI design thinking |
| T24.G4.05 | 4 | Fairness Checklist for AI | Create ethical evaluation framework |
| T24.G5.05 | 5 | Design an Ethical Chatbot | Apply ethics to conversational AI design |
| T24.G6.05 | 6 | Build and Test for Bias | Hands-on: build classifier, test for bias |
| T24.G7.05 | 7 | Document AI Limitations: Model Card Basics | Create simplified model card |
| T24.G8.05 | 8 | Build Ethical AI with Full Documentation | Capstone: complete ethical AI project |

**Rationale:** T24 focuses on *creating* with AI tools and AI-assisted programming. These skills extend that to *ethically creating* AI systems. This complements existing T35-T36 skills that focus on *evaluating* societal impacts (from a user/citizen perspective).

**Key Distinction:**
- **T35-T36:** Evaluate AI's societal impacts (observer perspective)
- **T24.G3-G8.05:** Create AI ethically (creator perspective)

**Dependencies:**
- T24.G3.05: T21.G3.05 (understanding AI creation), T35.G3.01 (impacts awareness)
- G4-G8: Sequential progression + existing T21 (AI use) and T24 (coding) skills
- T24.G6.05: Requires T23.G5+ (vision AI experience)
- T24.G8.05: Capstone requiring T21.G8.05 (AI project planning) + T22.G7+ (chatbots)

**Integration:** These become the .05 series in T24.G3-G8, interleaving with existing AI coding skills

**Progression:**
```
G3-G5: Ethical DESIGN (thinking, checklists, planning)
  ↓
G6-G8: Ethical PROGRAMMING (building, testing, documenting)
```

**Why this placement works:**
- T24 is about building/programming with AI
- Ethical creation is a natural extension of coding skills
- Students learn to build responsibly, not just build
- Practical focus: model cards, bias testing (hands-on)

---

### T35: Societal & Economic Impacts of Computing

**Topic Description:** How computing and AI affect society, economy, and individuals
**Why this topic?** T35 covers societal awareness - perfect for K-2 "who creates AI" foundation
**New Skills Added:** 3 (all K-2)

#### New Skills in T35

##### Human Role in Creating AI - Foundational (AI4K12 Category D)
| Skill ID | Grade | Title | Skill Type | Activity Type |
|----------|-------|-------|------------|---------------|
| T35.GK.05 | K | Who Makes the AI? | picture_based | match_pairs |
| T35.G1.05 | 1 | People Build AI Tools | picture_based | click_select |
| T35.G2.05 | 2 | Humans Teach AI to Work | picture_based | sequence_story |

**Rationale:** T35 focuses on societal awareness and understanding technology's impact. These K-2 skills establish the fundamental understanding that AI is created by people - not magic, not autonomous. This prevents anthropomorphization and builds responsible AI literacy from kindergarten.

**Dependencies:**
- T35.GK.05: None (foundational)
- T35.G1.05: T35.GK.05
- T35.G2.05: T35.G1.05, T04.G2.05 (pattern learning)

**Integration:** These become the .05 series in T35.GK-G2, complementing existing impact awareness skills

**Why K-2 in T35 (not T21)?**
- K-2 focus is on societal understanding ("who makes technology?")
- Not yet about using AI tools (that starts T21.G2+)
- Fits T35's mission: understanding technology's human origins
- G3-8 human role skills move to T21 where students actively use AI

**Connection to T21:**
```
T35.GK-G2.05: Foundational awareness (people create AI)
  ↓
T21.G3-G8.05: Applied understanding (HOW people create AI)
```

---

## Skill ID Numbering Strategy

### Numbering Convention

**Format:** `T{Topic}.G{Grade}.{Number}`

**New Skills Use .05 and .06 Series:**
- **.05 series:** Primary new AI skills for each grade
- **.06 series:** Additional skills (used only in T02 for representations)

**Why .05 and .06?**
- Most topics have .01-.04 skills already
- .05+ are available across all topics
- Keeps new skills clearly identifiable
- Maintains consistency across topics

### Skill ID Ranges by Topic

| Topic | Skill Series | Grades | Count | ID Examples |
|-------|-------------|--------|-------|-------------|
| T02 | .05 (reasoning) | K-2 | 3 | T02.GK.05, T02.G1.05, T02.G2.05 |
| T02 | .06 (representation) | K-8 | 9 | T02.GK.06, T02.G3.06, T02.G8.06 |
| T04 | .05 | K-2 | 3 | T04.GK.05, T04.G1.05, T04.G2.05 |
| T21 | .05 | G3-8 | 7 | T21.G3.05, T21.G4.05, T21.G8.05 |
| T23 | .01 | K-2 | 3 | T23.GK.01, T23.G1.01, T23.G2.01 |
| T24 | .05 | G3-8 | 6 | T24.G3.05, T24.G4.05, T24.G8.05 |
| T35 | .05 | K-2 | 3 | T35.GK.05, T35.G1.05, T35.G2.05 |

**Note:** T23 uses .01 because T23 previously started at G3 (no K-2 skills existed).

---

## Topic Size Analysis

### Before and After New Skills

| Topic | Before | New K-2 | New G3-5 | New G6-8 | After | Size Assessment |
|-------|--------|---------|----------|----------|-------|-----------------|
| T02 | ~20 | 5 | 3 | 3 | ~31 | Medium → Large |
| T04 | ~20 | 3 | 0 | 0 | ~23 | Medium |
| T21 | 25 | 0 | 3 | 4 | 32 | Large |
| T23 | ~15 | 3 | 0 | 0 | ~18 | Medium |
| T24 | ~20 | 0 | 3 | 3 | ~26 | Medium → Large |
| T35 | ~20 | 3 | 0 | 0 | ~23 | Medium |

### Size Considerations

**Larger Topics (30+ skills):**
- **T02:** Now 31 skills - manageable because covers foundational concepts
- **T21:** Now 32 skills - manageable, could consider split in future

**Future Consideration:**
If T21 feels too large (32 skills), could split into:
- **T21A:** Understanding AI & Human Role (how AI works, who creates it)
- **T21B:** Creating with AI Media (practical image/audio generation)

**Decision:** DEFER split until implementation shows it's needed. Current structure is workable.

---

## Cross-Topic Connections

### How New Skills Connect Across Topics

#### K-2 Foundation Layer
```
T35.GK-G2.05 (people create AI)
    ↓ societal awareness
T04.GK-G2.05 (pattern learning) ← connects → T02.GK-G2.05 (reasoning)
    ↓ concepts                              ↓ representation
T23.GK-G2.01 (sensing)
    ↓ all feed into
T21.G2.01+ (using AI media tools)
```

#### G3-8 Application Layer
```
T02.G3-G8.06 (creating representations)
    ↓ supports data for AI
T21.G3-G8.05 (human role in creating AI)
    ↓ understanding creation
T24.G3-G8.05 (ethical AI system programming)
    ↓ responsible creation
Existing T21-T24 (practical AI use and building)
```

### Gateway Skills (Enable Later Learning)

**K-2 Gateways:**
- T02.GK.05: Enables all decision tree / conditional logic work
- T04.GK.05: Enables all pattern recognition and ML concepts
- T35.GK.05: Enables responsible AI awareness throughout K-8

**G3-5 Gateways:**
- T21.G3.05: Enables understanding of AI creation pipeline
- T24.G3.05: Enables ethical design thinking for all AI work

**G6-8 Capstones:**
- T02.G8.06: Feature vectors bridge representation to ML
- T21.G8.05: Plan complete AI project with human roles
- T24.G8.05: Build ethical AI with full documentation

---

## Rationale Summary by Design Decision

### Why No New Topics?

**Considered creating:**
- T24B: Human Role in AI Creation
- T21A/B: Split AI Media

**Decision: Use existing topics because:**
1. **Skill counts manageable:** No topic exceeds 35 skills
2. **Conceptual fit strong:** All skills align with existing topic purposes
3. **Avoid fragmentation:** 36 topics is already comprehensive
4. **Flexibility:** Can split later if needed (T21 is candidate)
5. **Simplicity:** Easier for teachers/students to navigate

### Why T02 for Representation (not T25 Data)?

**T02 chosen because:**
- Representation is T02's core focus (representing algorithms, structures)
- T25 focuses on data *formats* and *types* (numerical, text, image)
- T02.G8.06 bridges from representation to data/AI (perfect transition)
- Creates complete K-8 progression in one topic

### Why T35 for K-2 Human Role (not T21)?

**T35 chosen because:**
- K-2 focus is societal awareness (who creates technology?)
- Not yet about using AI tools (T21 is for users)
- G3-8 human role moves to T21 where students use AI actively
- Logical progression: understand creators (T35) → understand creation process (T21)

### Why T24 for Ethical Creation (not T36 Ethics)?

**T24 chosen because:**
- T36 focuses on ethical evaluation and career awareness (observer)
- T24 focuses on building/programming (creator)
- Ethical creation is hands-on: model cards, bias testing, documentation
- T24.G3-G8.05 = "ethical programming" (action), T36 = "ethical awareness" (understanding)

---

## Implementation Sequence Recommendation

### Phase 1: High Priority (Immediate - Month 1-2)

**Goal:** Address critical gaps with easiest-to-implement skills

1. **T04.GK-G2.05** (3 skills) - K-2 pattern learning
   - Easy: sorting/selection activities
   - High impact: foundational ML concept

2. **T02.GK-G2.05** (3 skills) - K-2 reasoning
   - Easy: yes/no activities, tree navigation
   - High impact: foundational decision-making

3. **T35.GK-G2.05** (3 skills) - K-2 human role
   - Easy: matching, selection activities
   - High impact: prevents anthropomorphization

**Subtotal:** 9 skills (all K-2, picture-based, easy to create)

### Phase 2: Medium Priority (Short-term - Month 3-4)

**Goal:** Add G3-8 human role and ethical creation

4. **T21.G3-G8.05** (7 skills) - G3-8 human role in AI
   - Medium effort: needs lesson content, examples
   - High impact: understanding AI creation pipeline

5. **T24.G3-G8.05** (6 skills) - G3-8 ethical AI creation
   - Medium-high effort: needs templates (model card)
   - High impact: responsible AI development

**Subtotal:** 13 skills (G3-8, standard format, medium effort)

### Phase 3: Complete Coverage (Medium-term - Month 5-6)

**Goal:** Complete AI4K12 alignment with sensing and representation

6. **T23.GK-G2.01** (3 skills) - K-2 sensing
   - Easy: matching activities
   - Medium impact: completes perception foundation

7. **T02.GK-G8.06** (9 skills) - K-8 representation
   - Medium effort: varied activities (K-2 drawing/mapping, G3-8 design)
   - Medium impact: foundational skill applied to AI

**Subtotal:** 12 skills (mixed K-8, varied effort)

**Total:** 31 skills across 3 phases

---

## Integration Checklist

### For Each Topic Modified

- [ ] **T02:** Add 11 skills (.05 series for reasoning, .06 series for representation)
  - [ ] Update topic description to mention AI/ML representation
  - [ ] Verify dependencies don't conflict with existing T02 skills
  - [ ] Ensure K-2 progression is clear

- [ ] **T04:** Add 3 skills (.05 series for pattern learning)
  - [ ] Connect to existing pattern recognition skills
  - [ ] Link to T21 for AI application

- [ ] **T21:** Add 7 skills (.05 series for G3-8 human role)
  - [ ] Integrate with existing AI media use skills
  - [ ] Ensure human role context enhances AI tool use

- [ ] **T23:** Add 3 skills (.01 series for K-2 sensing)
  - [ ] These become the first T23 skills (topic previously started at G3)
  - [ ] Create clear bridge to existing G3+ vision/voice skills

- [ ] **T24:** Add 6 skills (.05 series for G3-8 ethical creation)
  - [ ] Create model card template
  - [ ] Connect to T22 (chatbots) and T21 (AI media)

- [ ] **T35:** Add 3 skills (.05 series for K-2 human role)
  - [ ] Position as foundational societal awareness
  - [ ] Connect to T21.G3+ for deeper exploration

---

## Summary: Clear Decision Trail

### Every Skill Has a Home

| AI4K12 Gap | New Skills | Topic | Rationale in 5 Words |
|------------|------------|-------|----------------------|
| Binary Reasoning | 3 (K-2) | T02 | Representation of decision processes |
| Pattern Learning | 3 (K-2) | T04 | Pattern recognition enables machine learning |
| Human Role K-2 | 3 (K-2) | T35 | Societal awareness of technology creators |
| Human Role G3-8 | 7 (G3-8) | T21 | Understanding tools students actively use |
| Ethical Creation | 6 (G3-8) | T24 | Programming with ethical responsibility |
| Sensing | 3 (K-2) | T23 | How computers perceive world |
| Representation | 9 (K-8) | T02 | Representing data for understanding/AI |

### All Decisions Support Core Goals

✅ **Maintain 36-topic structure:** No new topics needed
✅ **Clear conceptual fit:** Every skill enhances its topic's purpose
✅ **Logical progression:** K-2 foundations → G3-8 applications
✅ **Manageable topic sizes:** No topic exceeds 35 skills
✅ **Cross-topic connections:** Skills support each other across topics
✅ **Teacher clarity:** Clear rationale for every placement
✅ **Student experience:** Skills appear in context of related learning

---

**End of Document**
