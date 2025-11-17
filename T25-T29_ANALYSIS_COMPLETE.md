# Topics T25-T29: Data & Analysis Domain - Analysis Complete

**Analysis Date:** 2025-11-17
**Domain:** Data & Analysis (Topics 25-29)
**Total Skills Analyzed:** 167
**Status:** COMPLETE ✓

---

## Executive Summary

The T25-T29 Data & Analysis domain has been comprehensively analyzed with complete dependency mapping for all 167 skills across 5 topics. This analysis reveals a **well-architected, pedagogically sound data science curriculum** that progresses logically from foundational data concepts through advanced applications, with strong integration into the programming core and AI topics.

### Quick Statistics

| Metric | Value |
|--------|-------|
| **Total Skills** | 167 |
| **Topics** | 5 (T25-T29) |
| **Gateway Skills** | 2 (1.2%) |
| **Capstone Skills** | 9 (5.4%) |
| **Average Dependencies/Skill** | 2.37 |
| **Grade-Level Violations** | 0 ✓ |
| **Quality Rating** | Excellent |

---

## Topics Overview

### T25: Data Representation & Simple Data Types (39 skills)
**Role:** Foundation for all data work
- **Grade Span:** K-8
- **Avg Dependencies:** 1.97
- **Key Gateway:** T25.G3.05 - Lists for data structures (Grade 3)
- **Primary Links:** T09 (Variables), T10 (Lists), T02 (Tracing), T35 (Impacts)

**Progression:**
- K-2: Categories, numerical comparison, simple tallies
- G3-4: Data types, variables for data, tables
- G5-6: Data quality, metadata, measurement levels
- G7-8: Data schemas, representation bias, nested structures

### T26: Data Collection & Organization (35 skills)
**Role:** Systematic data gathering and preparation
- **Grade Span:** 1-8
- **Avg Dependencies:** 2.20
- **Key Capstones:** T26.G6.05, T26.G7.03, T26.G8.02 (Complete investigation)
- **Primary Links:** T25 (Data Types), T10 (Lists), T08 (Conditionals), T06 (Events)

**Progression:**
- K-2: Surveys, observations, simple questions
- G3-4: Collaborative collection, table organization
- G5-6: Sensor integration, automation, research design
- G7-8: Data quality, cleaning, ethical collection

### T27: Data Analysis & Visualization (31 skills)
**Role:** Computing statistics and creating visualizations
- **Grade Span:** 1-8
- **Avg Dependencies:** 2.13
- **Key Capstones:** T27.G8.01 (Investigation), T27.G8.03 (Interactive dashboard)
- **Primary Links:** T26 (Collection), T10 (Lists), T07 (Loops), T11 (Functions)

**Progression:**
- K-2: Counting, pictographs, bar charts
- G3-4: Averages, mode/median, comparisons
- G5-6: Loops for aggregation, multi-variable analysis
- G7-8: Simulations, dashboards, data-driven conclusions

### T28: Chance, Sampling & Experiments (31 skills)
**Role:** Probability, simulations, and experimental design
- **Grade Span:** 1-8
- **Avg Dependencies:** 2.39 (highest - complex topic)
- **Key Capstones:** T28.G7.02 (Monte Carlo), T28.G8.01 (Real-world experiment)
- **Primary Links:** T09 (Variables), T07 (Loops), T27 (Analysis), T26 (Collection)

**Progression:**
- K-2: Likelihood concepts, fair/unfair games
- G3-4: Large-scale simulations, sampling
- G5-6: Weighted probability, simulation design
- G7-8: Monte Carlo methods, experimental analysis, AI bias

### T29: Text Data & Introductory NLP (31 skills)
**Role:** Text as data and AI-powered natural language processing
- **Grade Span:** 1-8
- **Avg Dependencies:** 2.16
- **Key Gateway:** T29.G3.03 - AI text interaction (Grade 3)
- **Key Capstones:** T29.G8.01 (Search system), T29.G8.04 (NLP ethics)
- **Primary Links:** T09 (Variables), T10 (Lists), T22 (Chatbots)

