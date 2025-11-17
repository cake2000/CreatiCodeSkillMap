# T25-T29 Dependency Analysis - Executive Summary

**Analysis Date:** 2025-11-17
**Domain:** Data & Analysis (Topics 25-29)
**Analyst:** Claude Code Dependency Analyzer

---

## Quick Stats

| Metric | Value |
|--------|-------|
| **Total Skills** | 167 |
| **Topics** | 5 (T25-T29) |
| **Gateway Skills** | 2 (1.2%) |
| **Capstone Skills** | 9 (5.4%) |
| **Average Dependencies** | 2.37 per skill |
| **Grade-Level Violations** | 0 ✓ |
| **Quality Assessment** | Excellent |

---

## Topic Breakdown

### T25: Data Representation & Simple Data Types
- **Skills:** 39
- **Avg Deps:** 1.97
- **Role:** Foundation for all data work
- **Key Skill:** T25.G3.05 (Lists for data) - GATEWAY
- **Grades:** 1-8, even distribution (4-5 skills per grade)

### T26: Data Collection & Organization
- **Skills:** 35
- **Avg Deps:** 2.20
- **Role:** Gathering and organizing data systematically
- **Key Skills:** T26.G6.05 (Data cleaning), T26.G8.02 (Complete investigation - CAPSTONE)
- **Progression:** Manual → Automated → Ethical

### T27: Data Analysis & Visualization
- **Skills:** 31
- **Avg Deps:** 2.13
- **Role:** Computing statistics and creating visualizations
- **Key Skills:** T27.G8.01 (Data investigation), T27.G8.03 (Interactive dashboard - CAPSTONE)
- **Progression:** Counting → Statistics → Relationships → Dashboards

### T28: Chance, Sampling & Experiments
- **Skills:** 31
- **Avg Deps:** 2.39 (highest)
- **Role:** Probability, simulations, and experimental design
- **Key Skills:** T28.G7.02 (Monte Carlo - CAPSTONE), T28.G8.03 (AI bias analysis)
- **Progression:** Likelihood → Simulations → Experiments → Ethics

### T29: Text Data & Introductory NLP
- **Skills:** 31
- **Avg Deps:** 2.16
- **Role:** Text as data + AI-powered natural language processing
- **Key Skills:** T29.G3.03 (AI text - GATEWAY), T29.G8.01 (Search system - CAPSTONE)
- **Progression:** Words → Lists → AI → NLP Systems

---

## Key Findings

### 1. Data Science Pipeline Architecture
The five topics form a complete data science workflow:
```
T25 (Representation) → T26 (Collection) → T27 (Analysis) → T28 (Experiments) ⟲
                                                              ↓
                                                        T29 (Text/NLP)
```

### 2. Programming Core Integration
Strong dependencies on:
- **T09 (Variables):** Used in all 5 topics for data storage and calculations
- **T10 (Lists):** Critical for all data structures (T25.G3.05 is gateway)
- **T07 (Loops):** Essential for data processing, especially T27-T28
- **T11 (Functions):** Modular analysis in T27-T29
- **T08 (Conditionals):** Filtering and data selection

### 3. Gateway Skills (2)

#### T25.G3.05: Build a data structure with a list (Grade 3)
- **Impact:** Unlocks all structured data work across T25-T29
- **Why Critical:** Lists are the fundamental data structure for collections
- **Dependencies:** T25.G3.03, T10.G3.01

#### T29.G3.03: Ask AI a question and receive response (Grade 3)
- **Impact:** Unlocks all AI-powered NLP in T29
- **Why Critical:** Introduces students to AI text processing
- **Dependencies:** T22.G3.01 (Chatbots)

### 4. Capstone Skills (9)

#### Grade 6 (1 capstone)
- **T26.G6.05:** Clean and prepare data (5 deps)

#### Grade 7 (2 capstones)
- **T26.G7.03:** Manipulate data with code (6 deps)
- **T28.G7.02:** Monte Carlo simulation (6 deps)

#### Grade 8 (6 major capstones)
- **T26.G8.02:** Complete data investigation (7 deps) - Highest dependency count
- **T27.G8.01:** Data investigation (6 deps)
- **T27.G8.03:** Interactive dashboard (6 deps) - Bridges to T16 UI
- **T28.G8.01:** Real-world experiment (6 deps)
- **T29.G8.01:** Keyword search system (6 deps)
- **T29.G8.04:** NLP ethics evaluation (5 deps)

### 5. Grade Progression Patterns

