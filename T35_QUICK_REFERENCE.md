# T35 Optimization Quick Reference

## At a Glance

- **Dependency Fixes**: 4 changes
- **Description Improvements**: 13 skills enhanced
- **New Skills**: 4 additions
- **Deletions**: 0
- **Total Changes**: 21 modifications to T35

---

## Dependency Fixes (Copy-Paste Ready)

### 1. T35.G4.02
**REMOVE:**
```
  * T04.G2.01: Identify the repeating unit in a longer pattern
```

**KEEP:**
```
  * T35.G3.02: Discuss how algorithms influence what we see
```

---

### 2. T35.G5.03
**REMOVE:**
```
  * T04.G2.01: Identify the repeating unit in a longer pattern
```

**KEEP:**
```
  * T35.G4.01: Analyze case studies of tech helping/harming communities
  * T35.G4.02: Understand advertising/persuasion online
```

---

### 3. T35.G6.03.01
**REMOVE:**
```
  * T35.G6.03: Develop ethics guidelines for AI content generation (T21-T22)
```

**KEEP:**
```
  * T35.G5.03: Analyze AI's differential impacts on workers and communities
```

---

### 4. T35.G8.01
**REMOVE:**
```
  * T04.G2.01: Identify the repeating unit in a longer pattern
```

**KEEP:**
```
  * T35.G7.01: Conduct bias audits for AI content generation (T21-T22)
  * T35.G6.01: Apply ethics lenses (beneficence, fairness, autonomy)
```

---

## New Skills to Add

### T35.G3.04 (Insert after T35.G3.03)

```markdown
### T35.G3.04 – Recognize when apps collect data

_Dependency:_
  * T35.G3.03: Develop class guidelines for respectful communication
  * T09.G3.01: Create and use a numeric variable for score or count
  * T16.G3.01: Add a label widget to display text

- **Short name:** What does this app know about me?
- **Description:** Students build a simple app (quiz or game) that collects data using variables and widgets. They create visible indicators showing what's being collected: labels that update to show "You've answered 5 questions" (counter variable), "Your high score: 100" (performance data), "You clicked on: Animals" (preference tracking). Students then discuss what the app "knows" about users and whether users can see what's collected.
- **Challenge format:** Build-and-document project. Rubric checks: (1) app with visible data collection (variables displayed via labels), (2) at least 3 data types tracked, (3) reflection on transparency and user awareness.
- **CSTA:** E3‑CAS‑ET‑02.
```

---

### T35.G5.04 (Insert after T35.G5.03)

```markdown
### T35.G5.04 – Visualize stakeholder impacts using data tools

_Dependency:_
  * T35.G5.03: Analyze AI's differential impacts on workers and communities
  * T19.G5.01: Store data in a Google Sheet using blocks
  * T16.G5.01: Build a simple survey using widgets

- **Short name:** Who wins and loses from this technology?
- **Description:** Students research a technology's impact on different stakeholders (e.g., AI chatbots impact: students, teachers, tutors, textbook companies). They collect impact data via widget-based surveys (rating scales 1-5: How much does this help/harm you?). Responses are stored in Google Sheets using cloud blocks. Students create data visualizations using table variables showing which groups benefit most/least, then discuss equity implications.
- **Challenge format:** Survey project + data visualization + analysis. Rubric checks: (1) widget-based survey with 3+ stakeholder groups, (2) Google Sheets integration for data storage, (3) table-based visualization of results, (4) equity analysis identifying disparities.
- **CSTA:** E5‑CAS‑ET‑02, CAS‑HC.
```

---

### T35.G6.05 (Insert after T35.G6.02)

```markdown
### T35.G6.05 – Build consent mechanisms for data collection

_Dependency:_
  * T35.G6.02: Analyze data privacy tradeoffs
  * T16.G6.01: Create forms with multiple widget types
  * T19.G6.01: Store and retrieve data from cloud tables

- **Short name:** Ask before you collect
- **Description:** Students build a project demonstrating informed consent using widgets and conditional logic. They create: (1) A clear consent form with checkboxes (button widgets) explaining each data type and why it's needed, (2) Conditional data collection: only save data to cloud tables if consent checkbox is checked, (3) A "view my data" button that retrieves and displays user's stored data, (4) A "delete my data" button that removes records from cloud storage. Students test with peers and reflect on what makes consent "informed" (clear language, granular choices, revocable).
- **Challenge format:** Working consent-based app. Rubric checks: (1) granular consent interface with widgets, (2) conditional cloud data storage based on consent, (3) data access and deletion features, (4) reflection on informed consent principles.
- **CSTA:** MS‑CAS‑ET‑06.
```

---

### T35.G7.07 (Insert after T35.G7.06)

```markdown
### T35.G7.07 – Compare honest vs. misleading data visualizations

_Dependency:_
  * T35.G6.04: Examine digital divide data
  * T19.G7.01: Create data visualizations using table variables
  * T16.G7.01: Build interactive data displays with widgets

- **Short name:** Can data lie?
- **Description:** Students analyze how data presentation affects interpretation. Given the same dataset (e.g., test scores over time), they create two visualizations using table variables and sprite graphics: (1) Honest version: Appropriate scale, full context, clear labels, (2) Misleading version: Truncated y-axis, cherry-picked time range, or misleading colors. Using widget buttons, users can toggle between versions. Students document how design choices change perception and write guidelines for ethical data visualization.
- **Challenge format:** Dual visualization project + ethics guidelines. Rubric checks: (1) same data shown two ways, (2) widget toggle between versions, (3) documented design differences and their effects, (4) ethical guidelines for data presentation.
- **CSTA:** MS‑CAS‑ET‑05, DAA‑DI.
```

