# T35 Exact Changes for skillsv4/skills_T35_impacts.md

This document provides the exact changes to apply to `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/skills_T35_impacts.md`.

---

## CHANGE 1: T35.G3.01 - Replace entire skill section

**FIND (lines 129-140):**
```markdown
### T35.G3.01 – Evaluate digital footprints

_Dependency:_
  * T35.G2.01: Compare benefits and harms of a tech tool
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop


- **Short name:** What does this post say about you?
- **Description:** Learners analyze sample posts (photos, comments) to determine what others might learn and whether it's safe to share.
- **Challenge format:** Concept Q&A. Auto-grading checks identification of PII and judgement statements.
- **CSTA:** E3‑CAS‑ET‑02, T32 dependency.
```

**REPLACE WITH:**
```markdown
### T35.G3.01 – Evaluate digital footprints

_Dependency:_
  * T35.G2.01: Compare benefits and harms of a tech tool
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T16.G3.01: Add a label widget to display text
  * T22.G3.01: Use ChatGPT blocks for simple queries


- **Short name:** What does this post say about you?
- **Description:** Students build a simple CreatiCode project that demonstrates digital footprints. Using widget blocks (labels and text input), they create a form where users type sample social media posts. The program uses ChatGPT blocks to analyze the post and identify what personal information (PII) might be revealed (location, age, school, etc.), then displays the analysis using label widgets. Students reflect on whether posts are safe to share based on the AI analysis.
- **Challenge format:** Build-and-test project. Rubric checks: (1) widget-based input form, (2) ChatGPT block integration for PII detection, (3) output display showing identified information, (4) written reflection on post safety.
- **CSTA:** E3‑CAS‑ET‑02, T32 dependency.
```

---

## CHANGE 2: T35.G3.02 - Replace description and challenge format

**FIND (lines 142-153):**
```markdown
### T35.G3.02 – Discuss how algorithms influence what we see

_Dependency:_
  * T35.G3.01: Evaluate digital footprints
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Why does this video keep showing up?
- **Description:** Students learn that apps recommend content based on prior activity and reflect on how this shapes their time.
- **Challenge format:** Short reflection referencing cause/effect. Auto-grading ensures mention of recommendations.
- **CSTA:** E3‑CAS‑ET‑02.
```

**REPLACE WITH:**
```markdown
### T35.G3.02 – Discuss how algorithms influence what we see

_Dependency:_
  * T35.G3.01: Evaluate digital footprints
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Why does this video keep showing up?
- **Description:** Students build a simple recommendation simulator using variables, conditionals, and data visualization. They create a project where clicking different content types (sports, music, gaming) increments counters in a table variable. Using if-blocks and comparison operators, the program displays different "recommended content" labels based on which counters are highest, demonstrating how algorithms track behavior to shape recommendations. Students document patterns they observe and reflect on how this shapes viewing habits.
- **Challenge format:** Build-and-analyze project. Rubric checks: (1) click tracking with variables, (2) conditional recommendation logic, (3) table variable to display viewing history, (4) written reflection on algorithm influence.
- **CSTA:** E3‑CAS‑ET‑02.
```

---

## CHANGE 3: T35.G3.03 - Replace description and challenge format

**FIND (lines 155-167):**
```markdown
### T35.G3.03 – Develop class guidelines for respectful communication

_Dependency:_
  * T35.G3.02: Discuss how algorithms influence what we see
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Create a chat code of conduct
- **Description:** Learners write simple rules (no spam, be kind, no PII) for classroom collaboration tools.
- **Challenge format:** Group document summary. Rubric checks inclusion of kindness, privacy, consequences.
- **CSTA:** E3‑CAS‑ET‑02.

---
```

