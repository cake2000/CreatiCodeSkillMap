# T35 (Impacts & Ethics) Comprehensive Optimization Plan

## Executive Summary

This plan addresses critical dependency violations, improves skill descriptions to leverage CreatiCode features, and proposes new skills for better scaffolding. The plan maintains K-2 picture-based/unplugged activities while ensuring Grade 3-8 skills involve concrete block-based coding projects using CreatiCode's AI, widget, database, multiplayer, and data visualization capabilities.

---

## PART 1: DEPENDENCY FIXES (HIGH PRIORITY)

### 1.1 Same-Grade Dependency Removals

**Issue:** Skills should not depend on other skills within the same grade level.

#### Fix 1: T35.GK.04
**Problem:** Missing skill - there is NO T35.GK.04 but user instructions reference it.
**Action:** No fix needed - this appears to be an error in the initial prompt.

#### Fix 2: T35.G1.04
**Problem:** Missing skill - there is NO T35.G1.04 in the current file.
**Action:** No fix needed - this appears to be an error in the initial prompt.

#### Fix 3: T35.G2.04
**Problem:** Missing skill - there is NO T35.G2.04 in the current file.
**Action:** No fix needed - this appears to be an error in the initial prompt.

#### Fix 4: T35.G6.03.01
**Current Dependencies:**
- T35.G6.03: Develop ethics guidelines for AI content generation (T21-T22)
- T35.G5.03: Analyze AI's differential impacts on workers and communities

**Action:** REMOVE T35.G6.03 (same grade).

**After:**
```markdown
_Dependency:_
  * T35.G5.03: Analyze AI's differential impacts on workers and communities
```

**Rationale:** T35.G6.03.01 extends T35.G6.03 conceptually (perception/assistance ethics builds on content generation ethics), but should scaffold through prior grade rather than same-grade dependency. G5.03 provides sufficient foundation.

---

### 1.2 X-2 Rule Violations (Grade X Cannot Depend on Grade < X-2)

**Rule:** Grade X skills can only depend on grades X, X-1, or X-2.

#### Fix 5: T35.G4.02 (Grade 4)
**Current Dependencies:**
- T04.G2.01: Identify the repeating unit in a longer pattern (Grade 2) ← **VIOLATION**
- T35.G3.02: Discuss how algorithms influence what we see

**Issue:** Grade 4 depending on Grade 2 is acceptable (4-2=2), but the conceptual connection is weak. T04.G2.01 is about visual/sequence patterns, while T35.G4.02 is about recognizing persuasive patterns.

**Action:** REMOVE T04.G2.01 dependency.

**After:**
```markdown
_Dependency:_
  * T35.G3.02: Discuss how algorithms influence what we see
```

**Rationale:** T04.G2.01 (pattern recognition) doesn't conceptually support understanding advertising/persuasion. The dependency on T35.G3.02 (algorithms influencing content) is much more relevant for recognizing persuasive design patterns.

---

#### Fix 6: T35.G5.03 (Grade 5)
**Current Dependencies:**
- T04.G2.01: Identify the repeating unit in a longer pattern (Grade 2) ← **VIOLATION** (barely - 5-2=3, but allowed is X-2)
- T35.G4.01: Analyze case studies of tech helping/harming communities
- T35.G4.02: Understand advertising/persuasion online

**Issue:** Grade 5 depending on Grade 2 violates X-2 rule (5-2=3, but dependency is from Grade 2). Actually, this IS allowed (X-2 means grade X can depend on X-2). However, conceptually weak.

**Action:** REMOVE T04.G2.01 dependency.

**After:**
```markdown
_Dependency:_
  * T35.G4.01: Analyze case studies of tech helping/harming communities
  * T35.G4.02: Understand advertising/persuasion online
```

**Rationale:** AI impact analysis doesn't require pattern recognition from Grade 2. The ethical analysis scaffolds through T35's own progression.

---

#### Fix 7: T35.G8.01 (Grade 8)
**Current Dependencies:**
- T04.G2.01: Identify the repeating unit in a longer pattern (Grade 2) ← **MAJOR VIOLATION**
- T35.G7.01: Conduct bias audits for AI content generation (T21-T22)
- T35.G6.01: Apply ethics lenses (beneficence, fairness, autonomy)

