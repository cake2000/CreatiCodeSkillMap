# T35 (Impacts & Ethics) - Phase 1 Optimization Summary

## Overview

Topic T35 has been optimized to improve skill granularity, fix dependencies, add scaffolding skills, and clarify descriptions. The optimization increased the total skill count from **50 to 71 skills** (+21 skills, +42%).

## Skill Count by Grade

| Grade | Before | After | Change |
|-------|--------|-------|--------|
| GK    | 4      | 4     | 0      |
| G1    | 4      | 4     | 0      |
| G2    | 4      | 4     | 0      |
| G3    | 4      | 4     | 0      |
| G4    | 5      | 7     | +2     |
| G5    | 4      | 8     | +4     |
| G6    | 8      | 13    | +5     |
| G7    | 11     | 17    | +6     |
| G8    | 6      | 10    | +4     |
| **Total** | **50** | **71** | **+21** |

## Key Changes Made

### 1. Skills Broken Down (9 skills → 28 sub-skills)

| Original Skill | Broken Into | Rationale |
|---------------|-------------|-----------|
| **T35.G4.01** (Analyze case studies of tech helping/harming communities) | T35.G4.01.01, T35.G4.01.02, T35.G4.01.03 | Split reading/categorizing, building viewer, and analyzing tradeoffs into separate skills |
| **T35.G5.01** (Examine global impacts of technology) | T35.G5.01.01, T35.G5.01.02, T35.G5.01.03 | Split research, comparison, and explanation of differential impacts |
| **T35.G6.01** (Apply ethics lenses) | T35.G6.01.01, T35.G6.01.02, T35.G6.01.03, T35.G6.01.04 | Each ethics lens (beneficence, fairness, autonomy) is now a separate skill, plus tool building |
| **T35.G6.03.01** (Test AI content generation tools) | T35.G6.03.01a, T35.G6.03.01b, T35.G6.03.01c | Split image testing, chatbot testing, and dashboard building |
| **T35.G7.01.01** (Conduct bias audits for AI perception) | T35.G7.01.01a, T35.G7.01.01b, T35.G7.01.01c | Split framework building, data analysis, and solution proposals |
| **T35.G7.03** (Evaluate transparency vs security tensions) | T35.G7.03.01, T35.G7.03.02, T35.G7.03.03 | Split simulator building, stakeholder analysis, and recommendation writing |
| **T35.G7.05.01** (Experiment with AI-generated media) | T35.G7.05.01a, T35.G7.05.01b, T35.G7.05.01c | Split art style experiments, commercial asset creation, and gallery building |
| **T35.G8.01** (Apply ethical frameworks to real proposals) | T35.G8.01.01, T35.G8.01.02, T35.G8.01.03 | Split tool building, proposal evaluation, and conflict resolution |
| **T35.G8.03.01** (Build impact assessment tool with scoring) | T35.G8.03.01a, T35.G8.03.01b, T35.G8.03.01c | Split into accessibility/privacy modules, wellbeing/cultural modules, and integration |

### 2. New Skills Added (3 new skills)

| New Skill ID | Name | Purpose |
|--------------|------|---------|
| **T35.G5.05** | Apply simple ethics questions to technology decisions | Scaffolds G6 formal ethics frameworks with simple questions (Does it help? Is it fair? Do users have control?) |
| **T35.G5.06** | Identify credible vs. non-credible online sources | Fills media literacy gap - teaches source evaluation (credentials, bias, corroboration) |
| **T35.G7.08** | Analyze deepfakes and synthetic media detection | Addresses misinformation literacy - teaches detection techniques and implications |

### 3. Dependency Fixes

| Skill | Issue | Fix |
|-------|-------|-----|
| **T35.G5.03** | Depended on T09.G3.03 (violated X-2 rule: G5 skill depending on G3) | Changed to T09.G4.01 (G4 skill, appropriate for G5) |
| **T35.G7.01** | Depended on old T35.G6.03.01 | Updated to T35.G6.03.01c (new broken-down skill) |
| **T35.G7.02** | Depended on old T35.G6.01 | Updated to T35.G6.01.04 (new broken-down skill) |
| **T35.G8.01.01** | Depended on old T35.G6.01 | Updated to T35.G6.01.04 (new broken-down skill) |
| **T35.G8.03.01a** | Depended on old T35.G6.01 | Updated to T35.G6.01.04 (new broken-down skill) |
| Multiple G5 skills | Depended on old T35.G4.01 | Updated to T35.G4.01.03 (tradeoffs skill) |