**REPLACE WITH:**
```markdown
### T35.G3.03 – Develop class guidelines for respectful communication

_Dependency:_
  * T35.G3.02: Discuss how algorithms influence what we see
  * T08.G3.01: Use a simple if in a script
  * T16.G3.01: Add a label widget to display text
  * T22.G3.01: Use ChatGPT blocks for simple queries


- **Short name:** Create a chat code of conduct
- **Description:** Students build a simple moderated chat room using widget blocks (text input, labels, buttons) and AI moderation. They create a chat interface where users type messages into a text input widget. Before displaying messages in a label widget, the program uses ChatGPT AI moderation blocks to check for inappropriate content (spam, unkindness, PII). If content violates guidelines, a warning label appears instead. Students collaboratively write the guidelines that inform the AI moderation prompts.
- **Challenge format:** Build-and-test project with peer testing. Rubric checks: (1) widget-based chat interface, (2) AI moderation block integration, (3) conditional display based on moderation results, (4) written community guidelines document.
- **CSTA:** E3‑CAS‑ET‑02.

### T35.G3.04 – Recognize when apps collect data

_Dependency:_
  * T35.G3.03: Develop class guidelines for respectful communication
  * T09.G3.01: Create and use a numeric variable for score or count
  * T16.G3.01: Add a label widget to display text


- **Short name:** What does this app know about me?
- **Description:** Students build a simple app (quiz or game) that collects data using variables and widgets. They create visible indicators showing what's being collected: labels that update to show "You've answered 5 questions" (counter variable), "Your high score: 100" (performance data), "You clicked on: Animals" (preference tracking). Students then discuss what the app "knows" about users and whether users can see what's collected.
- **Challenge format:** Build-and-document project. Rubric checks: (1) app with visible data collection (variables displayed via labels), (2) at least 3 data types tracked, (3) reflection on transparency and user awareness.
- **CSTA:** E3‑CAS‑ET‑02.

---
```

---

## CHANGE 4: T35.G4.01 - Enhance description

**FIND (lines 172-181):**
```markdown
### T35.G4.01 – Analyze case studies of tech helping/harming communities

_Dependency:_
  * T35.G3.01: Evaluate digital footprints


- **Short name:** Tech impact case cards
- **Description:** Students read short case studies (drones delivering meds vs drones invading privacy) and discuss tradeoffs.
- **Challenge format:** Case discussion worksheet. Auto-grading ensures mention of both benefits and harms.
- **CSTA:** E4‑CAS‑ET‑02.
```

**REPLACE WITH:**
```markdown
### T35.G4.01 – Analyze case studies of tech helping/harming communities

_Dependency:_
  * T35.G3.01: Evaluate digital footprints
  * T16.G4.01: Create interactive displays with widgets


- **Short name:** Tech impact case cards
- **Description:** Students read short case studies (drones delivering meds vs drones invading privacy) and discuss tradeoffs. Then, they build an interactive case study viewer using widget blocks: buttons to select different case studies, and labels to display benefits/harms for each case. Students use table variables to organize multiple cases (columns: technology, benefits, harms, affected community) and practice navigating the data.
- **Challenge format:** Case discussion worksheet + interactive viewer project. Auto-grading ensures mention of both benefits and harms in discussion; project rubric checks widget interface and table data organization.
- **CSTA:** E4‑CAS‑ET‑02.
```

---

## CHANGE 5: T35.G4.02 - Remove dependency and replace description

**FIND (lines 183-193):**
```markdown
### T35.G4.02 – Understand advertising/persuasion online

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T35.G3.02: Discuss how algorithms influence what we see


- **Short name:** Spot sponsored content
- **Description:** Learners identify ads, influencer promotions, and persuasive design patterns in sample apps.
- **Challenge format:** Screenshot annotation. Auto-grading checks labels and explanation.
- **CSTA:** E4‑CAS‑ET‑02.
```

**REPLACE WITH:**
```markdown
### T35.G4.02 – Understand advertising/persuasion online

_Dependency:_
  * T35.G3.02: Discuss how algorithms influence what we see
  * T16.G4.01: Create interactive displays with widgets


- **Short name:** Spot sponsored content
- **Description:** Students analyze actual CreatiCode community projects to identify persuasive design patterns (bright colors for "buy" buttons, countdown timers, celebrity endorsements in sprites). They create a project that demonstrates persuasive vs. informative design: two versions of the same app (e.g., a game invitation) where one uses persuasive tactics (flashing sprites, urgent language in labels) and one is neutral. Using widget blocks, they build both interfaces and have peers compare them, documenting which tactics they notice.
- **Challenge format:** Comparative design project + analysis worksheet. Rubric checks: (1) two versions of interface with clear design differences, (2) widget usage for UI elements, (3) documentation of persuasive tactics identified, (4) peer testing results.
- **CSTA:** E4‑CAS‑ET‑02.
```

---

## CHANGE 6: T35.G4.03 - Enhance description

