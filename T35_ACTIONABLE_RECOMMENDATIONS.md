# T35 (Impacts & Ethics) - Actionable Recommendations
**Date:** 2024-11-24

## QUICK SUMMARY

**Current State:** 49 skills, K-8
**Recommended State:** ~74 skills after optimization
**Main Issues:** 13 overly broad skills in G6-G8, 4 missing scaffolding skills

---

## PRIORITY 1: SPLIT OVERLY BROAD SKILLS

### GRADE 6 SPLITS (4 skills → 13 skills)

#### 1. T35.G6.01 → Split into 4 skills

**CURRENT:** T35.G6.01 - Apply ethics lenses (beneficence, fairness, autonomy)

**REPLACE WITH:**

**T35.G6.01.01 - Apply beneficence lens**
- Description: Students evaluate CreatiCode projects using the beneficence (help/harm) lens. They build an evaluation interface using widgets where they: (1) Select a project to evaluate, (2) Answer evaluation questions: "Does this help people? Who benefits most? Who might be harmed?", (3) Use ChatGPT blocks to analyze project purpose, (4) Rate beneficence on 1-5 scale, (5) Record evidence in table variable (columns: Project, Benefits, Harms, Rating). Students evaluate 2-3 projects documenting specific benefits and harms.
- Dependencies: T16.G6.01, T35.G5.01, T22.G6.01
- CSTA: Connections to beneficence principle

**T35.G6.01.02 - Apply fairness lens**
- Description: Students evaluate CreatiCode projects using the fairness lens. They build an evaluation interface using widgets where they: (1) Test accessibility features (text-to-speech, keyboard controls, color contrast), (2) Answer evaluation questions: "Can everyone use this equally? Does it create barriers? Does it treat all users the same?", (3) Document accessibility barriers found, (4) Rate fairness on 1-5 scale, (5) Record evidence in table variable (columns: Project, Barriers Found, Equitable Features, Rating). Students evaluate 2-3 projects.
- Dependencies: T35.G6.01.01, T16.G6.01, T35.G4.03.01
- CSTA: Connections to equity and access

**T35.G6.01.03 - Apply autonomy lens**
- Description: Students evaluate CreatiCode projects using the autonomy (control/choice) lens. They build an evaluation interface using widgets where they: (1) Check for user consent mechanisms (buttons, checkboxes for permissions), (2) Check for user control features (settings, preferences, opt-out), (3) Answer evaluation questions: "Do users have choices? Can users control their experience? Is consent required for data collection?", (4) Rate autonomy on 1-5 scale, (5) Record evidence in table variable (columns: Project, Control Features, Consent Mechanisms, Rating). Students evaluate 2-3 projects.
- Dependencies: T35.G6.01.02, T16.G6.01, T35.G6.02
- CSTA: Connections to user agency and consent

**T35.G6.01.04 - Compare ethics frameworks**
- Description: Students synthesize findings from applying all three ethics lenses (beneficence, fairness, autonomy) to the same projects. They: (1) Create a comparison table showing how the same project scored on each lens, (2) Identify where frameworks agree (project scored high/low on all) and disagree (high on one, low on another), (3) Analyze tensions (e.g., "High beneficence for crime reduction conflicts with low autonomy from surveillance"), (4) Use ChatGPT blocks to explore which framework should take priority for different project types, (5) Write justification for framework priorities with specific examples.
- Dependencies: T35.G6.01.03, T22.G6.01
- CSTA: Ethical reasoning and tradeoff analysis

---

#### 2. T35.G6.03.01 → Split into 2 skills

**CURRENT:** T35.G6.03.01 - Test AI content generation tools (T21-T22)

**REPLACE WITH:**

**T35.G6.03.01a - Test AI image generation for bias (T21)**
- Description: Students systematically test CreatiCode's T21 (DALL-E) image generation blocks to identify bias patterns. They: (1) Generate 10+ images with occupation prompts ("doctor," "nurse," "CEO," "teacher," "engineer," "artist") and document demographic representation, (2) Create a testing dashboard using widgets (text input for prompts, buttons to record observations: gender/race/age/stereotypes present), (3) Log all findings to table variable (columns: Prompt, Gender Observed, Race Observed, Age Observed, Stereotype Present?, Notes), (4) Analyze patterns using table operations (e.g., "80% of 'CEO' images showed men"), (5) Test with diverse modifiers ("diverse group of doctors") to see if representation improves.
- Dependencies: T35.G5.03, T21.G6.01, T16.G6.01
- CSTA: Bias in AI systems

**T35.G6.03.01b - Test AI chatbots for limitations (T22)**
- Description: Students systematically test CreatiCode's T22 (ChatGPT) chatbot blocks to identify limitations and risks. They test: (1) **Citation:** Does it cite sources? How verifiable are claims? (test 5 factual questions), (2) **Misinformation:** Does it generate false information? (test with known facts), (3) **Dialect Understanding:** Does it understand different English varieties? (test with AAVE, Indian English, regional dialects), (4) Create testing dashboard using widgets (dropdown for test category, text input for prompts, buttons to rate quality 1-5), (5) Log findings to table variable (columns: Test Category, Prompt, Response Quality, Issues Found, Notes), (6) Analyze patterns in what chatbot does well vs. poorly.
- Dependencies: T35.G5.03, T22.G6.01, T16.G6.01
- CSTA: Limitations of AI systems

---

#### 3. T35.G6.03.03 → Split into 2 skills

**CURRENT:** T35.G6.03.03 - Develop ethics guidelines for AI perception and assistance (T23-T24)

**REPLACE WITH:**

**T35.G6.03.03a - Develop ethics guidelines for AI perception (T23)**
- Description: Students test AI perception tools and develop evidence-based ethics guidelines. They: (1) Test T23 hand/body tracking blocks with different conditions (skin tones: light/medium/dark, lighting: bright/dim, backgrounds: plain/busy), (2) Document accuracy variations using widgets and table variables (columns: Test Condition, Accuracy Rating 1-5, Errors Observed, Notes), (3) Research perception technology uses (gesture controls, surveillance, accessibility tools), (4) Identify ethical concerns (consent for tracking, surveillance risks, equity in accuracy, disability accommodation), (5) Create comprehensive guidelines document using widgets addressing: When should tracking require consent?, How to mitigate accuracy disparities?, When are surveillance uses justified?, How to ensure accessibility?
- Dependencies: T35.G5.03, T23.G6.01, T16.G6.01
- CSTA: Privacy and equity in AI perception