#### Early Elementary (K-2): Data Awareness
- Recognizing categories, comparing quantities
- Simple tallies and charts
- Introduction to variables for data storage

#### Elementary (3-4): Data Structures and Basic Analysis
- **G3:** Lists as data structures (GATEWAY)
- **G4:** Tables, logging events, basic statistics
- Introduction to probability concepts

#### Middle School (5-6): Computational Data Science
- **G5:** Loops for aggregation, functions for analysis
- **G6:** Filtering, grouping, research design
- Automated data collection (sensors)

#### Advanced Middle School (7-8): Complete Projects
- **G7:** Simulations, systematic investigations
- **G8:** Complete end-to-end data projects (CAPSTONES)
- Ethics, bias analysis, AI integration

### 6. AI Integration (Primary in T29)
- **8 AI-powered skills** in T29 (using T22 Chatbots)
- Progression: Simple Q&A → Classification → Summarization → Entity Extraction
- **T28.G8.03:** AI bias analysis bridges probability to AI ethics
- Natural connection between data science and AI/ML

### 7. Cross-Topic Dependencies

**Most Connected Topics:**
1. **T10 (Lists):** Referenced by all 5 data topics
2. **T27 (Analysis):** Used by T26 (collection), T28 (experiments), T29 (text viz)
3. **T26 (Collection):** Feeds into T27, T28
4. **T25 (Representation):** Foundation for all others

**Key Bridges:**
- T26 ↔ T27: Collection feeds analysis
- T27 → T29: Visualization used for text data
- T28 ↔ T26/T27: Experiments use collection and analysis
- T29 → T22: Text processing uses AI
- T28 → T22: Bias analysis connects probability to AI

---

## Strengths

### Architectural Excellence
1. **Clear pipeline:** Representation → Collection → Analysis → Experiments/Text
2. **Systematic progression:** Each grade builds on previous
3. **Integration:** Strong links to T06-T13 programming core
4. **Realistic workflow:** Mirrors professional data science process

### Pedagogical Quality
1. **Grade-appropriate:** All dependencies respect grade levels (0 violations)
2. **Conceptual before computational:** G1-G2 concepts, G3+ coding
3. **Ethics integrated:** G6-G8 address bias, fairness, impacts
4. **Hands-on projects:** 9 major capstones provide authentic experience

### Technical Depth
1. **Complete toolkit:** From simple counts to Monte Carlo simulations
2. **Modern skills:** AI/NLP integration in T29
3. **Statistical rigor:** Proper progression through statistics concepts
4. **Real-world applications:** Experiments, investigations, dashboards

---

## Comparison to Other Domains

### vs. T14-T24 (Applications)
| Metric | T14-T24 Apps | T25-T29 Data |
|--------|--------------|--------------|
| Skills | 346 | 167 |
| Avg Deps | 7.25 | 2.37 |
| Capstones | 256 (74%) | 9 (5.4%) |
| Nature | Integrative | Foundational |

**Analysis:** Data topics are more foundational with systematic progressions, while applications heavily integrate multiple skill areas.

### vs. T06-T13 (Programming Core)
| Metric | T06-T13 Core | T25-T29 Data |
|--------|--------------|--------------|
| Skills | ~100 | 167 |
| Gateways | 21 | 2 |
| Role | Building blocks | Applications |

**Analysis:** Data topics apply programming core concepts to authentic data science tasks.

---

## The Data Literacy Pathway

### Essential Progression for K-8 Data Science

```
Grade 1-2: Data Awareness
  T25.G1.01 (Categories) → T25.G2.02 (Variables) → T26.G2.02 (Tables) → T27.G2.01 (Charts)

Grade 3-4: Data Structures
  T25.G3.05 (Lists) → T26.G4.02 (Logging) → T27.G4.01 (Statistics) → T28.G4.02 (Probability)

Grade 5-6: Computational Methods
  T27.G5.01 (Aggregation) → T26.G5.03 (Filtering) → T28.G5.01 (Simulation) → T29.G6.03 (AI Classification)

Grade 7-8: Complete Projects
  T26.G8.02 (Investigation) → T27.G8.01 (Analysis) → T28.G8.01 (Experiments) → T29.G8.01 (NLP)
```

---

## AI Bridges (Data ↔ AI)

### T29: Text Data & NLP → T22: Chatbots
**8 skills use AI for text processing:**
- T29.G3.03: Simple Q&A (GATEWAY)
- T29.G4.03: Sentiment classification
- T29.G5.03: Text summarization
- T29.G6.03: Multi-category classification
- T29.G7.03: Question answering
- T29.G8.02: Sentiment at scale
- T29.G8.03: Entity extraction
- T29.G8.04: Ethics evaluation