**FIND (lines 195-205):**
```markdown
### T35.G4.03 – Reflect on accessibility/inclusion in games

_Dependency:_
  * T35.G3.03: Develop class guidelines for respectful communication


- **Short name:** Who can/can't play this game?
- **Description:** Students review a game for accessibility (color contrast, controls) and propose improvements.
- **Challenge format:** Review sheet. Auto-grading rubric checks mention of barriers + solutions.
- **CSTA:** E4‑CAS‑ET‑02, CAS‑HC.

---
```

**REPLACE WITH:**
```markdown
### T35.G4.03 – Reflect on accessibility/inclusion in games

_Dependency:_
  * T35.G3.03: Develop class guidelines for respectful communication
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T22.G4.01: Use AI Speaker for text-to-speech


- **Short name:** Who can/can't play this game?
- **Description:** Students review a CreatiCode game for accessibility barriers. They test: (1) Can you understand it without sound? (Test by muting), (2) Can you see important elements? (Use sprite size/color blocks to adjust contrast), (3) Can you control it without a mouse? (Add keyboard controls using when key pressed blocks), (4) Can you understand instructions? (Add text-to-speech using AI Speaker blocks). Students document barriers found and implement at least one improvement to a sample game using blocks (e.g., adding keyboard controls or text-to-speech instructions).
- **Challenge format:** Accessibility audit worksheet + improvement implementation. Rubric checks: (1) identification of barriers across multiple categories, (2) implemented code improvement using relevant blocks, (3) before/after testing documentation, (4) proposed solutions for remaining barriers.
- **CSTA:** E4‑CAS‑ET‑02, CAS‑HC.

---
```

---

## CHANGE 7: T35.G5.03 - Remove dependency

**FIND (lines 233-245):**
```markdown
### T35.G5.03 – Analyze AI's differential impacts on workers and communities

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T35.G4.01: Analyze case studies of tech helping/harming communities
  * T35.G4.02: Understand advertising/persuasion online


- **Short name:** AI job impacts across different communities
- **Description:** Learners research how AI affects different communities unequally: which jobs are most at risk, how impacts vary by education/income level, geographic disparities in AI adoption, and how T21-T24 AI tools might worsen or improve equity. They propose reskilling and policy solutions with social justice focus.
- **Challenge format:** Equity-focused AI impact analysis. Auto-grading requires demographic analysis, disparity identification, and community-centered solutions connecting to T21-T24.
- **CSTA:** E5‑CAS‑ET‑02.
- **AI4K12:** E2 Societal Impacts; D2 Bias and Fairness.
```

**REPLACE WITH:**
```markdown
### T35.G5.03 – Analyze AI's differential impacts on workers and communities

_Dependency:_
  * T35.G4.01: Analyze case studies of tech helping/harming communities
  * T35.G4.02: Understand advertising/persuasion online


- **Short name:** AI job impacts across different communities
- **Description:** Learners research how AI affects different communities unequally: which jobs are most at risk, how impacts vary by education/income level, geographic disparities in AI adoption, and how T21-T24 AI tools might worsen or improve equity. They propose reskilling and policy solutions with social justice focus.
- **Challenge format:** Equity-focused AI impact analysis. Auto-grading requires demographic analysis, disparity identification, and community-centered solutions connecting to T21-T24.
- **CSTA:** E5‑CAS‑ET‑02.
- **AI4K12:** E2 Societal Impacts; D2 Bias and Fairness.

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

## CHANGE 8: T35.G6.01 - Enhance description

**FIND (lines 251-263):**
```markdown
### T35.G6.01 – Apply ethics lenses (beneficence, fairness, autonomy)

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T35.G5.01: Examine global impacts of technology
  * T35.G4.01: Analyze case studies of tech helping/harming communities


- **Short name:** Use an ethics checklist for apps
- **Description:** Students evaluate a CreatiCode project using simple ethics lenses and document findings.
- **Challenge format:** Checklist + reflection. Auto-grading checks each lens includes evidence.
- **CSTA:** MS‑CAS‑ET‑05.
```

**REPLACE WITH:**
```markdown
### T35.G6.01 – Apply ethics lenses (beneficence, fairness, autonomy)

_Dependency:_
  * T16.G6.01: Create forms with multiple widget types
  * T35.G5.01: Examine global impacts of technology
  * T35.G4.01: Analyze case studies of tech helping/harming communities
  * T22.G6.01: Use ChatGPT for analysis tasks