**T35.G6.03.03b - Develop ethics guidelines for AI assistance (T24)**
- Description: Students test AI coding assistance tools and develop responsible use guidelines. They: (1) Test T24 coding assistant blocks with different question types (syntax help, debugging, algorithm design, full code generation), (2) Test with different English proficiency levels (beginner vs. advanced phrasing), (3) Document when AI help is most/least useful using widgets and table variables (columns: Question Type, Helpfulness 1-5, Learning Impact, Accuracy), (4) Identify ethical concerns (academic integrity, over-dependency, learning vs. completing, proper attribution), (5) Create comprehensive guidelines document using widgets addressing: When is AI assistance appropriate?, How to maintain learning goals?, How to cite AI-generated code?, How to avoid over-dependency?
- Dependencies: T35.G5.03, T24.G6.01, T16.G6.01
- CSTA: Responsible AI use and academic integrity

---

#### 4. T35.G6.05.02 → Split into 2 skills

**CURRENT:** T35.G6.05.02 - Implement data viewing and deletion controls

**REPLACE WITH:**

**T35.G6.05.02a - Implement data viewing controls**
- Description: Building on T35.G6.05.01 consent system, students implement user data transparency features. They add: (1) "View my data" button widget that triggers data retrieval from cloud tables, (2) Display interface using table widgets showing user's stored records in organized format with clear column headers (Data Type, Value, Date Collected, Purpose, Consent Status), (3) Summary labels showing data totals ("You have 15 quiz responses, 3 high scores, and 1 profile stored"), (4) "When collected" information for each data point using timestamps, (5) "Why collected" explanations displayed for each data type (e.g., "Location data → Show local leaderboard"). Students test with peers to verify data is displayed clearly and completely, then reflect on what "transparency" means (Can users understand what data exists? Is the purpose clear? Is the display overwhelming or helpful?).
- Dependencies: T35.G6.05.01, T16.G6.01, T19.G6.01
- CSTA: Data transparency and user rights

**T35.G6.05.02b - Implement data deletion controls**
- Description: Building on T35.G6.05.02a viewing controls, students implement user data control features. They add: (1) "Delete my data" button that shows confirmation dialog (new button widget: "Are you sure? This cannot be undone"), (2) Conditional logic using if-blocks to check confirmation before deleting records from cloud tables, (3) "Delete specific data" feature with checkboxes allowing selective deletion (delete quiz data but keep high scores), (4) "Revoke consent" feature that both removes consent flag AND deletes associated data, (5) Confirmation message after deletion (label: "Your data has been deleted"), (6) "Download my data" export button that displays data as copyable text. Students test deletion with different scenarios (delete all, delete partial, revoke consent) to verify data is actually removed from cloud storage, then reflect on what makes consent "informed and revocable" (granular choices, reversible decisions, clear consequences).
- Dependencies: T35.G6.05.02a, T16.G6.01, T19.G6.01
- CSTA: User data control and GDPR concepts

---

### GRADE 7 SPLITS (5 skills → 16 skills)

#### 5. T35.G7.01.01 → Split into 3 skills

**CURRENT:** T35.G7.01.01 - Conduct bias audits for AI perception and assistance (T23-T24)

**REPLACE WITH:**

**T35.G7.01.01a - Build bias testing framework**
- Description: Students design and build a reusable testing framework for auditing AI tools. They create: (1) Test configuration interface using widgets: Dropdown menus to select test tool (T21/T22/T23/T24), Dropdown for test conditions (for T23: skin tone light/medium/dark, lighting bright/dim/mixed; for T24: English proficiency native/intermediate/beginner), Text input for test prompts/questions, (2) Results logging system: Automated timestamp for each test, Table variable structure with columns (Tool Type, Test Condition, Prompt/Question, Accuracy Score 1-5, Error Type, Detailed Notes, Timestamp), Buttons to record results and save to cloud table, (3) Results display interface: Table widget showing logged tests, Filter buttons to view specific tool or condition, Summary labels showing test counts per category. Students verify the framework works by logging 5-10 sample tests.
- Dependencies: T35.G7.01, T16.G7.01, T19.G7.01
- CSTA: Systematic testing methodology

**T35.G7.01.01b - Audit AI perception tools (T23)**
- Description: Using the testing framework from T35.G7.01.01a, students conduct systematic bias audit of T23 perception tools. They: (1) Run comprehensive tests: Test hand tracking with 3 skin tones × 3 lighting conditions = 9 test scenarios, Test body pose tracking with 3 skin tones × 3 lighting conditions = 9 test scenarios, For each test: Rate accuracy 1-5, Document error types (missed detection, false detection, tracking loss), Note conditions where accuracy degrades, (2) Log all results to framework (minimum 18 tests), (3) Analyze patterns using table operations: Calculate average accuracy by skin tone (e.g., "Light: 4.8, Medium: 4.2, Dark: 3.1"), Calculate average accuracy by lighting, Identify biggest disparities (e.g., "Dark skin + dim lighting: 2.5 accuracy"), (4) Create visualization showing accuracy by condition using bar charts, (5) Analyze root causes (training data representation, camera sensors, algorithms) and propose solutions (diverse training data, adjustable sensitivity, user calibration options).
- Dependencies: T35.G7.01.01a, T23.G7.01
- CSTA: Bias in computer vision systems

**T35.G7.01.01c - Audit AI assistance tools (T24)**
- Description: Using the testing framework from T35.G7.01.01a, students conduct systematic bias audit of T24 coding assistance tools. They: (1) Run comprehensive tests across English proficiency levels: Native speakers (15 tests): Syntax questions, Debugging questions, Algorithm design, Full code generation, Advanced CS concepts, Intermediate English (15 tests): Same question types with simpler phrasing, Beginner English (15 tests): Same questions with ESL phrasing patterns, (2) For each test: Rate response quality 1-5 (accuracy, clarity, helpfulness), Document whether assistant understood question, Note if response included explanations or just code, Check if response was too advanced/simple for learner level, (3) Analyze patterns: Compare average quality scores by proficiency level, Identify question types that work well/poorly, Identify phrasing patterns that cause misunderstanding, (4) Test for code quality bias: Generate same algorithm with different prompt phrasing, Check if explanations are provided consistently, (5) Propose solutions (improved prompting strategies, proficiency-adaptive responses, multilingual support).
- Dependencies: T35.G7.01.01a, T24.G7.01
- CSTA: Equity in AI educational tools

---

#### 6. T35.G7.04.01 → Split into 3 skills

**CURRENT:** T35.G7.04.01 - Build AI perception surveillance simulator

**REPLACE WITH:**

**T35.G7.04.01a - Build entry/exit tracking system**
- Description: Students use T23 hand detection blocks to build a people-counting surveillance system. They create: (1) Detection zones using sprites (entry zone, exit zone), (2) Entry counter logic: When hand appears in entry zone, increment entry counter variable, Display running count on label widget, Store entry event in table variable (columns: Event Type, Timestamp, Location, Details), (3) Exit counter logic: When hand appears in exit zone, increment exit counter, Store exit event in table, (4) Current occupancy calculation: Live occupancy = entries - exits, Display on label widget, Update in real-time, (5) Basic dashboard using widgets: Labels showing total entries, total exits, current occupancy, Button to view event log in table widget, Button to clear/reset counters. Students test by moving hands in/out of zones, verify accurate counting, then discuss: What does this system capture? What privacy concerns exist? When might such systems be justified?
- Dependencies: T35.G6.02, T23.G7.01, T16.G7.01
- CSTA: Privacy in surveillance systems

