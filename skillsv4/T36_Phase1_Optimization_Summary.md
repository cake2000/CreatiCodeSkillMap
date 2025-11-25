# T36 Phase 1 Optimization Summary
## Topic: Careers, Collaboration & Future Paths

### Overview
- **Original skill count**: 43 skills
- **New skill count**: 60 skills
- **Net change**: +17 skills (added through breakdown of overly broad skills)

---

## Key Changes

### 1. NEW SKILLS ADDED

#### Kindergarten (GK)
| ID | Skill | Rationale |
|----|-------|-----------|
| T36.GK.04 | Identify different ways people work together | Added to strengthen collaboration foundation; bridges turn-taking to team concepts |

#### Grade 1 (G1)
| ID | Skill | Rationale |
|----|-------|-----------|
| T36.G1.04 | Identify jobs that make apps and games | Scaffolding between general computer jobs and digital creation careers |

#### Grade 2 (G2)
| ID | Skill | Rationale |
|----|-------|-----------|
| T36.G2.05 | Practice polite communication in group work | Essential collaboration skill missing; bridges listening to feedback |

#### Grade 3 (G3)
| ID | Skill | Rationale |
|----|-------|-----------|
| T36.G3.05 | Practice giving and receiving helpful feedback | Critical scaffolding for future collaboration skills |

#### Grade 4 (G4)
| ID | Skill | Rationale |
|----|-------|-----------|
| T36.G4.05 | Identify skills needed for different tech jobs | Connects career exploration to skill development |

#### Grade 5 (G5)
| ID | Skill | Rationale |
|----|-------|-----------|
| T36.G5.04 | Lead a team check-in meeting | Scaffolds into formal stand-ups in G6 |
| T36.G5.05 | Explore tech careers that help others | Connects representation/inclusion work to career paths |

#### Grade 6 (G6) - Major Restructure
| ID | Skill | Rationale |
|----|-------|-----------|
| T36.G6.01 | Research software development careers | **BROKEN DOWN** from original T36.G6.01 which covered ALL 4 clusters |
| T36.G6.01.01 | Research hardware engineering careers | Part of career cluster breakdown |
| T36.G6.01.02 | Research data science careers | Part of career cluster breakdown |
| T36.G6.01.03 | Research AI and machine learning careers | Part of career cluster breakdown |
| T36.G6.01.04 | Compare computing career clusters | Synthesis skill after researching all clusters |
| T36.G6.04 | Run daily stand-up meetings | **BROKEN DOWN** from original T36.G6.02 |
| T36.G6.04.01 | Maintain a team task board | Part of agile practices breakdown |
| T36.G6.04.02 | Conduct sprint reviews | Part of agile practices breakdown |
| T36.G6.05.01 | Analyze job descriptions for soft skills and values | **BROKEN DOWN** from original T36.G6.03 |

#### Grade 7 (G7) - Restructure
| ID | Skill | Rationale |
|----|-------|-----------|
| T36.G7.01 | Prepare interview questions for tech professionals | **BROKEN DOWN** from original interview skill |
| T36.G7.01.01 | Conduct and summarize a career interview | Part of interview skill breakdown |
| T36.G7.01.03 | Discuss AI ethics and equity with tech professionals | Renamed/clarified from original |
| T36.G7.04 | Plan a lesson for younger coders | **BROKEN DOWN** from original mentoring skill |
| T36.G7.04.01 | Deliver a lesson to younger coders | Part of mentoring breakdown |
| T36.G7.05.01 | Use project tracking tools for team coordination | Added to expand collaboration tools |

#### Grade 8 (G8) - Major Restructure
| ID | Skill | Rationale |
|----|-------|-----------|
| T36.G8.01 | Identify high school courses for tech careers | **BROKEN DOWN** from original roadmap skill |
| T36.G8.01.01 | Plan extracurriculars and portfolio goals | Part of roadmap breakdown |
| T36.G8.01.02 | Build a multi-year career roadmap | Synthesis skill after planning components |
| T36.G8.02 | Assemble a project portfolio | **BROKEN DOWN** from original resume/portfolio skill |
| T36.G8.02.01 | Write a student resume | Part of professional prep breakdown |
| T36.G8.02.02 | Practice interview skills | Part of professional prep breakdown |
| T36.G8.03 | Research jobs at risk of AI displacement | **BROKEN DOWN** from original AI impact skill |
| T36.G8.03.01 | Research jobs augmented by AI | Part of AI impact breakdown |
| T36.G8.03.02 | Compare AI displacement vs augmentation patterns | Synthesis of AI impact research |
| T36.G8.05 | Plan a capstone retrospective | **BROKEN DOWN** from original retrospective skill |
| T36.G8.05.01 | Facilitate a capstone retrospective with stakeholders | Part of retrospective breakdown |