- **Short name:** Use an ethics checklist for apps
- **Description:** Students apply three ethics lenses to evaluate CreatiCode projects (their own or community examples): Beneficence (Does this help people? Who benefits most? - Use ChatGPT blocks to analyze project purpose), Fairness (Can everyone use this equally? - Test with accessibility features like text-to-speech), Autonomy (Do users have control/choice? - Check for consent mechanisms using widget buttons). Students build an ethics evaluation tool using widgets: dropdown menu to select lens, text input for project URL/name, and label to display evaluation questions. They document findings in a table variable with columns: Project, Lens, Evidence, Rating.
- **Challenge format:** Evaluation tool project + completed assessment. Rubric checks: (1) widget-based evaluation interface, (2) table with multiple project assessments, (3) evidence-based ratings for each lens, (4) reflection on how lenses reveal different concerns.
- **CSTA:** MS‑CAS‑ET‑05.
```

---

## CHANGE 9: T35.G6.02 - Enhance description

**FIND (lines 265-275):**
```markdown
### T35.G6.02 – Analyze data privacy tradeoffs

_Dependency:_
  * T35.G5.01: Examine global impacts of technology
  * T35.G4.02: Understand advertising/persuasion online


- **Short name:** What data does this app collect and why?
- **Description:** Learners read mock privacy statements and decide whether the data collection is justified for the feature.
- **Challenge format:** Decision chart. Auto-grading checks references to stated purposes.
- **CSTA:** MS‑CAS‑ET‑06.
```

**REPLACE WITH:**
```markdown
### T35.G6.02 – Analyze data privacy tradeoffs

_Dependency:_
  * T35.G5.01: Examine global impacts of technology
  * T35.G4.02: Understand advertising/persuasion online
  * T16.G6.01: Create forms with multiple widget types
  * T19.G6.01: Store and retrieve data from cloud tables


- **Short name:** What data does this app collect and why?
- **Description:** Students build an interactive privacy policy demonstrator using widgets and cloud data blocks. They create a sample app (e.g., a quiz or game) that collects data points (name, age, score, location). Using widget blocks, they build: (1) A consent interface with checkboxes (buttons) for each data type, (2) Labels showing what each data type enables ("Location → Show local leaderboard"), (3) A "Submit" button that only saves checked data to a cloud table variable. Students compare full-data vs. minimal-data versions to analyze which features truly need which data. They write privacy statements justifying each data collection.
- **Challenge format:** Working privacy-conscious app + justification document. Rubric checks: (1) consent interface with widgets, (2) conditional data saving based on consent, (3) cloud/table variable usage, (4) written justification linking data to features.
- **CSTA:** MS‑CAS‑ET‑06.

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

## CHANGE 10: T35.G6.03 - Enhance description

**FIND (lines 277-289):**
```markdown
### T35.G6.03 – Develop ethics guidelines for AI content generation (T21-T22)

_Dependency:_
  * T35.G5.03: Analyze AI's differential impacts on workers and communities
  * T35.G4.03: Reflect on accessibility/inclusion in games


- **Short name:** AI content generation ethics
- **Description:** Students create ethical guidelines for AI image generation (T21) addressing bias in outputs, consent for training data, and cultural representation, and for AI chatbots (T22) addressing privacy, misinformation risks, and accessibility concerns.
- **Challenge format:** Ethics guideline document for generative AI. Rubric evaluates coverage of bias, consent, and misinformation issues.
- **CSTA:** MS‑CAS‑ET‑06.
- **AI4K12:** D1 Ethical Design; D2 Bias and Fairness.
```

**REPLACE WITH:**
```markdown
### T35.G6.03 – Develop ethics guidelines for AI content generation (T21-T22)

_Dependency:_
  * T35.G5.03: Analyze AI's differential impacts on workers and communities
  * T35.G4.03: Reflect on accessibility/inclusion in games
  * T21.G6.01: Generate images with AI (DALL-E blocks)
  * T22.G6.01: Use ChatGPT for complex conversations


- **Short name:** AI content generation ethics
- **Description:** Students actively test CreatiCode's AI blocks to develop evidence-based guidelines. For T21 (Image Generation): Generate 10+ images with prompts like "doctor," "nurse," "CEO," "teacher" noting demographic representation, documenting bias patterns in outputs. For T22 (ChatGPT): Test chatbot with various prompts to check: (1) Does it reveal training data sources? (2) Does it generate misinformation? (3) Does it understand different English dialects? Document quality variations. Using findings, students create ethics guidelines in a widget-based interactive guide (buttons for each AI type, labels displaying guidelines). They include: when bias is acceptable, how to write inclusive prompts, and how to verify AI outputs.
- **Challenge format:** AI testing documentation + interactive guidelines tool. Rubric checks: (1) systematic testing with 10+ examples per AI type, (2) documented bias/quality patterns, (3) widget-based guidelines interface, (4) actionable recommendations for responsible use.
- **CSTA:** MS‑CAS‑ET‑06.
- **AI4K12:** D1 Ethical Design; D2 Bias and Fairness.
```