**T35.G7.04.01b - Build movement classification system**
- Description: Students use T23 body pose detection blocks to build a movement analysis system. They create: (1) Body pose detection: Track key body joints (head, shoulders, hips, knees), Store joint positions in variables continuously, (2) Movement classification logic using conditionals: Walking detection: Calculate distance between frames, If distance > threshold, classify as "walking", Running detection: If distance > higher threshold, classify as "running", Standing detection: If distance < low threshold, classify as "standing", Sitting detection: If hip height < threshold, classify as "sitting", (3) Movement logging: Store each classification in table variable (columns: Timestamp, Movement Type, Duration, Body Position Data), Update live label showing current classification, Count how long person has been in each state, (4) Dashboard additions: Labels showing time spent in each movement type, Bar chart visualization using sprite graphics, Button to view movement history. Students test with different movements, verify accuracy, then discuss: How accurate is automated behavior classification? What could go wrong? How might different abilities be misclassified?
- Dependencies: T35.G7.04.01a, T23.G7.01, T16.G7.01
- CSTA: Bias in behavior recognition

**T35.G7.04.01c - Integrate surveillance dashboard**
- Description: Students combine the entry/exit and movement tracking systems into a comprehensive surveillance monitoring dashboard. They create: (1) Unified interface using widgets: Tabbed navigation (buttons) to switch between views: Occupancy view, Movement analysis view, Full event log, Settings/controls, (2) Combined data visualization: Real-time stats (current occupancy, current detected movements), Timeline view showing entries/exits/movements chronologically using table widget, Summary statistics (total events, average occupancy, movement patterns), (3) Advanced features: Time-based filtering (view last hour, last day), Alert system: If occupancy > threshold, display warning label, If unusual movement pattern detected, flag in log, Export button to save full surveillance log to cloud table, (4) Recording controls: Start/stop monitoring buttons, Clear data button with confirmation, Privacy mode button (pauses logging). Students test the complete system, generate realistic surveillance data, then export and analyze what information was captured.
- Dependencies: T35.G7.04.01b, T16.G7.01, T19.G7.01
- CSTA: Integrated surveillance systems

---

#### 7. T35.G7.04.02 → Split into 2 skills

**CURRENT:** T35.G7.04.02 - Analyze privacy and safety impacts

**REPLACE WITH:**

**T35.G7.04.02a - Analyze surveillance data for privacy risks**
- Description: Using surveillance data generated in T35.G7.04.01c, students conduct detailed privacy analysis. They: (1) Export and review their surveillance logs (entry/exit events, movement classifications, timestamps, durations), (2) Identify privacy-sensitive information captured: Movement patterns (when person arrives/leaves, how long they stay), Behavioral classifications (sitting, standing, walking, running), Temporal patterns (daily routines, schedule predictability), Location tracking within monitored space, (3) Analyze discrimination potential using structured questions: Could this system treat people with different abilities unfairly? (examples: mobility device users flagged as "suspicious," different walking gaits misclassified as unusual behavior), Could this system disproportionately monitor certain groups?, What assumptions does classification logic make about "normal" behavior?, (4) Research real-world cases: School monitoring systems (bathroom timers, hall passes), Retail analytics (customer tracking), Public safety (surveillance cameras), Workplace monitoring (productivity tracking), (5) Compare real cases to their simulator: What similarities exist? What additional privacy risks do real systems have? Create comparison table using widgets (columns: System Type, Data Collected, Privacy Concerns, Affected Groups).
- Dependencies: T35.G7.04.01c, T16.G7.01
- CSTA: Privacy analysis and discrimination

**T35.G7.04.02b - Debate surveillance ethics**
- Description: Using evidence from their surveillance simulator and privacy analysis, students engage in structured debate about AI perception surveillance ethics. They: (1) Build a debate tool using widgets: Buttons to select debate topics (school monitoring, public safety, retail analytics, workplace surveillance), Dropdown for stakeholder perspectives (student, parent, administrator, privacy advocate, security expert), Text display areas for pro-safety and pro-privacy arguments, Evidence panels showing simulator data and real-world cases, (2) Prepare debate positions using their evidence: Pro-safety arguments: Reference occupancy data (fire safety), movement data (injury detection), efficiency benefits, Pro-privacy arguments: Reference privacy-sensitive data captured, discrimination potential, chilling effects on behavior, (3) Conduct classroom debate in teams: Each team presents evidence from simulator and research, Respond to counterarguments with specific examples, Use debate tool to track arguments and counter-arguments, (4) Synthesize guidelines for justified surveillance: Required conditions (transparency, consent, proportionality), Required safeguards (data minimization, human oversight, bias testing, audit trails, user rights), Prohibited uses (individual behavior prediction, discriminatory applications). Students document final guidelines with specific, evidence-based criteria.
- Dependencies: T35.G7.04.02a, T16.G7.01
- CSTA: Ethical frameworks for surveillance

---

#### 8. T35.G7.05.01 → Split into 3 skills

**CURRENT:** T35.G7.05.01 - Experiment with AI-generated media

**REPLACE WITH:**

**T35.G7.05.01a - Generate art in various styles**
- Description: Students systematically experiment with AI art style mimicry using T21 (DALL-E) blocks. They: (1) Select 5 famous artists representing different styles (e.g., Van Gogh, Picasso, Frida Kahlo, Hokusai, Banksy), (2) For each artist, generate 3 images using style prompts: "landscape in [Artist] style", "portrait in [Artist] style", "abstract composition in [Artist] style", (3) Document results using widgets and table variables: Rate similarity to original artist's work (1-5 scale), Note what AI captured well (colors, brushstrokes, composition), Note what AI missed (emotional depth, cultural context, innovation), Record generation time (seconds), (4) Create side-by-side gallery: Display AI-generated art next to actual artist works using sprites/backdrops, Add labels with metadata (prompt used, artist referenced, similarity rating), Build navigation buttons to browse gallery, (5) Analyze patterns across all tests: Which styles did AI replicate best/worst? What artistic elements can AI capture vs. what it can't? Log findings in table variable (columns: Artist, Style Period, AI Strength, AI Weakness, Similarity Rating).
- Dependencies: T35.G6.03.01a, T21.G7.01, T16.G7.01
- CSTA: AI capabilities and limitations in creativity