**Issue:** Grade 8 depending on Grade 2 is WAY beyond X-2 rule (8-2=6, dependency from Grade 2 means 4 grades back).

**Action:** REMOVE T04.G2.01 dependency.

**After:**
```markdown
_Dependency:_
  * T35.G7.01: Conduct bias audits for AI content generation (T21-T22)
  * T35.G6.01: Apply ethics lenses (beneficence, fairness, autonomy)
```

**Rationale:** Ethical frameworks in Grade 8 don't need Grade 2 pattern recognition. The progression through T35.G6.01 and T35.G7.01 provides adequate scaffolding.

---

## PART 2: SKILL DESCRIPTION IMPROVEMENTS (MEDIUM PRIORITY)

### Goal
Grade 3-8 skills should specify which CreatiCode features they use. Currently many are too abstract/discussion-based. We'll make them concrete by incorporating:
- AI blocks (ChatGPT, image generation, speech recognition, text-to-speech)
- Widget blocks (labels, buttons, text inputs for UI)
- Database/cloud blocks (data privacy demonstrations)
- Multiplayer blocks (online safety in practice)
- Data visualization using table variables
- Computer vision (hand/body tracking for perception ethics)

---

### 2.1 Grade 3 Skills

#### Improvement 1: T35.G3.01 – Evaluate digital footprints

**Current Description:**
> Learners analyze sample posts (photos, comments) to determine what others might learn and whether it's safe to share.

**Problem:** Too abstract - "analyze sample posts" doesn't specify HOW students do this.

**NEW Description:**
```markdown
**Short name:** What does this post say about you?

**Description:** Students build a simple CreatiCode project that demonstrates digital footprints. Using widget blocks (labels and text input), they create a form where users type sample social media posts. The program uses ChatGPT blocks to analyze the post and identify what personal information (PII) might be revealed (location, age, school, etc.), then displays the analysis using label widgets. Students reflect on whether posts are safe to share based on the AI analysis.

**Challenge format:** Build-and-test project. Rubric checks: (1) widget-based input form, (2) ChatGPT block integration for PII detection, (3) output display showing identified information, (4) written reflection on post safety.
```

**Rationale:** Makes the skill concrete by using CreatiCode widgets + AI blocks. Students learn about digital footprints through hands-on coding.

---

#### Improvement 2: T35.G3.02 – Discuss how algorithms influence what we see

**Current Description:**
> Students learn that apps recommend content based on prior activity and reflect on how this shapes their time.

**Problem:** Pure discussion/lecture - no coding component.

**NEW Description:**
```markdown
**Short name:** Why does this video keep showing up?

**Description:** Students build a simple recommendation simulator using variables, conditionals, and data visualization. They create a project where clicking different content types (sports, music, gaming) increments counters in a table variable. Using if-blocks and comparison operators, the program displays different "recommended content" labels based on which counters are highest, demonstrating how algorithms track behavior to shape recommendations. Students document patterns they observe and reflect on how this shapes viewing habits.

**Challenge format:** Build-and-analyze project. Rubric checks: (1) click tracking with variables, (2) conditional recommendation logic, (3) table variable to display viewing history, (4) written reflection on algorithm influence.
```

**Rationale:** Uses core programming blocks (if-statements, variables) plus table variables for data visualization to make algorithmic recommendation concrete and observable.

---

#### Improvement 3: T35.G3.03 – Develop class guidelines for respectful communication

**Current Description:**
> Learners write simple rules (no spam, be kind, no PII) for classroom collaboration tools.

**Problem:** Mentions "chat code of conduct" but doesn't specify using actual chat tools.

**NEW Description:**
```markdown
**Short name:** Create a chat code of conduct

**Description:** Students build a simple moderated chat room using widget blocks (text input, labels, buttons) and AI moderation. They create a chat interface where users type messages into a text input widget. Before displaying messages in a label widget, the program uses ChatGPT AI moderation blocks to check for inappropriate content (spam, unkindness, PII). If content violates guidelines, a warning label appears instead. Students collaboratively write the guidelines that inform the AI moderation prompts.

**Challenge format:** Build-and-test project with peer testing. Rubric checks: (1) widget-based chat interface, (2) AI moderation block integration, (3) conditional display based on moderation results, (4) written community guidelines document.
```