---

## CHANGE 11: T35.G6.03.01 - Remove dependency

**FIND (lines 290-302):**
```markdown
### T35.G6.03.01 – Develop ethics guidelines for AI perception and assistance (T23-T24)

_Dependency:_
  * T35.G6.03: Develop ethics guidelines for AI content generation (T21-T22)
  * T35.G5.03: Analyze AI's differential impacts on workers and communities


- **Short name:** AI perception/assistance ethics
- **Description:** Students create ethical guidelines for AI perception tools (T23) addressing consent, surveillance concerns, and equity in recognition accuracy, and for AI coding assistants (T24) addressing academic integrity, proper citation, and avoiding over-dependency.
- **Challenge format:** Ethics guideline document for perception/assistance AI. Rubric evaluates coverage of surveillance, consent, and academic integrity issues.
- **CSTA:** MS‑CAS‑ET‑06.
- **AI4K12:** D1 Ethical Design; E2 Societal Impacts.
```

**REPLACE WITH:**
```markdown
### T35.G6.03.01 – Develop ethics guidelines for AI perception and assistance (T23-T24)

_Dependency:_
  * T35.G5.03: Analyze AI's differential impacts on workers and communities
  * T23.G6.01: Use AI perception tools (hand/body tracking)
  * T24.G6.01: Use AI coding assistants


- **Short name:** AI perception/assistance ethics
- **Description:** Students create ethical guidelines for AI perception tools (T23) addressing consent, surveillance concerns, and equity in recognition accuracy, and for AI coding assistants (T24) addressing academic integrity, proper citation, and avoiding over-dependency.
- **Challenge format:** Ethics guideline document for perception/assistance AI. Rubric evaluates coverage of surveillance, consent, and academic integrity issues.
- **CSTA:** MS‑CAS‑ET‑06.
- **AI4K12:** D1 Ethical Design; E2 Societal Impacts.
```

---

## CHANGE 12: T35.G7.01 - Minor enhancement

**FIND (lines 319-330):**
```markdown
### T35.G7.01 – Conduct bias audits for AI content generation (T21-T22)

_Dependency:_
  * T35.G6.03: Develop ethics guidelines for AI content generation (T21-T22)
  * T35.G5.03: Analyze AI's differential impacts on workers and communities


- **Short name:** AI content generation fairness testing
- **Description:** Students systematically audit T21 image generation for representation across demographics and T22 chatbots for response quality by dialect/topic. They measure disparities, analyze root causes, and propose mitigation strategies.
- **Challenge format:** Bias audit for generative AI. Auto-grading checks systematic testing, disparity measurement, and mitigation proposals.
- **CSTA:** MS‑CAS‑ET‑05, DAA‑DI.
- **AI4K12:** D2 Bias and Fairness; E2 Societal Impacts.
```

**REPLACE WITH:**
```markdown
### T35.G7.01 – Conduct bias audits for AI content generation (T21-T22)

_Dependency:_
  * T35.G6.03: Develop ethics guidelines for AI content generation (T21-T22)
  * T35.G5.03: Analyze AI's differential impacts on workers and communities


- **Short name:** AI content generation fairness testing
- **Description:** Students systematically audit T21 image generation for representation across demographics and T22 chatbots for response quality by dialect/topic. They measure disparities, analyze root causes, and propose mitigation strategies. Students use table variables to log results (columns: Prompt, Demographic, Quality Rating) and create data visualizations showing disparity patterns.
- **Challenge format:** Bias audit for generative AI. Auto-grading checks systematic testing, disparity measurement, table-based data logging, and mitigation proposals.
- **CSTA:** MS‑CAS‑ET‑05, DAA‑DI.
- **AI4K12:** D2 Bias and Fairness; E2 Societal Impacts.
```

---