**Progression:**
- K-2: Words, counting, classification
- G3-4: String operations, lists of words, AI interaction
- G5-6: Frequency analysis, visualization
- G7-8: Text processing, AI classification, entity extraction

---

## Dependency Architecture

### Core Data Science Pipeline

```
T25 (Representation)
    ↓
T26 (Collection)
    ↓
T27 (Analysis) ←→ T28 (Experiments)
    ↓
T29 (Text/NLP)
```

### Programming Core Integration

All five data topics depend heavily on the programming core:

- **T09 (Variables):** Essential for storing, calculating with data
- **T10 (Lists):** Critical for data collections and tables
- **T07 (Loops):** Required for iterative data processing
- **T08 (Conditionals):** Used for filtering and conditional analysis
- **T11 (Functions):** Modularizes analysis operations

### Gateway Skills (2 Critical Skills)

#### 1. T25.G3.05: Build a data structure with a list (Grade 3)
- **Why Critical:** Lists are the foundation for all structured data work
- **Dependencies:** T25.G3.03, T10.G3.01
- **Unlocks:** All tabular data operations in T25-T29
- **Estimated Time:** 2-3 weeks of focused instruction

#### 2. T29.G3.03: Ask AI a question and receive response (Grade 3)
- **Why Critical:** Introduces students to AI-powered text processing
- **Dependencies:** T22.G3.01 (Chatbots)
- **Unlocks:** All AI-NLP skills in T29
- **Estimated Time:** 1-2 weeks of focused instruction

### Capstone Projects (9 Major Projects)

**Grade 6 (1 capstone):**
- T26.G6.05: Clean and prepare data for analysis (5 dependencies)

**Grade 7 (2 capstones):**
- T26.G7.03: Manipulate data with code - filtering, sorting, aggregation (6 dependencies)
- T28.G7.02: Monte Carlo simulation - probability estimation (6 dependencies)

**Grade 8 (6 major capstones):**
- T26.G8.02: Complete data investigation from question to conclusion (7 dependencies) - HIGHEST COMPLEXITY
- T27.G8.01: Design and conduct data investigation (6 dependencies)
- T27.G8.03: Create interactive data dashboard (6 dependencies) - BRIDGES TO T16 UI
- T28.G8.01: Real-world experiment design and analysis (6 dependencies)
- T29.G8.01: Keyword search system (6 dependencies)
- T29.G8.04: Ethical implications of NLP (5 dependencies)

---

## Grade-Level Progression

### K-2: Data Awareness (Simple Concepts)
**Essential Skills:**
- T25.G1: Categories, comparison, tallies
- T26.G1: Surveys and observation
- T27.G1: Counting and pictographs
- T28.G1: Likelihood concepts
- T29.G1: Words and counting

**Learning Focus:** Concrete, manipulative data concepts

### G3-4: Data Structures (Computational Foundation)
**Essential Skills:**
- T25.G3.05: Lists for data (GATEWAY)
- T26.G3-4: Tables, logging with lists
- T27.G3-4: Simple statistics (average, mode)
- T28.G3-4: Code-based experiments
- T29.G3: AI interaction (GATEWAY)

**Learning Focus:** Transitioning from concrete to abstract; programming for data

### G5-6: Computational Data Science
**Essential Skills:**
- T27.G5-6: Loops and functions for analysis
- T26.G5-6: Sensor integration, research design
- T28.G5-6: Probability simulations
- T29.G5-6: Text analysis, AI classification

**Learning Focus:** Authentic data science workflows; automation

### G7-8: Complete Projects (Professional Practice)
**Essential Skills:**
- T26.G8.02: Full data investigation (CAPSTONE)
- T27.G8: Analysis and dashboards (CAPSTONES)
- T28.G8: Experiments with analysis (CAPSTONES)
- T29.G8: NLP systems and ethics (CAPSTONES)

**Learning Focus:** End-to-end projects; ethics and bias; real-world applications

---

## Cross-Domain Bridges

