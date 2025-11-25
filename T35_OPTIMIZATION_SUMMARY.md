# T35 Impacts & Ethics - Optimization Summary

## Overview
**Original**: 50 skills
**Optimized**: 71 skills (+21 skills)

This optimization addressed critical issues while maintaining curriculum coherence and progression.

---

## Major Changes by Category

### 1. SKILLS BROKEN DOWN (9 overly broad skills → 28 focused skills)

#### Grade 4
**T35.G4.01: Analyze case studies** was doing TOO MUCH (reading + building + organizing + analyzing)
- **NEW T35.G4.01.01**: Read and categorize tech impact case studies
  - Focus: Organize case studies into table variables
- **NEW T35.G4.01.02**: Build interactive case study viewer with widgets
  - Focus: Create widget-based viewer for the data
- **NEW T35.G4.01.03**: Identify tradeoffs in technology impacts
  - Focus: Analyze tradeoffs using the viewer

#### Grade 5
**T35.G5.01: Examine global impacts** was combining research + comparison + explanation
- **NEW T35.G5.01.01**: Research technology impacts in one community
  - Focus: Deep dive into single community
- **NEW T35.G5.01.02**: Compare impacts across two communities
  - Focus: Comparative analysis
- **NEW T35.G5.01.03**: Explain why technology impacts differ across contexts
  - Focus: Causal reasoning about differences

#### Grade 6
**T35.G6.01: Apply ethics lenses** was teaching 3 frameworks + building tool + testing (WAY too broad)
- **NEW T35.G6.01.01**: Apply beneficence lens (does it help? who benefits?)
  - Focus: Single ethics framework - helping/harm
- **NEW T35.G6.01.02**: Apply fairness lens (equal access and impact?)
  - Focus: Single ethics framework - equity
- **NEW T35.G6.01.03**: Apply autonomy lens (user control and choice?)
  - Focus: Single ethics framework - user agency
- **NEW T35.G6.01.04**: Build ethics evaluation tool combining all lenses
  - Focus: Integration and tool building

**T35.G6.03.01: Test AI content generation tools** was testing 2 AI types with multiple protocols
- **NEW T35.G6.03.01a**: Test AI image generation for bias
  - Focus: T21 image generation testing
- **NEW T35.G6.03.01b**: Test AI chatbots for accuracy and inclusivity
  - Focus: T22 chatbot testing
- **NEW T35.G6.03.01c**: Build AI testing dashboard
  - Focus: Consolidate testing data with widgets

#### Grade 7
**T35.G7.01.01: Conduct bias audits for AI perception** was building + analyzing + proposing solutions
- **NEW T35.G7.01.01a**: Build systematic testing framework for AI perception
  - Focus: Create the testing infrastructure
- **NEW T35.G7.01.01b**: Analyze audit data and identify disparities
  - Focus: Data analysis and visualization
- **NEW T35.G7.01.01c**: Propose solutions for detected bias
  - Focus: Evidence-based recommendations

**T35.G7.03: Evaluate transparency vs security tensions** was demo + components + stakeholder analysis + recommendations
- **NEW T35.G7.03.01**: Build transparency vs. security tradeoff simulator
  - Focus: Create the interactive simulation
- **NEW T35.G7.03.02**: Analyze stakeholder impacts at different transparency levels
  - Focus: Multi-stakeholder analysis
- **NEW T35.G7.03.03**: Justify transparency recommendations with evidence
  - Focus: Evidence-based policy recommendations

**T35.G7.05.01: Experiment with AI-generated media** was multiple experiments + comparison + gallery
- **NEW T35.G7.05.01a**: Generate and analyze AI art in different styles
  - Focus: Artistic style experiments
- **NEW T35.G7.05.01b**: Create AI-generated commercial assets
  - Focus: Commercial use cases and time analysis
- **NEW T35.G7.05.01c**: Build AI art gallery with comparison data
  - Focus: Data visualization and pattern documentation

#### Grade 8
**T35.G8.01: Apply ethical frameworks to real proposals** was building tool + assessing + resolving conflicts
- **NEW T35.G8.01.01**: Build ethical evaluation tool
  - Focus: Create the assessment infrastructure
- **NEW T35.G8.01.02**: Evaluate real proposals using the tool
  - Focus: Apply tool to real cases
- **NEW T35.G8.01.03**: Resolve conflicts between ethical frameworks
  - Focus: Navigate framework conflicts with reasoning

**T35.G8.03.01: Build impact assessment tool** was very detailed with 4 categories + scoring + ChatGPT
- **NEW T35.G8.03.01a**: Build accessibility and privacy assessment modules
  - Focus: First two modules (accessibility + privacy)
- **NEW T35.G8.03.01b**: Build wellbeing and cultural sensitivity modules
  - Focus: Second two modules (wellbeing + cultural)