**Rationale:** Uses widgets for UI and ChatGPT moderation blocks to create a working demonstration of community guidelines, making the concept tangible.

---

### 2.2 Grade 4 Skills

#### Improvement 4: T35.G4.01 – Analyze case studies of tech helping/harming communities

**Current Description:**
> Students read short case studies (drones delivering meds vs drones invading privacy) and discuss tradeoffs.

**Problem:** Pure reading/discussion - no CreatiCode component.

**Keep as-is but ADD coding extension:**

**ENHANCED Description:**
```markdown
**Short name:** Tech impact case cards

**Description:** Students read short case studies (drones delivering meds vs drones invading privacy) and discuss tradeoffs. THEN, they build an interactive case study viewer using widget blocks: buttons to select different case studies, and labels to display benefits/harms for each case. Students use table variables to organize multiple cases (columns: technology, benefits, harms, affected community) and practice navigating the data.

**Challenge format:** Case discussion worksheet + interactive viewer project. Auto-grading ensures mention of both benefits and harms in discussion; project rubric checks widget interface and table data organization.
```

**Rationale:** Adds a coding component to reinforce the analysis through data organization and UI design.

---

#### Improvement 5: T35.G4.02 – Understand advertising/persuasion online

**Current Description:**
> Learners identify ads, influencer promotions, and persuasive design patterns in sample apps.

**Problem:** "Sample apps" is vague - doesn't specify what students actually DO.

**NEW Description:**
```markdown
**Short name:** Spot sponsored content

**Description:** Students analyze actual CreatiCode community projects to identify persuasive design patterns (bright colors for "buy" buttons, countdown timers, celebrity endorsements in sprites). They create a project that demonstrates persuasive vs. informative design: two versions of the same app (e.g., a game invitation) where one uses persuasive tactics (flashing sprites, urgent language in labels) and one is neutral. Using widget blocks, they build both interfaces and have peers compare them, documenting which tactics they notice.

**Challenge format:** Comparative design project + analysis worksheet. Rubric checks: (1) two versions of interface with clear design differences, (2) widget usage for UI elements, (3) documentation of persuasive tactics identified, (4) peer testing results.
```

**Rationale:** Makes persuasion tangible by building examples using block coding and widgets, connecting to real design choices.

---

#### Improvement 6: T35.G4.03 – Reflect on accessibility/inclusion in games

**Current Description:**
> Students review a game for accessibility (color contrast, controls) and propose improvements.

**Problem:** Doesn't specify HOW to test or what CreatiCode features to use.

**ENHANCED Description:**
```markdown
**Short name:** Who can/can't play this game?

**Description:** Students review a CreatiCode game for accessibility barriers. They test: (1) Can you understand it without sound? (Test by muting), (2) Can you see important elements? (Use sprite size/color blocks to adjust contrast), (3) Can you control it without a mouse? (Add keyboard controls using when key pressed blocks), (4) Can you understand instructions? (Add text-to-speech using AI Speaker blocks). Students document barriers found and implement at least one improvement to a sample game using blocks (e.g., adding keyboard controls or text-to-speech instructions).

**Challenge format:** Accessibility audit worksheet + improvement implementation. Rubric checks: (1) identification of barriers across multiple categories, (2) implemented code improvement using relevant blocks, (3) before/after testing documentation, (4) proposed solutions for remaining barriers.
```

**Rationale:** Makes accessibility concrete through actual testing and code implementation using CreatiCode's blocks (events, AI text-to-speech, sprite properties).

---

### 2.3 Grade 5 Skills

#### Improvement 7: T35.G5.04 – [NEW SKILL - SEE PART 3]

This skill needs to be ADDED - see Part 3 for details on visualization.

---

### 2.4 Grade 6 Skills

#### Improvement 8: T35.G6.01 – Apply ethics lenses (beneficence, fairness, autonomy)

**Current Description:**
> Students evaluate a CreatiCode project using simple ethics lenses and document findings.