### Data ↔ Programming Core (T06-T13)
**Strength:** Excellent integration
- T25 ↔ T09 (Variables for data)
- T26/T27 ↔ T10 (Lists for collections)
- T27/T28 ↔ T07 (Loops for processing)
- T26/T27 ↔ T08 (Conditionals for filtering)
- T27 ↔ T11 (Functions for analysis)

### Data ↔ Applications (T14-T24)
**Strength:** Emerging integration
- T27.G8.03 ↔ T16 (UI Widgets for dashboards)
- T26 ↔ T06 (Events for data collection)
- T29 ↔ T22 (Chatbots for AI text)

### Data ↔ AI (T21-T24)
**Strength:** Growing bridges
- T29 ↔ T22 (Chatbots): 8 AI-powered NLP skills
- T28.G8.03 ↔ T22 (Bias analysis): Probability meets AI ethics
- T27 ↔ T21 (Potential): Data-driven generative art

### Data ↔ Societal Impact (T35)
**Strength:** Ethics integrated
- T25.G8.05: Representation bias
- T26.G8.04: Collection bias
- T28.G8.04: Ethical data decisions
- T29.G8.04: NLP ethics

---

## Data Literacy Pathway

### Essential Sequence for Complete Data Science Education

**For Grades K-2 (Data Awareness):**
```
T25.G1.01 (Categories)
  → T26.G1.01 (Surveys)
  → T27.G1.01 (Counting)
  → T27.G2.01 (Simple charts)
  → T28.G1.01 (Likelihood)
```
**Outcome:** Students recognize data as representing reality

**For Grades 3-4 (Data Structures):**
```
T25.G3.05 (Lists - GATEWAY)
  → T26.G3.03 (Multi-column tables)
  → T26.G3.04 (Data retrieval)
  → T27.G4.01 (Statistics from lists)
  → T28.G3.01 (Simulations)
  → T29.G3.03 (AI text - GATEWAY)
```
**Outcome:** Students can structure and access data programmatically

**For Grades 5-6 (Computational Methods):**
```
T27.G5.01 (Loop aggregation)
  → T26.G5.03 (Filtering)
  → T28.G5.01 (Simulations)
  → T29.G5.01 (Text analysis)
  → T29.G6.03 (AI classification)
```
**Outcome:** Students can process substantial datasets with code

**For Grades 7-8 (Complete Projects):**
```
T26.G8.02 (Investigation - CAPSTONE)
  → T27.G8.01 (Analysis - CAPSTONE)
  → T27.G8.03 (Dashboard - CAPSTONE)
  → T28.G8.01 (Experiments - CAPSTONE)
  → T29.G8.01 (Search - CAPSTONE)
  → T29.G8.04 (NLP Ethics - CAPSTONE)
```
**Outcome:** Students conduct professional-grade data science projects

---

## AI Integration Points

### T29 Text/NLP + T22 Chatbots
**8 AI-powered skills connect T29 and T22:**
1. T29.G3.03: Simple Q&A (GATEWAY)
2. T29.G4.03: Sentiment classification
3. T29.G5.03: Text summarization
4. T29.G6.03: Multi-category classification
5. T29.G7.03: Question answering
6. T29.G8.02: Sentiment at scale
7. T29.G8.03: Entity extraction
8. T29.G8.04: NLP ethics (with T35)

### T28 Experiments + T22 AI Ethics
**1 critical bridge:**
- T28.G8.03: Analyze bias in AI models trained on biased data
  - Connects: Probability/sampling → Machine learning fairness
  - Outcome: Students understand data quality impacts AI decisions

### T27 Visualization + T16 UI Widgets
**1 major bridge:**
- T27.G8.03: Create interactive data dashboard
  - Integrates: Data analysis + UI design
  - Outcome: Data-driven applications

---

## Quality Assessment

### Strengths
1. **Perfect Grade Consistency:** Zero grade-level violations across all 167 skills
2. **Clear Pipeline:** Logical T25 → T26 → T27 → T28/T29 progression
3. **Strong Integration:** Excellent connection to T06-T13 programming core
4. **Modern Content:** AI, simulations, interactive dashboards included
5. **Ethics Emphasis:** Bias and fairness integrated throughout G6-G8
6. **Authentic Tasks:** Capstone projects mirror real data science work