## CHANGE 13: T35.G7.04 - Enhance description

**FIND (lines 369-381):**
```markdown
### T35.G7.04 – Analyze societal impacts of AI perception technologies (Pairing with T23)

_Dependency:_
  * T35.G6.02: Analyze data privacy tradeoffs
  * T35.G6.03.01: Develop ethics guidelines for AI perception and assistance (T23-T24)


- **Short name:** AI surveillance: community safety vs privacy
- **Description:** Following T23 perception projects, students analyze real-world case studies of AI surveillance (facial recognition in schools, emotion detection at work, gesture tracking in public). They debate tradeoffs between security and privacy, examine disproportionate impacts on marginalized communities, and propose ethical guidelines.
- **Challenge format:** Case study debate with equity focus. Rubric checks stakeholder analysis, community impact assessment, and ethical framework application.
- **CSTA:** MS‑CAS‑ET‑05.
- **AI4K12:** E2 Societal Impacts; D2 Bias and Fairness.
```

**REPLACE WITH:**
```markdown
### T35.G7.04 – Analyze societal impacts of AI perception technologies (Pairing with T23)

_Dependency:_
  * T35.G6.02: Analyze data privacy tradeoffs
  * T35.G6.03.01: Develop ethics guidelines for AI perception and assistance (T23-T24)
  * T23.G7.01: Use hand and body tracking for interactive projects


- **Short name:** AI surveillance: community safety vs privacy
- **Description:** Students use CreatiCode's T23 perception blocks (hand detection, body pose tracking) to build a simple surveillance simulator. They create a project that: (1) Uses hand detection to count people entering a "virtual space" (tracking when hands appear/disappear), (2) Uses body pose detection to identify "suspicious" movements (e.g., running vs. walking based on joint distances), (3) Logs all detections to a table variable with timestamps. Students then analyze their own data log as a case study: What privacy information is captured? Could it discriminate (e.g., different walking styles for different abilities)? They debate surveillance tradeoffs and write ethical guidelines for when such systems are justified.
- **Challenge format:** Surveillance simulator + case study analysis. Rubric checks: (1) working perception block integration, (2) data logging to table, (3) privacy impact analysis of collected data, (4) equity-focused ethical guidelines with stakeholder perspectives.
- **CSTA:** MS‑CAS‑ET‑05.
- **AI4K12:** E2 Societal Impacts; D2 Bias and Fairness.
```

---

## CHANGE 14: T35.G7.05 - Enhance description

**FIND (lines 382-394):**
```markdown
### T35.G7.05 – Debate ethical implications of AI media generation (Pairing with T21)

_Dependency:_
  * T35.G6.03: Develop ethics guidelines for AI content generation (T21-T22)
  * T35.G5.03: Analyze AI's differential impacts on workers and communities


- **Short name:** AI-generated content and creative professions
- **Description:** Following T21 AI media projects, students hold structured debates on AI's impact on artists, photographers, and designers. They examine issues of copyright, style imitation, job displacement, cultural representation in training data, and propose frameworks for ethical AI media use.
- **Challenge format:** Structured debate + policy proposal. Rubric checks multiple perspective inclusion, equity analysis, and actionable recommendations.
- **CSTA:** MS‑CAS‑ET‑05.
- **AI4K12:** E2 Societal Impacts; D1 Ethical Design.
```

**REPLACE WITH:**
```markdown
### T35.G7.05 – Debate ethical implications of AI media generation (Pairing with T21)

_Dependency:_
  * T35.G6.03: Develop ethics guidelines for AI content generation (T21-T22)
  * T35.G5.03: Analyze AI's differential impacts on workers and communities
  * T21.G7.01: Generate complex images with AI


- **Short name:** AI-generated content and creative professions
- **Description:** Students conduct AI art experiments using T21 (DALL-E) blocks: (1) Generate art "in the style of" famous artists (e.g., "landscape in Van Gogh style"), (2) Generate commercial assets (logos, product images, stock photos), (3) Compare time required (AI seconds vs. human hours for similar quality). They research artists' concerns through interviews/articles, then debate: Should AI art be copyrightable? Should training data sources be credited? How can artists adapt/benefit? Students create a policy proposal using widgets (interactive policy viewer with buttons for different stakeholder positions).
- **Challenge format:** AI art experiment documentation + structured debate + policy proposal project. Rubric checks: (1) systematic T21 testing across multiple styles/uses, (2) evidence from multiple stakeholder perspectives, (3) widget-based policy interface, (4) balanced recommendations.
- **CSTA:** MS‑CAS‑ET‑05.
- **AI4K12:** E2 Societal Impacts; D1 Ethical Design.

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

## CHANGE 15: T35.G8.01 - Remove dependency

**FIND (lines 412-423):**
```markdown
### T35.G8.01 – Apply ethical frameworks to real proposals

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T35.G7.01: Conduct bias audits for AI content generation (T21-T22)
  * T35.G6.01: Apply ethics lenses (beneficence, fairness, autonomy)