---

### 2. DEPENDENCY FIXES

#### Fixed Incorrect Reference
- **T36.G7.03** (Facilitate inclusive collaboration): Changed dependency from `T36.G5.01` (Map personal interests) to `T36.G4.03` (Role-play resolving disagreements) - the original reference was incorrect

#### Dependency Chain Improvements
- G6 career cluster skills now properly chain: G6.01 → G6.01.01 → G6.01.02 → G6.01.03 → G6.01.04
- G6 agile practices properly chain: G5.04 → G6.04 → G6.04.01/G6.04.02
- G8 career roadmap properly chains: G8.01 → G8.01.01 → G8.01.02
- G8 AI impact properly chains: G8.03 → G8.03.01 → G8.03.02 → G8.04 → G8.04.01

#### Renumbered Skills
- Original T36.G6.01.01 (Analyze representation) → T36.G6.02
- Original T36.G6.01.02 (Connect AI skills) → T36.G6.03
- Original T36.G6.02 (Stand-ups/task boards/sprints) → Broken into T36.G6.04, G6.04.01, G6.04.02
- Original T36.G6.03 (Job descriptions) → T36.G6.05, G6.05.01
- Original T36.G6.04 (Ethics clauses) → T36.G6.06
- Original T36.G6.05 (Portfolio) → T36.G6.07
- Original T36.G8.03.01 (AI community impacts) → T36.G8.04
- Original T36.G8.03.02 (Equitable AI proposal) → T36.G8.04.01
- Original T36.G8.04 (Capstone retrospectives) → T36.G8.05, G8.05.01

---

### 3. SKILL DESCRIPTION IMPROVEMENTS

All skill descriptions were enhanced to be:
- **More concrete and actionable** - specific deliverables defined
- **More assessable** - clear success criteria
- **Age-appropriate** - language adjusted for grade level
- **Numbered steps** - complex skills broken into clear sub-steps

Examples:
- K-2 skills now explicitly reference picture-based activities
- G3+ skills include specific outputs (charts, summaries, presentations)
- All skills now specify what students should produce, not just what they should learn

---

### 4. SKILLS BY GRADE (Final Count)

| Grade | Original | New | Change |
|-------|----------|-----|--------|
| GK | 3 | 4 | +1 |
| G1 | 3 | 4 | +1 |
| G2 | 4 | 5 | +1 |
| G3 | 4 | 5 | +1 |
| G4 | 4 | 5 | +1 |
| G5 | 3 | 5 | +2 |
| G6 | 8 | 12 | +4 |
| G7 | 7 | 10 | +3 |
| G8 | 7 | 10 | +3 |
| **Total** | **43** | **60** | **+17** |

---

### 5. PRESERVED CROSS-TOPIC DEPENDENCIES

All external dependencies were preserved exactly as they were:
- T01.GK.01, T03.GK.01, T03.G1.03, T03.G6.01
- T05.G3.01, T05.G3.02, T05.G5.01
- T06.G5.01
- T07.G2.01
- T08.G5.01, T08.G6.01a
- T10.G6.01
- T12.G6.01
- T13.G6.01
- T17.G6.01
- T18.G5.01
- T22.G6.01.01
- T24.G5.01
- T26.G6.01
- T34.G6.01

---

### 6. KEY PRINCIPLES APPLIED

1. **One skill = one learning objective**: Overly broad skills covering multiple topics were broken down
2. **Clear scaffolding**: Each skill builds on previous skills with proper dependencies
3. **IXL-style granularity**: Skills are now small enough for focused, assessable practice
4. **Grade-appropriate language**: K-2 uses simpler vocabulary; G6-8 introduces professional terminology
5. **X-2 rule compliance**: All intra-topic dependencies stay within 2 grade levels
6. **Concrete deliverables**: Every skill specifies what students should produce

---

## Next Steps (Phase 2)

Cross-topic dependency optimization will be handled in Phase 2, including:
- Verifying external topic dependencies are accurate
- Checking for missing cross-topic prerequisites
- Ensuring proper sequencing across all 36 topics