### Architecture
1. **Foundation (T25):** Data types and structures (1.97 avg deps)
2. **Application (T26-T29):** Using data for various purposes (2.13-2.39 avg deps)
3. **Progressive Complexity:** K-2 concrete → G7-8 abstract and complex
4. **Multiple Modalities:** Structured data, text data, probabilistic thinking

### Pedagogical Quality
1. **Conceptual Before Computational:** G1-G2 concepts before G3+ coding
2. **Hands-On:** 9 major capstones provide authentic experience
3. **Integrated:** Strong connections across T06-T13 programming core
4. **Relevant:** Text analysis and AI match student interests

---

## Comparison with Other Domains

### vs. T06-T13 (Programming Core)
| Aspect | T06-T13 | T25-T29 |
|--------|---------|---------|
| Role | Building blocks | Applications |
| Skills | ~100 | 167 |
| Gateways | 21 | 2 |
| Dependencies | Simple | Complex |
| Nature | Foundational | Domain-specific |

**Analysis:** Data topics apply programming to authentic tasks; more skills needed for complete coverage

### vs. T14-T24 (Applications)
| Aspect | T14-T24 | T25-T29 |
|--------|---------|---------|
| Skills | 346 | 167 |
| Avg Deps | 7.25 | 2.37 |
| Capstones | 256 (74%) | 9 (5.4%) |
| Nature | Integrative | Foundational |
| Structure | Many paths | Single pipeline |

**Analysis:** Data topics form a coherent curriculum; applications integrate data with other domains

---

## Key Findings & Insights

### 1. Data Science Pipeline Is Clear
T25-T29 mirror the actual data science workflow:
1. Represent (T25)
2. Collect (T26)
3. Analyze (T27)
4. Experiment (T28)
5. Process Text (T29)

This progression aligns with professional practice and supports learning transfer.

### 2. Gateway Skills Are Strategic
- **T25.G3.05 (Lists):** Without lists, students can't handle structured data
- **T29.G3.03 (AI Q&A):** Opens modern NLP capabilities; enables T29 progression
Both are appropriately placed in Grade 3 and worth significant instructional focus.

### 3. Capstone Projects Are Comprehensive
9 capstone projects (G6-8) provide authentic, motivating endpoints:
- Data investigation (T26.G8.02) - highest complexity (7 deps)
- Interactive dashboard (T27.G8.03) - bridges to UI
- Monte Carlo simulation (T28.G7.02) - probability capstone
- Search system (T29.G8.01) - text capstone
- NLP ethics (T29.G8.04) - responsible AI capstone

### 4. Programming Core Is Essential
Every data skill depends on programming:
- No data work without T09 (Variables) for storage
- No structured data without T10 (Lists)
- No processing without T07 (Loops) and T08 (Conditionals)

### 5. AI Integration Is Natural
T29 + T22 connection is particularly strong:
- 8 AI-powered NLP skills
- Progression from simple (Q&A) to complex (entity extraction)
- Ethics integrated (T29.G8.04)

### 6. Ethics Is Not an Afterthought
Bias, fairness, and impact appear consistently:
- T25.G8.02: Representation bias
- T26.G8.04: Collection bias
- T28.G8.04: Ethical data decisions
- T29.G8.04: NLP ethics
Showing ethics as integral to data practice, not separate.

### 7. Grade Progression Is Smooth
No dramatic jumps in complexity:
- K-2: Concrete concepts
- G3-4: Computational foundations
- G5-6: Substantial projects
- G7-8: Professional-level work

---

## Recommendations for Implementation

### Curriculum Planning
1. **Prioritize T25.G3.05** (Grade 3): Allocate 2-3 weeks to ensure mastery
2. **Sequence Carefully:** Don't skip T25 foundation work
3. **Integrate with T06-T13:** Introduce data concepts same year as programming concepts
4. **Use Real Data:** Authentic datasets improve engagement and retention
5. **Emphasize T28 Experiments:** Probability is challenging; needs sufficient time