- **Short name:** Use consequentialist vs deontological reasoning
- **Description:** Students evaluate a computing project (predictive policing, emotion AI) through multiple ethical lenses and compare conclusions.
- **Challenge format:** Comparative essay. Rubric checks lens definitions and application.
- **CSTA:** MS‑CAS‑ET‑06.
```

**REPLACE WITH:**
```markdown
### T35.G8.01 – Apply ethical frameworks to real proposals

_Dependency:_
  * T35.G7.01: Conduct bias audits for AI content generation (T21-T22)
  * T35.G6.01: Apply ethics lenses (beneficence, fairness, autonomy)


- **Short name:** Use consequentialist vs deontological reasoning
- **Description:** Students evaluate a computing project (predictive policing, emotion AI) through multiple ethical lenses and compare conclusions.
- **Challenge format:** Comparative essay. Rubric checks lens definitions and application.
- **CSTA:** MS‑CAS‑ET‑06.
```

---

## CHANGE 16: T35.G8.03 - Enhance description

**FIND (lines 451-461):**
```markdown
### T35.G8.03 – Design impact assessments for CreatiCode projects

_Dependency:_
  * T35.G7.02: Explore unintended consequences of new tech
  * T35.G6.01: Apply ethics lenses (beneficence, fairness, autonomy)


- **Short name:** Pre-launch impact checklist
- **Description:** Students create rubrics assessing accessibility, privacy, wellbeing, and cultural sensitivity before publishing games/apps.
- **Challenge format:** Checklist + sample application. Auto-grading checks categories and evidence fields.
- **CSTA:** MS‑PRO‑PM‑03, CAS‑ET.
```

**REPLACE WITH:**
```markdown
### T35.G8.03 – Design impact assessments for CreatiCode projects

_Dependency:_
  * T35.G7.02: Explore unintended consequences of new tech
  * T35.G6.01: Apply ethics lenses (beneficence, fairness, autonomy)
  * T16.G8.01: Build complex multi-widget applications
  * T22.G8.01: Use ChatGPT for advanced analysis


- **Short name:** Pre-launch impact checklist
- **Description:** Students build an interactive impact assessment tool using widgets and table variables. The tool includes: (1) Input: Text field for project name/URL (widget text input), (2) Assessment categories (widget buttons to select): Accessibility (text-to-speech? keyboard controls? color contrast?), Privacy (what data collected? user consent? secure storage?), Wellbeing (time limits? addictive patterns? breaks encouraged?), Cultural sensitivity (inclusive representation? stereotypes avoided?), (3) Scoring interface: Radio buttons/dropdowns for each checklist item, (4) Output: Table variable showing assessment results + auto-generated recommendations using ChatGPT (e.g., "Project lacks keyboard controls - consider adding when key pressed blocks"). Students apply their tool to assess 3+ community projects and document findings.
- **Challenge format:** Working assessment tool + assessment reports. Rubric checks: (1) comprehensive widget interface for all categories, (2) table variable data storage, (3) ChatGPT integration for recommendations, (4) completed assessments of 3+ projects with evidence.
- **CSTA:** MS‑PRO‑PM‑03, CAS‑ET.
```

---

## SUMMARY OF CHANGES

**Total Lines Changed:** ~21 skill sections modified
**New Skills Added:** 4 (T35.G3.04, T35.G5.04, T35.G6.05, T35.G7.07)
**Dependencies Removed:** 4 instances of T04.G2.01, 1 instance of T35.G6.03
**Dependencies Added:** Multiple additions of T16 (widgets), T19 (data), T21-T24 (AI blocks)

**Implementation Order:**
1. Make all dependency removals (changes 5, 7, 11, 15)
2. Add new skills (changes 3, 7, 9, 14)
3. Update descriptions (all other changes)
4. Verify cross-references and numbering