**Problem:** Unclear if they're analyzing an existing project or building one.

**ENHANCED Description:**
```markdown
**Short name:** Use an ethics checklist for apps

**Description:** Students apply three ethics lenses to evaluate CreatiCode projects (their own or community examples):
- **Beneficence**: Does this help people? Who benefits most? (Use ChatGPT blocks to analyze project purpose)
- **Fairness**: Can everyone use this equally? (Test with accessibility features like text-to-speech)
- **Autonomy**: Do users have control/choice? (Check for consent mechanisms using widget buttons)

Students build an ethics evaluation tool using widgets: dropdown menu to select lens, text input for project URL/name, and label to display evaluation questions. They document findings in a table variable with columns: Project, Lens, Evidence, Rating.

**Challenge format:** Evaluation tool project + completed assessment. Rubric checks: (1) widget-based evaluation interface, (2) table with multiple project assessments, (3) evidence-based ratings for each lens, (4) reflection on how lenses reveal different concerns.
```

**Rationale:** Makes abstract ethics lenses concrete through a systematic coding tool that structures the evaluation process.

---

#### Improvement 9: T35.G6.02 – Analyze data privacy tradeoffs

**Current Description:**
> Learners read mock privacy statements and decide whether the data collection is justified for the feature.

**Problem:** Reading comprehension exercise - no coding.

**NEW Description:**
```markdown
**Short name:** What data does this app collect and why?

**Description:** Students build an interactive privacy policy demonstrator using widgets and cloud data blocks. They create a sample app (e.g., a quiz or game) that collects data points (name, age, score, location). Using widget blocks, they build:
1. A consent interface with checkboxes (buttons) for each data type
2. Labels showing what each data type enables ("Location → Show local leaderboard")
3. A "Submit" button that only saves checked data to a cloud table variable

Students compare full-data vs. minimal-data versions to analyze which features truly need which data. They write privacy statements justifying each data collection.

**Challenge format:** Working privacy-conscious app + justification document. Rubric checks: (1) consent interface with widgets, (2) conditional data saving based on consent, (3) cloud/table variable usage, (4) written justification linking data to features.
```

**Rationale:** Makes privacy tradeoffs concrete by building a working consent system using widgets and data storage blocks.

---

#### Improvement 10: T35.G6.03 – Develop ethics guidelines for AI content generation (T21-T22)

**Current Description:**
> Students create ethical guidelines for AI image generation (T21) addressing bias in outputs, consent for training data, and cultural representation, and for AI chatbots (T22) addressing privacy, misinformation risks, and accessibility concerns.

**Problem:** Mentions T21-T22 tools but doesn't specify USING them.

**ENHANCED Description:**
```markdown
**Short name:** AI content generation ethics

**Description:** Students actively test CreatiCode's AI blocks to develop evidence-based guidelines:

**T21 (Image Generation):** Generate 10+ images with prompts like "doctor," "nurse," "CEO," "teacher" noting demographic representation. Document bias patterns in outputs.

**T22 (ChatGPT):** Test chatbot with various prompts to check: (1) Does it reveal training data sources? (2) Does it generate misinformation? (3) Does it understand different English dialects? Document quality variations.

Using findings, students create ethics guidelines in a widget-based interactive guide (buttons for each AI type, labels displaying guidelines). They include: when bias is acceptable, how to write inclusive prompts, and how to verify AI outputs.

**Challenge format:** AI testing documentation + interactive guidelines tool. Rubric checks: (1) systematic testing with 10+ examples per AI type, (2) documented bias/quality patterns, (3) widget-based guidelines interface, (4) actionable recommendations for responsible use.
```

**Rationale:** Changes from abstract guideline writing to evidence-based research using actual AI blocks, making bias and limitations observable.

---

### 2.5 Grade 7 Skills

#### Improvement 11: T35.G7.01 – Conduct bias audits for AI content generation (T21-T22)

**Current Description:**
> Students systematically audit T21 image generation for representation across demographics and T22 chatbots for response quality by dialect/topic. They measure disparities, analyze root causes, and propose mitigation strategies.