**T35.G7.05.01b - Generate commercial assets**
- Description: Students test T21 image generation for commercial applications and compare to human work. They: (1) Generate commercial assets across categories: Company logos (5): "modern tech company logo," "eco-friendly brand logo," "gaming company logo", Product images (5): "smart watch product photo," "running shoe advertisement," "food packaging design", Stock photos (5): "diverse team meeting," "person using laptop," "outdoor adventure", (2) For each asset, document using widgets: Quality rating (1-5: professional, amateur, unusable), Commercial viability (Yes/Partial/No: Could this be used in real business?), Time to generate (seconds), Estimate human creation time (hours/days), Cost comparison (AI: nearly free; Human: estimate based on freelance rates), Specific issues noted (wrong proportions, uncanny valley, text gibberish, copyright concerns), (3) Compare 10 AI-generated assets to 10 human-created equivalents (provided examples): Rate quality difference, Identify unique strengths of each (AI: speed, cost, variations; Human: originality, cultural understanding, refinement), Note what tasks AI could replace vs. where humans remain essential, (4) Create commercial viability report using table variables (columns: Asset Type, AI Quality, Human Quality, Time Saved, Cost Saved, Best Use Case).
- Dependencies: T35.G7.05.01a, T21.G7.01, T16.G7.01
- CSTA: Economic impacts of AI

**T35.G7.05.01c - Analyze AI art capabilities**
- Description: Students synthesize findings from style and commercial experiments to map AI art capabilities and limitations. They: (1) Build an interactive AI art capabilities dashboard using widgets: Style replication slider (shows what styles AI handles well to poorly), Task type categorization (logos, products, art styles, photos) with quality indicators, Time savings calculator (input human creation estimate, show AI time, display difference), (2) Pattern identification using table analysis: Calculate average similarity ratings by art style/period, Identify which commercial tasks score highest quality, Find correlations (e.g., "Simple geometric styles: high similarity, Complex emotional pieces: low similarity"), (3) Create capability matrix visualization using sprites/labels: Grid showing Task Type (rows) × Quality Factors (columns), Color-code cells (green: AI excellent, yellow: AI partial, red: AI poor), Add specific examples in each cell, (4) Document limitations with evidence: What can AI NOT do well? (original creative vision, cultural context, emotional authenticity, consistent characters across images), What requires human work? (art direction, refinement, cultural sensitivity, strategic creativity), Where is AI most useful? (rapid prototyping, variations, style transfer, stock content). Students present findings as an "AI Art Capabilities Report" with specific examples and evidence.
- Dependencies: T35.G7.05.01b, T16.G7.01
- CSTA: Understanding AI system capabilities

---

#### 9. T35.G7.05.02 → Split into 3 skills

**CURRENT:** T35.G7.05.02 - Debate ethics and propose policies

**REPLACE WITH:**

**T35.G7.05.02a - Research AI art stakeholder perspectives**
- Description: Students research diverse stakeholder perspectives on AI-generated media ethics through interviews, articles, and case studies. They: (1) Identify key stakeholder groups: Visual artists (illustrators, photographers, painters), Educators (art teachers, curriculum designers), Business users (marketing, advertising, product design), Consumers (social media users, content viewers), AI researchers/developers, (2) Research each perspective through: Conducting 1-2 stakeholder interviews (in person or via provided videos/articles), Reading opinion pieces and news articles, Reviewing comments on AI art communities, (3) Document perspectives using widgets and table variables: Stakeholder type, Main concerns (copyright, devaluation, training data, disclosure, compensation), Potential benefits they see (efficiency, accessibility, democratization), Proposed solutions (regulation, attribution, opt-out, licensing), Supporting quotes/evidence, (4) Build stakeholder perspective database: Table variable with columns (Stakeholder, Role, Concerns, Benefits, Proposed Solutions, Source), Widget interface to browse perspectives (dropdown to select stakeholder type, text display showing their views), (5) Identify areas of agreement and disagreement: Where do all stakeholders agree? (e.g., "AI should disclose when content is generated"), Where do perspectives conflict? (e.g., Artists want restrictions vs. businesses want freedom), Map conflicts in visualization using widgets.
- Dependencies: T35.G7.05.01c, T16.G7.01
- CSTA: Multiple perspectives in tech ethics

**T35.G7.05.02b - Conduct AI art ethics debates**
- Description: Using evidence from experiments and stakeholder research, students engage in structured debates on AI art ethics. They: (1) Build an interactive debate tool using widgets: Buttons to select debate topics: "Should AI art be copyrightable?", "Should training data sources be credited/compensated?", "When must AI generation be disclosed?", "How can artists adapt and benefit from AI?", Dropdown to select stakeholder perspective to argue from (Artist, Business, Educator, Consumer, Researcher), Text display areas for arguments and counter-arguments, Evidence panels linking to experiment data and stakeholder quotes, Vote buttons to track class opinion before/after debate, (2) Prepare debate positions: Select position using debate tool, Gather evidence from AI art experiments (capabilities, limitations, time savings), Reference stakeholder interviews and research, Prepare arguments using debate tool interface, Anticipate counter-arguments, (3) Conduct classroom debates: Teams present opening arguments (2 minutes) with specific evidence, Rebuttal period using counter-arguments (2 minutes), Audience questions and discussion, Document key points in debate tool (record arguments and responses), Vote on most convincing positions, (4) After each debate topic: Identify strongest arguments on each side, Find common ground or compromises, Note unresolved tensions, Document in table variable (columns: Topic, Pro Arguments, Con Arguments, Evidence Used, Common Ground, Tensions).
- Dependencies: T35.G7.05.02a, T16.G7.01
- CSTA: Ethical reasoning and argumentation

**T35.G7.05.02c - Draft AI art policy proposals**
- Description: Building on debate insights and stakeholder perspectives, students draft specific policy proposals for AI-generated media. They: (1) Select 2-3 policy areas to address: Copyright and ownership (Is AI art copyrightable? Who owns it?), Training data and attribution (Should AI disclose training sources? Should artists be compensated?), Disclosure requirements (When must AI generation be labeled? How should disclosure look?), Artist adaptation and support (How can artists compete? What new opportunities exist?), (2) For each policy area, draft proposals using widgets: Text input for policy statement (specific, actionable rule), Dropdown for scope (school/platform/state/federal), Justification section referencing: Evidence from AI art experiments, Stakeholder perspectives considered, Debate arguments that persuaded them, Rationale section explaining how policy balances competing interests, (3) Include policy components: Problem statement (what issue does this address?), Specific requirement (what must happen?), Affected parties (who must comply?), Enforcement (how is compliance ensured?), Exceptions (when does this not apply?), Rationale (why this policy balances interests?), (4) Create interactive policy proposal tool using widgets: Navigation buttons for each policy area, Display showing full proposal text, Comparison view showing how proposal addresses different stakeholder concerns, Rating interface for peer feedback, (5) Present proposals to class: Explain problem addressed, Describe specific requirements, Show how policy balances competing interests with evidence, Respond to questions and critiques, Iterate based on feedback.
- Dependencies: T35.G7.05.02b, T16.G7.01
- CSTA: Policy development and systems thinking