### 4. Skills Clarified (4 skills)

| Skill | Change |
|-------|--------|
| **T35.G2.02** | Added detail: "using picture cards and timers" |
| **T35.G2.03** | Expanded: Added "role-play responses to unkind messages" and "picture cards showing scenarios and speech bubbles" |
| **T35.G5.02** | Clarified: Added "structured debate formats (claim, evidence, reasoning)" and "reference specific studies or data" |
| **T35.G6.04** | Expanded: Added specific actions (interpret charts, identify patterns, propose interventions like wifi hotspots, device lending) |

### 5. Other Improvements

- **T35.G4.03.01**: Removed T35.G3.03 dependency (was unnecessary same-topic dependency)
- **T35.G4.04**: Added detail about button widgets and affirmations
- **T35.G7.02**: Clarified that storyboards can be digital or paper-based
- **T35.G7.06**: Added specific requirements (5+ open-ended questions, interview protocols)
- **T35.G7.07**: Added "digital divide statistics" as example dataset

## Skill ID Mapping (Old → New)

### Renamed/Split Skills
| Old ID | New ID(s) |
|--------|-----------|
| T35.G4.01 | T35.G4.01.01, T35.G4.01.02, T35.G4.01.03 |
| T35.G5.01 | T35.G5.01.01, T35.G5.01.02, T35.G5.01.03 |
| T35.G6.01 | T35.G6.01.01, T35.G6.01.02, T35.G6.01.03, T35.G6.01.04 |
| T35.G6.03.01 | T35.G6.03.01a, T35.G6.03.01b, T35.G6.03.01c |
| T35.G7.01.01 | T35.G7.01.01a, T35.G7.01.01b, T35.G7.01.01c |
| T35.G7.03 | T35.G7.03.01, T35.G7.03.02, T35.G7.03.03 |
| T35.G7.05.01 | T35.G7.05.01a, T35.G7.05.01b, T35.G7.05.01c |
| T35.G8.01 | T35.G8.01.01, T35.G8.01.02, T35.G8.01.03 |
| T35.G8.01.01 | T35.G8.01.04 (renamed, was AI chatbot analysis) |
| T35.G8.03.01 | T35.G8.03.01a, T35.G8.03.01b, T35.G8.03.01c |

### Unchanged Skills
All other T35 skills retained their original IDs:
- T35.GK.01 through T35.GK.04
- T35.G1.01 through T35.G1.04
- T35.G2.01 through T35.G2.04
- T35.G3.01 through T35.G3.04
- T35.G4.02, T35.G4.03.01, T35.G4.03.02, T35.G4.04
- T35.G5.02, T35.G5.03, T35.G5.04
- T35.G6.02, T35.G6.03.02, T35.G6.03.03, T35.G6.04, T35.G6.05.01, T35.G6.05.02
- T35.G7.01, T35.G7.02, T35.G7.04.01, T35.G7.04.02, T35.G7.05.02, T35.G7.06, T35.G7.07
- T35.G8.02, T35.G8.03.02, T35.G8.04

## Complete Skill List by Grade

### Kindergarten (4 skills)
- T35.GK.01: Identify a helpful use of technology
- T35.GK.02: Recognize signs of too much screen time
- T35.GK.03: Practice device sharing etiquette
- T35.GK.04: Choose safe sharing in role-play

### Grade 1 (4 skills)
- T35.G1.01: Sort good vs not-so-good choices and explain why
- T35.G1.02: Match feelings to technology experiences
- T35.G1.03: Recognize that people make technology choices
- T35.G1.04: Identify who to tell when uncomfortable online

### Grade 2 (4 skills)
- T35.G2.01: Compare benefits and harms of a tech tool
- T35.G2.02: Plan balanced tech schedules
- T35.G2.03: Practice online kindness scripts
- T35.G2.04: Distinguish public vs. private information

### Grade 3 (4 skills)
- T35.G3.01: Evaluate digital footprints
- T35.G3.02: Discuss how algorithms influence what we see
- T35.G3.03: Develop class guidelines for respectful communication
- T35.G3.04: Recognize when apps collect data