**Status:** ✅ **ALREADY EXCELLENT** - explicitly mentions using T21/T22 blocks systematically.

**Minor Enhancement:**
Add to description: "Students use table variables to log results (columns: Prompt, Demographic, Quality Rating) and create data visualizations showing disparity patterns."

---

#### Improvement 12: T35.G7.04 – Analyze societal impacts of AI perception technologies (Pairing with T23)

**Current Description:**
> Following T23 perception projects, students analyze real-world case studies of AI surveillance (facial recognition in schools, emotion detection at work, gesture tracking in public).

**Problem:** Should explicitly use T23 perception blocks.

**ENHANCED Description:**
```markdown
**Short name:** AI surveillance: community safety vs privacy

**Description:** Students use CreatiCode's T23 perception blocks (hand detection, body pose tracking) to build a simple surveillance simulator. They create a project that:
1. Uses hand detection to count people entering a "virtual space" (tracking when hands appear/disappear)
2. Uses body pose detection to identify "suspicious" movements (e.g., running vs. walking based on joint distances)
3. Logs all detections to a table variable with timestamps

Students then analyze their own data log as a case study: What privacy information is captured? Could it discriminate (e.g., different walking styles for different abilities)? They debate surveillance tradeoffs and write ethical guidelines for when such systems are justified.

**Challenge format:** Surveillance simulator + case study analysis. Rubric checks: (1) working perception block integration, (2) data logging to table, (3) privacy impact analysis of collected data, (4) equity-focused ethical guidelines with stakeholder perspectives.
```

**Rationale:** Makes surveillance impacts concrete by building and analyzing an actual perception-based system.

---

#### Improvement 13: T35.G7.05 – Debate ethical implications of AI media generation (Pairing with T21)

**Current Description:**
> Following T21 AI media projects, students hold structured debates on AI's impact on artists, photographers, and designers.

**Problem:** Should explicitly test T21 with artist impact in mind.

**ENHANCED Description:**
```markdown
**Short name:** AI-generated content and creative professions

**Description:** Students conduct AI art experiments using T21 (DALL-E) blocks:
1. Generate art "in the style of" famous artists (e.g., "landscape in Van Gogh style")
2. Generate commercial assets (logos, product images, stock photos)
3. Compare time required (AI seconds vs. human hours for similar quality)

They research artists' concerns through interviews/articles, then debate:
- Should AI art be copyrightable?
- Should training data sources be credited?
- How can artists adapt/benefit?

Students create a policy proposal using widgets (interactive policy viewer with buttons for different stakeholder positions).

**Challenge format:** AI art experiment documentation + structured debate + policy proposal project. Rubric checks: (1) systematic T21 testing across multiple styles/uses, (2) evidence from multiple stakeholder perspectives, (3) widget-based policy interface, (4) balanced recommendations.
```

**Rationale:** Grounds debate in hands-on experience with AI art generation, making abstract concerns tangible.

---

### 2.6 Grade 8 Skills

#### Improvement 14: T35.G8.03 – Design impact assessments for CreatiCode projects

**Current Description:**
> Students create rubrics assessing accessibility, privacy, wellbeing, and cultural sensitivity before publishing games/apps.

**Problem:** Doesn't specify building the rubric AS a CreatiCode project.

**NEW Description:**
```markdown
**Short name:** Pre-launch impact checklist

**Description:** Students build an interactive impact assessment tool using widgets and table variables. The tool includes:
1. **Input**: Text field for project name/URL (widget text input)
2. **Assessment categories** (widget buttons to select):
   - Accessibility (text-to-speech? keyboard controls? color contrast?)
   - Privacy (what data collected? user consent? secure storage?)
   - Wellbeing (time limits? addictive patterns? breaks encouraged?)
   - Cultural sensitivity (inclusive representation? stereotypes avoided?)
3. **Scoring interface**: Radio buttons/dropdowns for each checklist item
4. **Output**: Table variable showing assessment results + auto-generated recommendations using ChatGPT (e.g., "Project lacks keyboard controls - consider adding when key pressed blocks")

Students apply their tool to assess 3+ community projects and document findings.

**Challenge format:** Working assessment tool + assessment reports. Rubric checks: (1) comprehensive widget interface for all categories, (2) table variable data storage, (3) ChatGPT integration for recommendations, (4) completed assessments of 3+ projects with evidence.
```