### T28: Experiments → T22: AI Bias
**1 critical bridge:**
- T28.G8.03: Analyze bias in AI models trained on biased data
  - Connects probability/sampling to ML fairness
  - Bridges data science to AI ethics

### T27: Visualization → T16: UI Widgets
**1 major bridge:**
- T27.G8.03: Interactive data dashboard
  - Combines data visualization with UI design
  - Creates data-driven applications

### Future Opportunities
- T27 → T21 (AI Media): Data-driven generative art
- T28 → T23 (Voice/Vision): AI model evaluation
- T26 → T30 (Hardware): Physical data collection devices
- T28 → T24 (Responsible AI): Expanded ethics integration

---

## Recommendations

### For Curriculum Implementation
1. **Emphasize T25 foundation:** Ensure solid understanding before T26-T29
2. **Gateway at G3:** T25.G3.05 (lists) is critical - allocate sufficient time
3. **Integrate ethics early:** Don't wait until G8 for bias/fairness discussions
4. **Use real data:** Students should work with authentic datasets
5. **AI as tool:** T29 shows AI augmenting human data work, not replacing it

### For Skill Map Enhancement
1. **Add mid-grade capstones:** G5-G6 could use more integrative projects
2. **Strengthen hardware links:** T26 sensors could expand to T30
3. **More collaborative data:** T26.G6.03 multiplayer data could be a larger theme
4. **Expand AI bridges:** Connect T27 to T21 for data-driven art
5. **Add data storytelling:** Could add skills about communicating data findings

### For Assessment
1. **Test gateway mastery:** Ensure students master T25.G3.05 and T29.G3.03
2. **Capstone portfolios:** G8 capstones make excellent portfolio pieces
3. **Ethical reasoning:** Assess both technical and ethical understanding
4. **Real investigations:** Use authentic data investigations for summative assessment

---

## Data Literacy Outcomes

By the end of Grade 8, students who complete T25-T29 will be able to:

### Technical Skills
- ✓ Design and implement data schemas
- ✓ Collect, clean, and organize data systematically
- ✓ Compute descriptive and inferential statistics
- ✓ Create effective data visualizations
- ✓ Design and conduct experiments
- ✓ Build Monte Carlo simulations
- ✓ Process text data computationally
- ✓ Use AI for NLP tasks

### Analytical Skills
- ✓ Formulate testable questions
- ✓ Identify patterns and relationships in data
- ✓ Distinguish correlation from causation
- ✓ Evaluate statistical claims
- ✓ Recognize sampling bias
- ✓ Analyze variability and uncertainty

### Ethical Skills
- ✓ Recognize bias in data collection and representation
- ✓ Evaluate fairness in algorithms and AI
- ✓ Consider privacy in data collection
- ✓ Assess impacts of data-driven decisions
- ✓ Communicate data findings responsibly

### Integration Skills
- ✓ Combine data, programming, and domain knowledge
- ✓ Work with both structured and unstructured data
- ✓ Use computational tools for data science
- ✓ Integrate AI into data workflows
- ✓ Create data-driven applications

---

## Conclusion

The T25-T29 Data & Analysis domain represents a **comprehensive, well-structured K-8 data science curriculum** that prepares students for both practical data work and ethical data citizenship. With 167 carefully sequenced skills, 9 major capstone projects, and strong integration with programming core and AI topics, this progression provides students with the complete toolkit for 21st-century data literacy.

### Key Achievements
- ✓ **Zero grade violations:** Perfect grade-level consistency
- ✓ **Clear pipeline:** Logical progression from representation to NLP
- ✓ **Strong integration:** Excellent connection to T06-T13 and T21-T24
- ✓ **Modern skills:** Includes AI, simulations, interactive dashboards
- ✓ **Ethics emphasis:** Bias and fairness integrated throughout
- ✓ **Authentic tasks:** Realistic data science projects at G7-G8

### Final Assessment
**Quality Score: Excellent**

The dependency structure supports effective learning progressions, the topic integration mirrors professional data science workflows, and the ethical dimensions prepare students for responsible data citizenship. This curriculum successfully balances conceptual understanding, computational skills, and ethical reasoning across the K-8 spectrum.

---

**Report Generated:** 2025-11-17
**Validation Status:** ✓ Complete
**Dependencies File:** dependencies_T25_T29.json
**Detailed Report:** DEPENDENCIES_T25_T29_REPORT.md