---

### GRADE 8 SPLITS (2 skills → 8 skills)

#### 10. T35.G8.02 → Split into 3 skills

**CURRENT:** T35.G8.02 - Draft equity-focused policy briefs for AI in education

**REPLACE WITH:**

**T35.G8.02a - Research and collect AI equity data**
- Description: Students design and conduct original research on AI equity issues in education. They: (1) Design a comprehensive student survey using widgets: Demographics questions (grade, prior CS experience, device ownership, internet access), T21-T24 AI tool access questions: "Have you used AI image generation?", "Have you used AI chatbots for schoolwork?", "Have you used AI perception tools?", "Have you used AI coding assistants?", AI tool experience questions: "How helpful were they? (1-5)", "What barriers did you face? (cost, access, skills, awareness)", Equity perception questions: "Do you think all students have equal access to AI tools?", "How has AI helped or hindered your learning?", (2) Deploy survey to 20+ students across grade levels, (3) Collect and analyze survey data: Store responses in Google Sheets using cloud blocks, Calculate access percentages by demographic group, Identify access disparities (e.g., "80% of G8 used chatbots, only 30% of G5"), Identify reported barriers and challenges, (4) Supplement survey with additional data: Analyze their own T35.G7.01 bias audit results (AI output quality disparities), Review privacy policies from education AI tools (what data is collected? how is it used?), Research incidents (news articles about AI cheating, data breaches, bias scandals in education AI), (5) Organize all data in comprehensive table variables (columns: Data Source, Finding, Affected Group, Evidence Type, Severity, Date). Students create data summary document showing key statistics and patterns.
- Dependencies: T35.G7.06, T35.G6.04, T16.G8.01, T19.G8.01
- CSTA: Data collection and analysis