**Rationale:** Makes impact assessment concrete by building it as an actual tool using widgets, tables, and AI blocks.

---

## PART 3: NEW SKILLS TO ADD (FOR BETTER SCAFFOLDING)

### 3.1 New Skill: T35.G3.04 – Recognize when apps collect data

**Placement:** Grade 3 (after T35.G3.03)

**Full Specification:**
```markdown
### T35.G3.04 – Recognize when apps collect data

_Dependency:_
  * T35.G3.03: Develop class guidelines for respectful communication
  * T09.G3.01: Create and use a numeric variable for score or count
  * T16.G3.01: Add a label widget to display text

**Short name:** What does this app know about me?

**Description:** Students build a simple app (quiz or game) that collects data using variables and widgets. They create visible indicators showing what's being collected: labels that update to show "You've answered 5 questions" (counter variable), "Your high score: 100" (performance data), "You clicked on: Animals" (preference tracking). Students then discuss what the app "knows" about users and whether users can see what's collected.

**Challenge format:** Build-and-document project. Rubric checks: (1) app with visible data collection (variables displayed via labels), (2) at least 3 data types tracked, (3) reflection on transparency and user awareness.

**CSTA:** E3‑CAS‑ET‑02.
```

**Rationale:** Bridges from guidelines (G3.03) to understanding data collection before digital footprints (current G3.01), making data collection concrete through building.

---

### 3.2 New Skill: T35.G5.04 – Visualize stakeholder impacts using data tools

**Placement:** Grade 5 (after T35.G5.03)

**Full Specification:**
```markdown
### T35.G5.04 – Visualize stakeholder impacts using data tools

_Dependency:_
  * T35.G5.03: Analyze AI's differential impacts on workers and communities
  * T19.G5.01: Store data in a Google Sheet using blocks
  * T16.G5.01: Build a simple survey using widgets

**Short name:** Who wins and loses from this technology?

**Description:** Students research a technology's impact on different stakeholders (e.g., AI chatbots impact: students, teachers, tutors, textbook companies). They collect impact data via widget-based surveys (rating scales 1-5: How much does this help/harm you?). Responses are stored in Google Sheets using cloud blocks. Students create data visualizations using table variables showing which groups benefit most/least, then discuss equity implications.

**Challenge format:** Survey project + data visualization + analysis. Rubric checks: (1) widget-based survey with 3+ stakeholder groups, (2) Google Sheets integration for data storage, (3) table-based visualization of results, (4) equity analysis identifying disparities.

**CSTA:** E5‑CAS‑ET‑02, CAS‑HC.
```

**Rationale:** Adds concrete data visualization skill to complement G5.03's AI impact analysis, using CreatiCode's Google Sheets integration.

---

### 3.3 New Skill: T35.G6.05 – Build consent mechanisms for data collection

**Placement:** Grade 6 (after T35.G6.02)

**Full Specification:**
```markdown
### T35.G6.05 – Build consent mechanisms for data collection

_Dependency:_
  * T35.G6.02: Analyze data privacy tradeoffs
  * T16.G6.01: Create forms with multiple widget types
  * T19.G6.01: Store and retrieve data from cloud tables

**Short name:** Ask before you collect

**Description:** Students build a project demonstrating informed consent using widgets and conditional logic. They create:
1. A clear consent form with checkboxes (button widgets) explaining each data type and why it's needed
2. Conditional data collection: only save data to cloud tables if consent checkbox is checked
3. A "view my data" button that retrieves and displays user's stored data
4. A "delete my data" button that removes records from cloud storage

Students test with peers and reflect on what makes consent "informed" (clear language, granular choices, revocable).

**Challenge format:** Working consent-based app. Rubric checks: (1) granular consent interface with widgets, (2) conditional cloud data storage based on consent, (3) data access and deletion features, (4) reflection on informed consent principles.

**CSTA:** MS‑CAS‑ET‑06.
```

**Rationale:** Adds a hands-on data ethics skill using widgets and cloud blocks, making abstract consent concepts concrete.

