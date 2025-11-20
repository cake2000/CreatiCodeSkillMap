# Grade 5 Skills Extraction - Complete Analysis

## Overview

This analysis extracted **all 172 Grade 5 skills** from the CreatiCode Skill Map (allskills.md).

## Generated Files

### 1. G5_COMPLETE_REPORT.txt (89KB)
**Complete detailed report with full information for each skill**

Contains:
- Full skill ID, name, description, and dependencies for all 172 G5 skills
- Organized by 35 topics
- Each dependency includes both ID and description
- 2,092 lines of detailed content

**Use this file for:** Complete reference, understanding skill details, analyzing descriptions

---

### 2. G5_DEPENDENCY_ANALYSIS.txt (12KB)
**Statistical analysis of dependencies across all G5 skills**

Key findings:
- **Total G5 Skills:** 172
- **Total Dependencies:** 320
- **Average Dependencies per Skill:** 1.86
- **All skills have dependencies** (100%)

**Dependencies by Grade:**
- G3: 201 dependencies (62.8%) - Most common
- G4: 80 dependencies (25.0%)
- G1: 36 dependencies (11.3%)
- G2: 2 dependencies (0.6%)
- G5: 1 dependency (0.3%)

**Most Referenced Skills (Top 5):**
1. T07.G3.05 - Referenced 38 times
2. T08.G3.05 - Referenced 28 times
3. T06.G3.08 - Referenced 25 times
4. T01.G3.01 - Referenced 22 times
5. T09.G3.04 - Referenced 21 times

**Dependency Distribution:**
- 3 Dependencies: 19 skills (11.0%)
- 2 Dependencies: 110 skills (64.0%)
- 1 Dependency: 43 skills (25.0%)

**Use this file for:** Understanding dependency patterns, identifying key prerequisite skills, analyzing curriculum structure

---

### 3. G5_SKILLS_SUMMARY.txt (20KB)
**Compact one-line summary of each skill with dependency count**

Format per skill:
```
ID: Skill Name [X deps]
```

Example:
```
T01.G5.01: Match a word description to a flowchart [1 deps]
```

**Use this file for:** Quick reference, overview of all skills, scanning skill names

---

## Topic Breakdown

172 Grade 5 skills across 35 topics:

| Topic | Count | Topic Name |
|-------|-------|------------|
| T01 | 10 | Everyday Algorithms |
| T02 | 6 | Algorithm Diagrams |
| T03 | 5 | Problem Decomposition |
| T04 | 5 | Algorithm Patterns |
| T05 | 6 | Human-Centered Design |
| T06 | 6 | Events & Sequences |
| T07 | 4 | Loops |
| T08 | 4 | Conditions & Logic |
| T09 | 8 | Variables & Expressions |
| T10 | 5 | Lists & Tables |
| T11 | 4 | Functions & Procedures |
| T12 | 4 | Organizing Programs |
| T13 | 4 | Testing, Debugging & Error Handling |
| T14 | 10 | 2D Games |
| T15 | 8 | Stories & Animation |
| T16 | 4 | User Interfaces |
| T17 | 11 | 2D Motion & Physics |
| T18 | 6 | 3D Worlds & Games |
| T19 | 5 | Multiplayer Apps |
| T20 | 5 | Algorithmic Art & Creative Coding |
| T21 | 1 | AI Media |
| T22 | 1 | Chatbots & Prompting |
| T23 | 4 | AI Perception |
| T24 | 5 | XO & Generative AI Practices |
| T25 | 4 | Data Representation |
| T26 | 4 | Data Collection & Logging |
| T27 | 3 | Data Analysis & Storytelling |
| T28 | 4 | Chance & Simulations |
| T29 | 4 | Text Data & NLP Foundations |
| T30 | 4 | Devices & Hardware Systems |
| T31 | 5 | Internet & Cloud |
| T32 | 4 | Cybersecurity & Digital Safety |
| T34 | 3 | Computing History |
| T35 | 3 | Impacts & Ethics |
| T36 | 3 | Careers, Collaboration & Future Paths |

**Note:** Topics T33 has no G5 skills

## Key Insights

1. **Strong G3 Foundation**: 62.8% of dependencies are on Grade 3 skills, showing G5 builds heavily on G3 concepts

2. **Core Skills**: The most referenced skills are:
   - T07.G3.05 (Loops) - 38 references
   - T08.G3.05 (Conditions) - 28 references
   - T06.G3.08 (Events) - 25 references

3. **Dependency Pattern**: Most skills (64%) have exactly 2 dependencies, suggesting balanced prerequisite structure

4. **Topic Coverage**: Wide coverage across 35 topics, with largest concentrations in:
   - T17 (2D Motion & Physics): 11 skills
   - T01 (Everyday Algorithms): 10 skills
   - T14 (2D Games): 10 skills

5. **Computational Thinking Focus**: Heavy emphasis on T09 (Variables), T07 (Loops), T06 (Events), and T08 (Conditions) as foundational topics

## Data Extraction Scripts

Three Python scripts were created:
- `extract_g5.py` - Extracts all G5 skills with full details
- `analyze_g5_dependencies.py` - Analyzes dependency patterns
- `create_g5_summary.py` - Creates compact summary view

## Source Data

- **Source File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`
- **File Size:** 569.6KB
- **Extraction Date:** November 20, 2025
- **Total Skills Extracted:** 172

## Usage

For detailed skill information, open `G5_COMPLETE_REPORT.txt`

For dependency analysis and statistics, see `G5_DEPENDENCY_ANALYSIS.txt`

For quick reference lookup, use `G5_SKILLS_SUMMARY.txt`