**T35.G8.02b - Visualize AI equity data**
- Description: Using data collected in T35.G8.02a, students create clear, honest visualizations to communicate equity findings. They: (1) Design visualizations for key findings using table variables and sprite graphics: AI tool access by grade level: Bar chart showing percentage using each AI tool (T21/T22/T23/T24), Access by demographic group: Clustered bars showing disparities, Reported barriers: Pie chart of barrier types (cost, device, skills, awareness), Tool helpfulness by prior experience: Line graph showing correlation, Privacy concerns: Word cloud or bar chart of concern categories, (2) Apply ethical data visualization principles from T35.G7.07: Use appropriate scales (start y-axis at 0), Show full context (don't cherry-pick data), Use clear labels and legends, Use color carefully (accessible, not manipulative), Include sample sizes and confidence indicators, (3) Build interactive data visualization tool using widgets: Buttons to navigate between visualizations, Dropdown to filter by demographic group or grade level, Labels displaying key statistics for each visualization, Hover or click to see detailed data points, Toggle between different chart types for same data, (4) Create visualization descriptions: For each chart: What does this show?, What patterns are visible?, What disparities exist?, What questions remain?, (5) Test visualizations with peers: Can they interpret correctly?, Do visualizations communicate clearly?, Are there misleading elements? Students iterate based on feedback to ensure honest, clear communication.
- Dependencies: T35.G8.02a, T19.G8.01, T16.G8.01, T35.G7.07
- CSTA: Data visualization and communication

**T35.G8.02c - Draft equity policy brief**
- Description: Using research and visualizations from previous skills, students draft a comprehensive one-page policy brief addressing AI equity in education. They: (1) Build interactive brief using widgets with standard policy brief structure: Title section (clear, specific problem statement), Executive summary section (3-4 sentence overview), Background section (why this matters, 2-3 key statistics from visualizations), Problem statement section (specific equity issues identified with evidence: "Only 30% of students without home internet use AI tools vs. 85% with access"), Recommendations section (3-4 specific, actionable policy recommendations): Each recommendation includes: specific action, responsible parties, timeline, expected impact, supporting evidence from research/visualizations, (2) Embed visualizations directly in brief: Use sprite graphics to display charts inline with text, Add "click to expand" buttons for detailed data, Include data tables as supporting documentation, (3) Example recommendations: "Provide free AI tool access through school accounts (addresses cost barrier, evidence: 45% cited cost as barrier)", "Offer AI literacy workshops for students with less prior experience (addresses skills gap, evidence: correlation between experience and reported helpfulness)", "Establish AI privacy standards for education tools (addresses privacy concerns, evidence: 70% concerned about data collection)", (4) Create multiple delivery formats: Widget-based interactive version (navigate with buttons), Printable text version (export as formatted text), Presentation version (slides with visualizations), (5) Review criteria: Are recommendations specific and actionable?, Is evidence clearly connected to recommendations?, Do visualizations support arguments effectively?, Does brief address multiple stakeholder perspectives? Students peer review using these criteria and iterate.
- Dependencies: T35.G8.02b, T16.G8.01
- CSTA: Policy writing and advocacy

---

#### 11. T35.G8.03.01 → Split into 4 skills

**CURRENT:** T35.G8.03.01 - Build impact assessment tool with scoring

**REPLACE WITH:**

**T35.G8.03.01a - Build accessibility assessment module**
- Description: Students design and build a comprehensive accessibility assessment module using widgets. They create: (1) Assessment interface with detailed checklist: **Audio independence:** Can you understand without sound? (test by muting), Are visual cues provided for audio information?, Is critical information conveyed multiple ways?, **Visual clarity:** Can you see important elements? (check sprite sizes, color contrast), Is text large enough and readable? (minimum 12pt equivalent), Are color combinations accessible? (test with contrast checker), Do animations cause issues? (flashing, motion sickness), **Input alternatives:** Can you control without mouse? (test keyboard-only), Are multiple control options available? (mouse, keyboard, touch), Are controls clearly labeled?, Can you remap controls?, **Instruction clarity:** Are instructions clear and complete?, Is help available when needed?, Are error messages helpful?, Is language appropriate for audience?, (2) Scoring interface using widgets: Radio buttons or dropdowns for each checklist item (Yes=2 points, Partial=1 point, No=0 points, NA), Text fields to record evidence/examples, Photo upload or link to specific examples, (3) Calculation and reporting: Calculate total score (sum all points), Calculate percentage (score / possible points), Calculate category score (audio, visual, input, instructions), Display overall accessibility rating: 90-100%: "Highly Accessible", 70-89%: "Mostly Accessible", 50-69%: "Needs Improvement", <50%: "Significant Barriers", Generate specific recommendations based on failed items, (4) Evidence documentation: Table variable storing all assessments (columns: Project Name, Checklist Item, Score, Evidence, Timestamp), Screenshots or examples of barriers found, Notes about severity and user impact.
- Dependencies: T35.G7.02, T35.G6.01, T16.G8.01
- CSTA: Accessibility evaluation

**T35.G8.03.01b - Build privacy assessment module**
- Description: Students design and build a comprehensive privacy assessment module using widgets. They create: (1) Assessment interface with detailed checklist: **Data collection:** What data is collected? (list all: name, age, location, scores, preferences, behavior), Is collection minimized? (only necessary data), Are collection points clearly marked?, Can users see what's collected?, **User consent:** Is consent requested before collection?, Is consent specific and granular? (separate consent for each data type), Can users opt out of non-essential collection?, Is consent language clear and age-appropriate?, **Data storage:** How is data stored? (local, cloud, third-party), Is storage secure? (encrypted, access-controlled), Who can access data? (user, teacher, admin, company), How long is data retained?, **Data usage:** How is data used? (immediate function, analytics, third-party sharing), Is usage transparent to users?, Can users control usage?, Are there unexpected uses?, **User rights:** Can users view their data?, Can users delete their data?, Can users export their data?, Can users correct inaccurate data?, (2) Scoring interface using widgets: Radio buttons for each checklist item (Yes=2, Partial=1, No=0, NA), Text fields for evidence and data flow documentation, Risk rating for each data type (Low/Medium/High risk), (3) Calculation and reporting: Calculate total privacy score, Calculate category scores (collection, consent, storage, usage, rights), Display overall privacy rating: 90-100%: "Privacy-Respecting", 70-89%: "Adequate Privacy", 50-69%: "Privacy Concerns", <50%: "Significant Privacy Risks", Generate specific recommendations, Flag high-risk practices (e.g., "Collects location without clear purpose"), (4) Documentation: Data flow diagram showing collection → storage → usage, Table variable with all findings.
- Dependencies: T35.G8.03.01a, T35.G6.05.02b, T16.G8.01
- CSTA: Privacy evaluation

**T35.G8.03.01c - Build wellbeing assessment module**
- Description: Students design and build a comprehensive wellbeing assessment module using widgets. They create: (1) Assessment interface with detailed checklist: **Time management:** Does app encourage time limits?, Are breaks suggested or required?, Is there a natural stopping point?, Does app discourage binge use?, **Addictive patterns:** Are there infinite scrolls or auto-play?, Are there randomized rewards? (loot boxes, gacha), Are there social pressure mechanics? (streaks, FOMO), Are there dark patterns? (fake urgency, nagging), **Age-appropriateness:** Is content appropriate for target age?, Is difficulty appropriate?, Are safety features suitable for age?, Is time investment reasonable?, **Mental health:** Does app promote positive feelings?, Are failure states constructive or punitive?, Is competition healthy or toxic?, Does app encourage real-world connections?, **Physical health:** Does app encourage movement/breaks?, Are there ergonomic considerations?, Is eye strain minimized? (brightness, contrast, breaks), Does app promote healthy habits?, (2) Scoring interface using widgets: Radio buttons for each checklist item (Healthy=2, Neutral=1, Concerning=0, NA), Text fields for specific examples of patterns, Severity ratings for concerning features, (3) Calculation and reporting: Calculate total wellbeing score, Calculate category scores (time, addiction, age, mental, physical), Display overall wellbeing rating: 90-100%: "Supports Wellbeing", 70-89%: "Generally Healthy", 50-69%: "Some Concerns", <50%: "Significant Concerns", Flag specific concerning patterns with evidence, Generate recommendations for improvement, (4) Documentation: List specific dark patterns or addictive mechanics found, Table variable with all findings and examples.
- Dependencies: T35.G8.03.01b, T35.G5.02, T16.G8.01
- CSTA: Digital wellbeing evaluation

**T35.G8.03.01d - Integrate assessment modules**
- Description: Students integrate the three assessment modules (accessibility, privacy, wellbeing) into a unified comprehensive impact assessment tool. They: (1) Build unified navigation interface: Main menu with buttons for each module (Accessibility, Privacy, Wellbeing), Tab interface to switch between modules, Progress indicators showing completion status for each module, "Assessment Overview" dashboard showing all scores, (2) Implement project management features: Text input for project name/URL at start, "Save Assessment" button storing all module data to cloud table, "Load Assessment" button retrieving previous assessments, "New Assessment" button clearing all data with confirmation, Project comparison view showing multiple assessments side-by-side, (3) Create comprehensive reporting system: Overall impact score combining all three modules (weighted: Accessibility 35%, Privacy 35%, Wellbeing 30%), Visual dashboard using sprite graphics: Three gauges/meters showing each module score, Color-coded overall rating (green/yellow/red), List of top concerns across all modules, Comprehensive recommendations section: Automatically generate recommendations using ChatGPT blocks, Input: all assessment data and scores, Output: prioritized, actionable recommendations (e.g., "High Priority: Add keyboard controls (Accessibility score: 45%). Consider: 'when key pressed' blocks for all mouse interactions."), Category-specific recommendations for each module, (4) Advanced features: Export assessment as formatted report (text), Share assessment link (cloud table), Compare to assessment standards (WCAG, COPPA, etc.), Generate certificate for projects meeting all thresholds (>80% all categories). Students test the complete tool on sample projects to verify: All modules work together smoothly, Scores calculate correctly, Recommendations are relevant and helpful, Interface is intuitive to navigate.
- Dependencies: T35.G8.03.01c, T16.G8.01, T22.G8.01
- CSTA: Systems integration and comprehensive evaluation

---

## PRIORITY 2: ADD MISSING SCAFFOLDING SKILLS

### 1. T35.G2.05 - Introduction to digital ethics tools (NEW)
**Location:** After T35.G2.04, before T35.G3.01
**Purpose:** Bridge from unplugged to block-based ethics work

**Description:** Students explore simple digital tools for ethics learning to prepare for block-based work in Grade 3. They: (1) Explore provided ethics apps/tools (teacher-selected age-appropriate tools that demonstrate privacy, kindness, or digital citizenship concepts), (2) Identify how digital tools can demonstrate ethics concepts: Labels that show information, Buttons that offer choices, Images that illustrate consequences, (3) Practice using basic digital interfaces: Clicking buttons to make choices, Reading labels with information, Looking at visual feedback, (4) Discuss what makes a tool helpful for learning: Clear instructions, Visual examples, Interactive choices, Immediate feedback, (5) Draw or describe a simple ethics tool they would create using these elements (preparing for G3.01 where they'll build with blocks). This provides concrete experience with digital ethics tools before coding them.

**Dependencies:** T35.G2.04, T16.G2.01 (basic widget understanding)
**CSTA:** Digital tools for learning

---

### 2. T35.G5.05 - Introduction to ethics frameworks (NEW)
**Location:** After T35.G5.04, before T35.G6.01
**Purpose:** Introduce ethics concepts before G6 detailed application

**Description:** Students learn foundational concepts of ethical frameworks through simple scenarios. They explore three key frameworks: (1) **Beneficence (Help vs. Harm):** Explore scenarios: "A camera on the school bus keeps kids safe BUT records their conversations", "AI tutoring helps students learn BUT may reduce teacher jobs", For each, identify: Who benefits? Who might be harmed? Do benefits outweigh harms?, Practice asking beneficence questions about familiar technologies, (2) **Fairness (Equal Access and Impact):** Explore scenarios: "A reading app uses AI BUT only works well in English", "A game has beautiful graphics BUT requires expensive device", For each, identify: Can everyone use this? Who faces barriers? Does it treat all users equally?, Practice asking fairness questions about familiar technologies, (3) **Autonomy (Control and Choice):** Explore scenarios: "A learning app tracks progress BUT doesn't let you delete data", "A social app suggests friends BUT doesn't explain how", For each, identify: Do users have control? Do users have choices? Is consent required?, Practice asking autonomy questions about familiar technologies, (4) Create simple ethics framework reference guide (table format) with: Framework name, Key question, Example scenario, When to prioritize this framework, (5) Practice applying frameworks to 2-3 provided scenarios, discussing which framework reveals the most important issue. This prepares students for G6.01 where they'll build tools to apply these frameworks systematically.

**Dependencies:** T35.G5.04, T35.G4.01
**CSTA:** Ethical frameworks introduction

---

### 3. T35.G6.03.00 - Explore AI bias concepts (NEW)
**Location:** Before T35.G6.03.01a and T35.G6.03.01b
**Purpose:** Introduce bias concepts before systematic testing

**Description:** Students learn what bias means in AI systems before conducting formal testing. They: (1) **Define AI bias:** Unfair or skewed AI outputs that favor/disfavor certain groups, Examples: Image search showing mostly men for "doctor", Voice assistants misunderstanding accents, Facial recognition working poorly for darker skin tones, (2) **Explore types of bias:** Representation bias (training data doesn't include all groups equally), Quality bias (AI performs better for some groups than others), Stereotype bias (AI reinforces cultural stereotypes), (3) **Understand causes of bias:** Training data reflects human biases and historical inequality, Some groups are underrepresented in training data, Developers' choices affect AI behavior, Testing may not include diverse groups, (4) **Explore impacts of bias:** Some people excluded or underserved, Stereotypes reinforced, Discrimination automated at scale, Trust in AI systems eroded, (5) **Practice identifying bias:** View 10+ provided examples of biased AI outputs (images, text, recognition failures), For each, identify: What bias is present? Who is affected? What might have caused this? How could it be improved?, Document examples in table variable (columns: AI Type, Bias Observed, Affected Group, Possible Cause), (6) **Prepare for testing:** Brainstorm what to test in T21 (image prompts that might show bias), Brainstorm what to test in T22 (questions that might reveal limitations), Design testing approach (what data to collect, how to identify bias patterns). This prepares students for systematic bias testing in T35.G6.03.01a-b.

**Dependencies:** T35.G5.03, T35.G4.01
**CSTA:** Bias in AI systems

---

### 4. T35.G7.04.00 - Research surveillance technology uses (NEW)
**Location:** Before T35.G7.04.01a
**Purpose:** Understand surveillance context before building simulator

**Description:** Students research real-world AI surveillance technologies and their ethical concerns before building their own simulator. They: (1) **Research surveillance types:** School monitoring: Bathroom timers, hall pass systems, camera-based attendance, activity tracking, Retail surveillance: Customer tracking, behavior analysis, heat maps, facial recognition for theft prevention, Public safety: Camera networks, license plate readers, crowd monitoring, predictive policing, Workplace monitoring: Productivity tracking, break time monitoring, email/chat surveillance, keystroke logging, (2) **Analyze each case using structured questions:** What is being monitored? (location, behavior, time, identity), What technology is used? (cameras, sensors, AI, biometrics), What is the stated purpose? (safety, efficiency, security), What data is collected and stored?, Who has access to the data?, Were monitored people informed/consented?, (3) **Identify ethical concerns:** Privacy: What privacy-sensitive information is captured?, Consent: Were people asked permission? Can they opt out?, Discrimination: Could system treat different groups unfairly?, Chilling effects: Does monitoring change behavior in harmful ways?, Mission creep: Could data be used for unintended purposes?, Power imbalance: Who controls vs. who is monitored?, (4) **Document research using widgets and table variables:** Table of surveillance systems (columns: System Type, Technology, Purpose, Data Collected, Ethical Concerns), Rating of each system's justification (1-5: How justified is this use?), Most concerning practices identified, (5) **Prepare for simulator:** List what their T23 simulator will be able to monitor, Predict what ethical concerns their simulator will demonstrate, Design what data they'll collect to analyze ethics, Identify what questions they'll explore through building. This provides essential context before building surveillance simulator in T35.G7.04.01a-c.

**Dependencies:** T35.G6.02, T35.G6.03.03a
**CSTA:** Surveillance technology and ethics

---

## PRIORITY 3: CLARIFY VAGUE DESCRIPTIONS

### 1. T35.G5.02 - Debate digital well-being scenarios (CLARIFY)

**CURRENT DESCRIPTION:**
"Students debate policy scenarios (device-free times, notifications) referencing evidence on focus and health."

**REVISED DESCRIPTION:**
"Students engage in evidence-based debates about digital wellbeing policies. They: (1) Research evidence on screen time effects: Read 2-3 provided articles or studies on topics (device use and sleep, notifications and focus, social media and mental health, screen time and physical activity), Identify key findings and statistics from research, Note which sources are credible and why, (2) Prepare debate positions on policy scenarios: Device-free times (should schools have phone-free lunch? should bedrooms be device-free after 9pm?), Notification management (should apps be required to have 'focus mode'? should students control notification frequency?), Screen time limits (should apps show time-spent warnings? should parents set device time limits?), (3) Conduct structured debates using evidence: Teams present position with 2-3 evidence points from research (e.g., 'Study X found sleep improved 1 hour when devices removed from bedroom'), Opposing team responds with counter-evidence, Class discusses which evidence is most convincing and why, Document debate arguments and evidence in table format, (4) Reach evidence-based conclusions: Which policies are best supported by research? Where does evidence conflict or remain unclear? What additional information would help decide? Students write reflection connecting evidence to positions."

---

### 2. T35.G6.04 - Examine digital divide data (CLARIFY)

**CURRENT DESCRIPTION:**
"Learners interpret charts (broadband availability, device ownership) and propose community actions."

**REVISED DESCRIPTION:**
"Students analyze digital divide data visualizations and develop evidence-based community action proposals. They: (1) Interpret provided data visualizations: Analyze 2-3 charts showing digital access disparities (broadband availability by region/income, device ownership by demographic group, internet speed by location), For each visualization: Identify the most underserved groups (e.g., '30% of rural areas lack broadband vs. 5% of urban'), Calculate disparity gaps (e.g., '25 percentage point gap in device ownership between high/low income'), Note trends over time (is gap growing or shrinking?), (2) Identify root causes of disparities: Infrastructure challenges (rural areas, cost of deployment), Economic barriers (device costs, subscription fees), Digital literacy gaps (skills to use technology effectively), Awareness barriers (not knowing resources exist), (3) Propose 2-3 specific, realistic community actions: For each action: Identify specific problem addressed (e.g., '30% of students lack home internet'), Describe concrete action (e.g., 'Partner with public library to offer extended hours with free computers and WiFi'), Explain who would implement (school district, library system, community organization), Justify how action addresses root cause (e.g., 'Addresses infrastructure and cost barriers by providing free access point'), Estimate potential impact (e.g., 'Could serve 200 students in after-school hours'), (4) Present action proposals with supporting evidence: Reference specific data points justifying need, Explain feasibility and implementation steps, Compare to similar successful programs elsewhere. Students create proposal document with data visualizations, problem analysis, and action plans."

---

### 3. T35.G8.01.01 - Analyze AI chatbots' impact on information literacy (COMPLETE)

**CURRENT DESCRIPTION:**
"Following T22 chatbot projects, students analyze how AI-generated answers affect research habits, critical thinking, misinformation spread, and educational equity. They examine differential impacts on students with varying digital literacy levels and propose guidelines for responsible chatbot use in academic settings."

**REVISED DESCRIPTION:**
"Following T22 chatbot projects, students conduct comprehensive analysis of how AI chatbots affect information literacy. They: (1) **Research habits analysis:** Survey students: How has chatbot use changed your research process? Do you still consult multiple sources? Do you verify chatbot information?, Compare research process before/after chatbot access: Steps taken (direct answer vs. multi-source research), Time spent on research tasks, Quality of sources consulted, Document changes using table variables (columns: Research Aspect, Before Chatbots, After Chatbots, Impact), (2) **Critical thinking impact:** Test critical thinking by asking students to: Evaluate chatbot answers for accuracy (fact-check 5 responses), Identify missing context or nuance in chatbot answers, Recognize when chatbot is guessing vs. knows, Analyze: Are students more/less critical of information? Do students recognize limitations? What critical thinking skills are strengthened/weakened?, (3) **Misinformation risk:** Test chatbot responses for accuracy across domains (history, science, current events), Document misinformation instances using table variables, Analyze: What types of questions produce misinformation? Do students recognize false information? How does misinformation spread (sharing without verification)?, (4) **Educational equity impact:** Compare chatbot impact across student groups: Students with strong digital literacy vs. weak literacy, Students with prior research skills vs. limited skills, Native English speakers vs. English learners, Access to premium vs. free chatbot versions, Analyze differential impacts: Who benefits most from chatbots? Who faces new barriers? Does chatbot access reduce or increase education gaps?, (5) **Develop responsible use guidelines:** Synthesize findings into specific guidelines: When is chatbot use appropriate in academic settings? How should students verify chatbot information? How should students cite chatbot sources? What skills must students maintain despite chatbot availability? Include different guidelines for different literacy levels. Students present analysis with data visualizations and evidence-based guidelines."

**Dependencies:** T35.G8.01, T35.G7.01, T22.G8.01
**CSTA:** Information literacy and AI

---

## PRIORITY 4: VERIFY CROSS-TOPIC DEPENDENCIES

### Dependencies to Review

**T35.G5.04 → T19.G5.01 (Store data in Google Sheet)**
- **Question:** Is T19.G5.01 the first introduction to cloud storage, or is there earlier scaffolding?
- **Action:** Check T19 progression to verify G5 introduction is appropriate
- **If violation:** Add earlier T19 introduction at G3-G4, or delay T35.G5.04 to G6

**T35 Widget Dependencies (T16)**
- Multiple T35 skills depend on T16 widgets across grades
- **Action:** Verify T16 progression aligns with T35 needs:
  - G3: T16.G3.01 available for T35.G3.01, G3.03, G3.04? ✓
  - G4: T16.G4.01 available for T35.G4.01, G4.02, G4.03.01? ✓
  - G5: T16.G5.01 available for T35.G5.04? ✓
  - G6: T16.G6.01 available for multiple G6 skills? ✓
  - G7: T16.G7.01 available for multiple G7 skills? ✓
  - G8: T16.G8.01 available for T35.G8.03.01? ✓

**T35 AI Dependencies (T21-T24)**
- **Action:** Verify AI topics introduce tools before T35 ethics requires them:
  - T21.G6.01 before T35.G6.03.01a? ✓
  - T22.G3.01 before T35.G3.03? ✓
  - T22.G6.01 before T35.G6.01, G6.03.01b? ✓
  - T23.G6.01 before T35.G6.03.03a? ✓
  - T24.G6.01 before T35.G6.03.03b? ✓

---

## IMPLEMENTATION SUMMARY

### Before Optimization
- **Total skills:** 49
- **K:** 4, **G1:** 4, **G2:** 4, **G3:** 4, **G4:** 5, **G5:** 4, **G6:** 9, **G7:** 9, **G8:** 6

### After Optimization
- **Total skills:** ~74 (estimated)
- **K:** 4, **G1:** 4, **G2:** 5, **G3:** 4, **G4:** 5, **G5:** 5, **G6:** 13, **G7:** 16, **G8:** 8

### Changes
- **13 skills split into 37** (net +24 skills)
- **4 new scaffolding skills added** (+4 skills)
- **3 descriptions clarified** (no count change)
- **Cross-topic dependencies verified**

### Benefits
1. **Clearer learning objectives** - Each skill has focused, assessable outcome
2. **Better pacing** - Smaller steps reduce overwhelm
3. **Easier teaching** - Teachers can plan lessons around specific goals
4. **Better assessment** - Can evaluate mastery of specific competencies
5. **Maintained rigor** - Same comprehensive coverage, better organization
6. **Improved scaffolding** - Smoother transitions between grade levels

---

## NEXT STEPS

1. **Review and approve splits** - Verify proposed skill splits maintain learning goals
2. **Create new skill IDs** - Assign IDs to new skills (e.g., T35.G6.01.01, T35.G6.01.02)
3. **Update dependencies** - Revise dependency lists for split and new skills
4. **Add CSTA alignments** - Map skills to specific CSTA standards
5. **Review descriptions** - Ensure all descriptions are clear and complete
6. **Verify cross-topic dependencies** - Confirm T16, T19, T21-T24 progressions support T35
7. **Update allskills.md** - Implement all changes in master file
8. **Create teaching resources** - Develop examples and rubrics for new skills

---

**END OF RECOMMENDATIONS**