---

### 3.4 New Skill: T35.G7.07 – Compare honest vs. misleading data visualizations

**Placement:** Grade 7 (after T35.G7.06)

**Full Specification:**
```markdown
### T35.G7.07 – Compare honest vs. misleading data visualizations

_Dependency:_
  * T35.G6.04: Examine digital divide data
  * T19.G7.01: Create data visualizations using table variables
  * T16.G7.01: Build interactive data displays with widgets

**Short name:** Can data lie?

**Description:** Students analyze how data presentation affects interpretation. Given the same dataset (e.g., test scores over time), they create two visualizations using table variables and sprite graphics:
1. **Honest version**: Appropriate scale, full context, clear labels
2. **Misleading version**: Truncated y-axis, cherry-picked time range, or misleading colors

Using widget buttons, users can toggle between versions. Students document how design choices change perception and write guidelines for ethical data visualization.

**Challenge format:** Dual visualization project + ethics guidelines. Rubric checks: (1) same data shown two ways, (2) widget toggle between versions, (3) documented design differences and their effects, (4) ethical guidelines for data presentation.

**CSTA:** MS‑CAS‑ET‑05, DAA‑DI.
```

**Rationale:** Adds critical data literacy skill connecting to existing digital divide data analysis (G6.04), using visualization capabilities.

---

## PART 4: SKILLS TO DELETE/MERGE

**Recommendation:** ❌ **NO DELETIONS**

All current T35 skills serve distinct purposes:
- K-2 skills build foundational awareness (helpful tech, screen time, sharing)
- Grade 3-5 skills transition to analyzing impacts (footprints, algorithms, case studies)
- Grade 6-8 skills apply frameworks and conduct systematic audits

Even skills that currently lack coding components (like G4.01 case studies) can be enhanced with coding extensions (see Part 2) rather than deleted.

**Merge Consideration:** T35.G6.03 and T35.G6.03.01 could theoretically merge, but they serve pedagogical progression (content generation → perception/assistance). Keep separate.

---

## PART 5: SUMMARY OF CHANGES

### Dependency Fixes (7 changes)
1. ✅ T35.G6.03.01: Remove T35.G6.03 (same-grade dependency)
2. ✅ T35.G4.02: Remove T04.G2.01 (weak conceptual connection)
3. ✅ T35.G5.03: Remove T04.G2.01 (X-2 rule + weak connection)
4. ✅ T35.G8.01: Remove T04.G2.01 (major X-2 violation)

### Description Improvements (14 skills)
**Grade 3:**
- T35.G3.01: Add widgets + ChatGPT for PII detection
- T35.G3.02: Add recommendation simulator with variables/tables
- T35.G3.03: Add AI moderation blocks to chat

**Grade 4:**
- T35.G4.01: Add widget-based case viewer
- T35.G4.02: Build persuasive vs. informative designs
- T35.G4.03: Add accessibility testing with AI Speaker/controls

**Grade 6:**
- T35.G6.01: Build ethics evaluation tool with widgets
- T35.G6.02: Build privacy policy demonstrator with consent
- T35.G6.03: Test T21/T22 blocks to generate evidence-based guidelines

**Grade 7:**
- T35.G7.01: Add table visualization (minor enhancement)
- T35.G7.04: Build surveillance simulator with T23 blocks
- T35.G7.05: Conduct T21 art experiments before debate

**Grade 8:**
- T35.G8.03: Build assessment tool as widget/table project

### New Skills (4 additions)
1. ✅ T35.G3.04: Data collection recognition (widgets + variables)
2. ✅ T35.G5.04: Stakeholder visualization (Google Sheets + widgets)
3. ✅ T35.G6.05: Consent mechanisms (widgets + cloud blocks)
4. ✅ T35.G7.07: Honest vs. misleading visualizations (tables + widgets)

### Deletions
- None

---

## PART 6: IMPLEMENTATION CHECKLIST

### Phase 1: Dependency Fixes (Do First)
- [ ] Update T35.G6.03.01 dependencies (remove same-grade)
- [ ] Update T35.G4.02 dependencies (remove T04.G2.01)
- [ ] Update T35.G5.03 dependencies (remove T04.G2.01)
- [ ] Update T35.G8.01 dependencies (remove T04.G2.01)