---

## Description Enhancement Summary

| Skill | Current Issue | Fix |
|-------|--------------|-----|
| **T35.G3.01** | Too abstract | Add widgets + ChatGPT for PII detection demo |
| **T35.G3.02** | Pure discussion | Build recommendation simulator with variables/tables |
| **T35.G3.03** | No actual chat | Add AI moderation blocks to working chat |
| **T35.G4.01** | Just reading | Add interactive case viewer with widgets/tables |
| **T35.G4.02** | Vague "sample apps" | Build persuasive vs. informative interface comparison |
| **T35.G4.03** | No testing method | Add accessibility testing (mute, resize, keyboard, TTS) |
| **T35.G6.01** | Unclear if building/analyzing | Build ethics evaluation tool with widgets |
| **T35.G6.02** | Just reading policies | Build working privacy/consent demonstrator |
| **T35.G6.03** | Doesn't use T21/T22 | Test AI blocks systematically for bias evidence |
| **T35.G7.01** | Already good | Minor: add table visualization mention |
| **T35.G7.04** | Should use T23 | Build surveillance simulator with perception blocks |
| **T35.G7.05** | Should use T21 | Conduct AI art experiments before debate |
| **T35.G8.03** | Just create rubric | Build assessment tool AS widget/table project |

---

## CreatiCode Features by Grade

### Grade 3
- Variables (counters, tracking)
- Conditionals (if-then logic)
- Widget blocks (labels, text input, buttons)
- Table variables (basic data display)
- ChatGPT blocks (simple queries)

### Grade 4
- Widget interfaces (multi-element UI)
- Table variables (data organization)
- Sprite properties (accessibility: size, color)
- Event blocks (keyboard controls)
- AI Speaker (text-to-speech)

### Grade 5
- Google Sheets integration
- Widget surveys (forms)
- Table visualization
- Data analysis

### Grade 6
- Cloud data storage
- Conditional data logic
- Complex widget forms
- ChatGPT analysis
- T21/T22 AI blocks (systematic testing)

### Grade 7
- T23 perception blocks (hand/body tracking)
- T21 image generation (systematic testing)
- Advanced table operations
- Data visualization ethics
- Multi-version projects (A/B comparison)

### Grade 8
- Integration projects (widgets + tables + AI)
- ChatGPT recommendations
- Complex data tools
- Assessment frameworks

---

## Validation Checklist

✅ **Dependency Rules:**
- No same-grade dependencies (except removed)
- All follow X-2 rule (Grade X only depends on X, X-1, X-2)
- Cross-topic dependencies preserved (T04, T06-T09, T16, T19, T21-T24)

✅ **Content Rules:**
- K-2 remain picture-based/unplugged
- Grade 3-8 specify actual CreatiCode blocks used
- All skills mention concrete activities, not just "discuss"

✅ **Coverage:**
- All CSTA standards preserved
- AI ethics (T21-T24) thoroughly covered
- Data ethics (privacy, visualization) covered
- Accessibility covered
- Digital wellbeing covered
- Equity/justice lens integrated

---

## One-Sentence Summary of Each Change

1. **G3.01**: Build PII detector using widgets + ChatGPT
2. **G3.02**: Build recommendation simulator with variables/if-blocks
3. **G3.03**: Build moderated chat with AI moderation blocks
4. **G3.04** ⭐NEW: Build app showing visible data collection
5. **G4.01**: Add interactive case viewer with widgets
6. **G4.02**: Build persuasive vs. neutral interfaces
7. **G4.03**: Test accessibility features (mute, keyboard, TTS)
8. **G5.04** ⭐NEW: Build stakeholder survey + Google Sheets visualization
9. **G6.01**: Build ethics evaluation tool
10. **G6.02**: Build privacy consent demonstrator
11. **G6.03**: Test T21/T22 blocks systematically for bias
12. **G6.05** ⭐NEW: Build consent mechanism with cloud storage
13. **G7.01**: Add table visualization (minor)
14. **G7.04**: Build surveillance simulator with T23 blocks
15. **G7.05**: Conduct T21 art experiments before debate
16. **G7.07** ⭐NEW: Build honest vs. misleading visualization comparison
17. **G8.03**: Build assessment tool as interactive project

---

## Key Principles Applied

1. **Concrete > Abstract**: Every "discuss" or "analyze" now includes building something
2. **Use the Platform**: Leverage CreatiCode's unique AI/widget/cloud features
3. **Evidence-Based**: Test AI blocks to see bias, don't just read about it
4. **Scaffolded**: Each grade builds on previous with clear progression
5. **Assessable**: Clear rubrics based on what students build, not just discuss
6. **Integrated**: Connect ethics to actual coding skills (T21-T24, widgets, data)

---

## Notes for Implementation

- **Dependencies**: Fix these FIRST (4 changes) before touching descriptions
- **New Skills**: Add these SECOND (4 additions) to maintain numbering stability
- **Descriptions**: Update LAST (13 enhancements) grade by grade
- **Testing**: After changes, verify all T16, T19, T21-T24 dependencies still valid
- **Documentation**: Note that some enhanced skills assume T16 (widgets) and T19 (data) exist in those grades - verify those topics are developed appropriately