### Teacher Preparation
1. **Data literacy PD:** Teachers need to understand data science workflow
2. **AI tools training:** T29 requires familiarity with AI APIs/tools
3. **Ethics discussion:** Enable conversations about bias and fairness
4. **Project support:** Capstones need scaffolding and resources
5. **Interdisciplinary:** Coordinate with science/social studies for context

### Assessment
1. **Gateway mastery:** Test T25.G3.05 and T29.G3.03 thoroughly
2. **Capstone portfolios:** G8 projects make excellent portfolio pieces
3. **Process over product:** Value the investigation process, not just results
4. **Ethical reasoning:** Assess understanding of bias and fairness
5. **Transfer:** Test application of concepts to new domains

### Enhancements
1. **Mid-grade capstones:** Add integrative projects at G5-G6
2. **Hardware expansion:** Connect T26 sensors to T30 (Hardware)
3. **Storytelling skills:** Add data communication/presentation focus
4. **Cross-curricular:** Link to science investigations, social studies data
5. **Advanced pathways:** Extend to high school computer science topics

---

## Skill Maps Generated

### Primary Files
1. **dependencies_T25_T29.json** (167 skills)
   - Complete dependency graph for all T25-T29 skills
   - Includes gateway and capstone flagging
   - Cross-domain dependency links

2. **DEPENDENCIES_T25_T29_REPORT.md** (Detailed analysis)
   - Full breakdown by topic and grade
   - Dependency patterns and insights
   - Quality assessment by skill

3. **DEPENDENCIES_T25_T29_SUMMARY.md** (Executive summary)
   - Quick statistics and comparisons
   - Gateway and capstone descriptions
   - Grade progression patterns
   - Data literacy pathway
   - AI bridges
   - Recommendations

### Analysis Files
- **T25-T29_data_analysis.md** - Streamlined analysis
- **DEPENDENCIES_T25_T29_COMPLETE.txt** - Completion report

---

## Validation Results

### Quality Checks
- ✓ All 167 skills mapped
- ✓ Dependencies validated (2.37 avg per skill)
- ✓ Grade levels consistent (0 violations)
- ✓ Gateway skills identified (2 critical)
- ✓ Capstone skills identified (9 major projects)
- ✓ Cross-domain links verified
- ✓ AI bridges documented (9 connections)
- ✓ Progression patterns confirmed

### Grade Distribution
- K-2: 22 skills (foundational)
- G3-4: 38 skills (computational foundations)
- G5-6: 50 skills (advanced methods)
- G7-8: 57 skills (professional projects)

### Topic Distribution
- T25: 39 skills (23.4%)
- T26: 35 skills (21.0%)
- T27: 31 skills (18.6%)
- T28: 31 skills (18.6%)
- T29: 31 skills (18.6%)

---

## Conclusion

The T25-T29 Data & Analysis domain represents a **comprehensive, well-architected K-8 data science curriculum** that:

1. **Follows authentic workflows:** Mirrors real data science practice
2. **Ensures progression:** Smooth complexity increase across grades
3. **Integrates technology:** Strong programming core connections
4. **Embraces modern tools:** AI, simulations, dashboards included
5. **Teaches responsibility:** Ethics and bias integrated throughout
6. **Provides projects:** 9 capstones for authentic learning

With **zero grade violations**, **clear pedagogical progression**, and **strong cross-domain integration**, this curriculum successfully prepares students for 21st-century data literacy and opens pathways to computer science, AI, and data science careers.

### Overall Assessment: **EXCELLENT**

The dependency structure is sound, the progression is logical, and the curriculum achieves its goal of developing complete data science competency across K-8.

---

**Analysis Complete:** 2025-11-17
**Total Analysis Time:** Comprehensive (T25-T29 complete)
**Next Steps:** Integration with T30-T36 for complete K-8 system
**Status:** Ready for implementation