### Grade 4 (7 skills)
- T35.G4.01.01: Read and categorize tech impact case studies
- T35.G4.01.02: Build interactive case study viewer with widgets
- T35.G4.01.03: Identify tradeoffs in technology impacts
- T35.G4.02: Understand advertising/persuasion online
- T35.G4.03.01: Test game accessibility features
- T35.G4.03.02: Implement accessibility improvements
- T35.G4.04: Create a digital citizen pledge project

### Grade 5 (8 skills)
- T35.G5.01.01: Research technology impacts in one community
- T35.G5.01.02: Compare impacts across two communities
- T35.G5.01.03: Explain why technology impacts differ across contexts
- T35.G5.02: Debate digital well-being scenarios
- T35.G5.03: Analyze AI's differential impacts on workers and communities
- T35.G5.04: Visualize stakeholder impacts using data tools
- T35.G5.05: Apply simple ethics questions to technology decisions **(NEW)**
- T35.G5.06: Identify credible vs. non-credible online sources **(NEW)**

### Grade 6 (13 skills)
- T35.G6.01.01: Apply beneficence lens (does it help? who benefits?)
- T35.G6.01.02: Apply fairness lens (equal access and impact?)
- T35.G6.01.03: Apply autonomy lens (user control and choice?)
- T35.G6.01.04: Build ethics evaluation tool combining all lenses
- T35.G6.02: Analyze data privacy tradeoffs
- T35.G6.03.01a: Test AI image generation for bias
- T35.G6.03.01b: Test AI chatbots for accuracy and inclusivity
- T35.G6.03.01c: Build AI testing dashboard
- T35.G6.03.02: Synthesize comprehensive AI ethics guidelines
- T35.G6.03.03: Develop ethics guidelines for AI perception and assistance (T23-T24)
- T35.G6.04: Examine digital divide data
- T35.G6.05.01: Build consent form and data collection
- T35.G6.05.02: Implement data viewing and deletion controls

### Grade 7 (17 skills)
- T35.G7.01: Conduct bias audits for AI content generation (T21-T22)
- T35.G7.01.01a: Build systematic testing framework for AI perception
- T35.G7.01.01b: Analyze audit data and identify disparities
- T35.G7.01.01c: Propose solutions for detected bias
- T35.G7.02: Explore unintended consequences of new tech
- T35.G7.03.01: Build transparency vs. security tradeoff simulator
- T35.G7.03.02: Analyze stakeholder impacts at different transparency levels
- T35.G7.03.03: Justify transparency recommendations with evidence
- T35.G7.04.01: Build AI perception surveillance simulator
- T35.G7.04.02: Analyze privacy and safety impacts
- T35.G7.05.01a: Generate and analyze AI art in different styles
- T35.G7.05.01b: Create AI-generated commercial assets
- T35.G7.05.01c: Build AI art gallery with comparison data
- T35.G7.05.02: Debate ethics and propose policies
- T35.G7.06: Facilitate community discussions on AI-powered tech policy
- T35.G7.07: Compare honest vs. misleading data visualizations
- T35.G7.08: Analyze deepfakes and synthetic media detection **(NEW)**

### Grade 8 (10 skills)
- T35.G8.01.01: Build ethical evaluation tool
- T35.G8.01.02: Evaluate real proposals using the tool
- T35.G8.01.03: Resolve conflicts between ethical frameworks
- T35.G8.01.04: Analyze AI chatbots' impact on information literacy
- T35.G8.02: Draft equity-focused policy briefs for AI in education
- T35.G8.03.01a: Build accessibility and privacy assessment modules
- T35.G8.03.01b: Build wellbeing and cultural sensitivity modules
- T35.G8.03.01c: Integrate scoring and generate recommendations
- T35.G8.03.02: Apply tool to evaluate AI projects
- T35.G8.04: Lead peer workshops on responsible tech use

## Cross-Topic Dependencies Preserved

All dependencies to other topics (T01-T34, T36) were preserved exactly as they were. Only intra-topic (T35) dependencies were modified.

## Notes for Phase 2

The following cross-topic dependency issues should be reviewed in Phase 2:
1. Several G4 skills depend on G2 skills (borderline acceptable, at exactly X-2)
2. T35.G4.03.01 has many dependencies - consider if all are necessary
3. Some G6+ skills have dependencies on T24 and T25 without version numbers (e.g., T24.G5.01)

---

*Generated: 2025-11-25*
*Phase: 1 - Topic-Focused Optimization*
*Topic: T35 - Impacts & Ethics*