### Phase 2: Add New Skills
- [ ] Add T35.G3.04 after T35.G3.03
- [ ] Add T35.G5.04 after T35.G5.03
- [ ] Add T35.G6.05 after T35.G6.02
- [ ] Add T35.G7.07 after T35.G7.06

### Phase 3: Update Descriptions (Grade by Grade)
- [ ] Update T35.G3.01-G3.03 descriptions
- [ ] Update T35.G4.01-G4.03 descriptions
- [ ] Update T35.G6.01-G6.03 descriptions
- [ ] Update T35.G7.01, G7.04, G7.05 descriptions
- [ ] Update T35.G8.03 description

### Phase 4: Validation
- [ ] Verify all dependencies follow X-2 rule
- [ ] Verify no same-grade dependencies
- [ ] Verify Grade 3-8 skills mention specific CreatiCode blocks
- [ ] Verify K-2 skills remain picture-based/unplugged
- [ ] Check cross-topic dependencies preserved (T06, T07, T08, T09, T16, T19, T21-T24)

---

## PART 7: RATIONALE SUMMARY

### Why These Changes?

**Dependency Fixes:**
- Same-grade dependencies create circular scaffolding (students can't learn A to learn A)
- X-2 violations mean students need skills from grades too far back (forgotten knowledge)
- T04.G2.01 dependencies were conceptually weak (visual patterns ≠ ethical reasoning)

**Description Improvements:**
- Current G3-8 skills too abstract ("discuss," "analyze," "reflect" without clear action)
- CreatiCode platform has powerful AI/widget/data tools that make ethics CONCRETE
- Building projects (not just discussing) deepens understanding and engagement
- Specifying blocks used ensures skills are assessable and aligned with platform

**New Skills:**
- Fill gaps in progression (data collection → privacy → consent → visualization ethics)
- Leverage underutilized CreatiCode features (Google Sheets, cloud blocks, table variables)
- Add data literacy (visualization ethics) to complement AI ethics focus

**Preserving Structure:**
- All current skills kept (none deleted) to maintain coverage
- Cross-topic dependencies preserved (T06-T09, T16, T19, T21-T24)
- K-2 unplugged philosophy maintained
- Grade 3+ coding focus strengthened

---

## APPENDIX: Quick Reference of CreatiCode Features Used

| Feature Category | Blocks/Tools | Skills That Use Them |
|-----------------|--------------|---------------------|
| **AI - ChatGPT** | ChatGPT request, moderation | G3.01, G3.03, G6.01, G6.03, G8.03 |
| **AI - Image Gen** | T21 DALL-E blocks | G6.03, G7.01, G7.05 |
| **AI - Speech** | Speech recognition, AI Speaker | G4.03 |
| **AI - Perception** | Hand detection, pose tracking (T23) | G7.04 |
| **Widgets** | Labels, buttons, text inputs | G3.01-G3.04, G4.01-G4.02, G5.04, G6.01-G6.05, G7.07, G8.03 |
| **Data - Tables** | Table variables, row/column ops | G3.02, G5.04, G6.01, G7.01, G7.04, G7.07, G8.03 |
| **Data - Cloud** | Google Sheets, cloud storage | G5.04, G6.02, G6.05 |
| **Core Blocks** | Variables, conditionals, events | G3.02, G3.04, G4.03, G6.05 |

---

## CONCLUSION

This optimization plan transforms T35 from a largely discussion-based topic into a hands-on, project-based curriculum that leverages CreatiCode's unique capabilities. By fixing dependency violations, specifying concrete block usage, and adding strategic new skills, we create a coherent K-8 progression where students:

- **K-2**: Build awareness through pictures and simple scenarios
- **Grade 3-5**: Use basic blocks + widgets to make impacts visible and interactive
- **Grade 6-8**: Systematically test AI tools, build ethical frameworks, and create assessment tools

The result is a topic that teaches not just ABOUT ethics and impacts, but teaches students to DEMONSTRATE, TEST, and EVALUATE ethical computing through actual coding projects.