- **NEW T35.G8.03.01c**: Integrate scoring and generate recommendations
  - Focus: Integration + ChatGPT recommendations

---

### 2. NEW SKILLS ADDED (3 critical gaps filled)

#### Grade 5 - Scaffolding Gap
**NEW T35.G5.05: Apply simple ethics questions to technology decisions**
- **Why Added**: Grade 6 jumped directly to formal ethics frameworks (beneficence, fairness, autonomy) without scaffolding
- **Purpose**: Introduce simple versions of ethics questions in G5 to prepare for formal frameworks in G6
- **Content**: Does it help? Is it fair? Do users have control?
- **Dependencies**: T35.G5.01.03, T35.G5.02

#### Grade 5 - Media Literacy Gap
**NEW T35.G5.06: Identify credible vs. non-credible online sources**
- **Why Added**: Students need source evaluation skills before conducting research in higher grades
- **Purpose**: Teach critical evaluation of online information sources
- **Content**: Check credentials, date, evidence, bias, corroboration
- **Dependencies**: T35.G5.01.01 (uses research skills)

#### Grade 7 - Misinformation/Synthetic Media Gap
**NEW T35.G7.08: Analyze deepfakes and synthetic media detection**
- **Why Added**: Critical skill for digital literacy in AI era
- **Purpose**: Recognize synthetic media and understand implications for trust/misinformation
- **Content**: Detection techniques (blinking, lighting, audio-visual sync), build evaluation checklist
- **Dependencies**: T35.G7.05.01c (AI art gallery), T35.G5.06 (source credibility)

---

### 3. DEPENDENCY ISSUES FIXED

#### Critical X-2 Rule Violation
**T35.G5.03: Analyze AI's differential impacts on workers and communities**
- **OLD DEPENDENCY**: T09.G3.03 (G5 skill depending on G3 - violates X-2 rule)
- **NEW DEPENDENCY**: T09.G4.01 (G5 skill depending on G4 - appropriate)
- **Fix**: Changed to "Create and update a variable with meaningful names" which is appropriate prerequisite

---

### 4. UNCLEAR SKILLS CLARIFIED (4 skills)

#### T35.G2.02: Plan balanced tech schedules
- **OLD**: "Learners design a simple daily routine that includes device time, outdoor play, meals, and sleep."
- **NEW**: "Learners design a simple daily routine that includes device time, outdoor play, meals, and sleep using picture cards and timers."
- **Improvement**: Specifies concrete materials (picture cards, timers)

#### T35.G2.03: Practice online kindness scripts
- **OLD**: "Students role-play responses (ignore, block, tell adult) and positive messages."
- **NEW**: "Students role-play responses to unkind messages (ignore, block, tell adult) and practice writing positive messages. They use picture cards showing scenarios and speech bubbles to practice kind communication strategies."
- **Improvement**: Clarifies what they're responding to and adds concrete materials

#### T35.G5.02: Debate digital well-being scenarios
- **OLD**: "Students debate policy scenarios (device-free times, notifications) referencing evidence on focus and health."
- **NEW**: "Students debate policy scenarios (device-free times, notifications settings, screen time limits) using evidence from research on focus, sleep, and mental health. They reference specific studies or data and use structured debate formats (claim, evidence, reasoning) to support their positions."
- **Improvement**: Clarifies "referencing evidence" means using structured debate format with research

#### T35.G6.04: Examine digital divide data
- **OLD**: "Learners interpret charts (broadband availability, device ownership) and propose community actions."
- **NEW**: "Students interpret data charts and graphs showing digital divide indicators (broadband availability by region/income, device ownership by demographic, internet speeds, digital literacy rates). They identify patterns and disparities, then propose specific, actionable community interventions to address access gaps (community wifi hotspots, device lending programs, digital literacy classes)."
- **Improvement**: Specific data types, specific analysis tasks, specific intervention examples

---

## Summary Statistics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| **Total Skills** | 50 | 71 | +21 (+42%) |
| **GK Skills** | 4 | 4 | 0 |
| **G1 Skills** | 4 | 4 | 0 |
| **G2 Skills** | 4 | 4 | 0 |
| **G3 Skills** | 4 | 4 | 0 |
| **G4 Skills** | 5 | 7 | +2 |
| **G5 Skills** | 4 | 8 | +4 |
| **G6 Skills** | 8 | 13 | +5 |
| **G7 Skills** | 11 | 17 | +6 |
| **G8 Skills** | 6 | 10 | +4 |
| **Skills Broken Down** | 9 | 28 | +19 |
| **Skills Added (New)** | 0 | 3 | +3 |
| **Skills Clarified** | 0 | 4 | +4 |
| **Dependency Fixes** | 0 | 1 | +1 |
