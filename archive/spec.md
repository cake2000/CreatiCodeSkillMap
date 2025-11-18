# CreatiCode K–8 Skill Map – Codex CLI Agent Specification

## 0. Purpose

You are a Codex CLI agent.  
Your job is to design **an initial K–8 domain → topic → skill hierarchy** for CreatiCode, suitable for:

- Alignment to **CSTA K–12 standards** (especially K–8).
- Leveraging **CreatiCode’s extended capabilities** (3D, physics, AI blocks, XO assistant, etc.).
- Supporting **competition preparation** (ACSL, Scratch Olympiad, NOC, Lanqiao, Games for Change, Codeavour, ICode Global Hackathon, Congressional App Challenge, CSP-J/S in china, etc.).
- Eventually driving **auto-graded skill pages** inside CreatiCode.

The output should be **machine-usable** (JSON/YAML/CSV) and **human-readable** (markdown summaries).

You must treat the discussion and suggestions in this spec as **strong guidance, not immutable law**.  
If the CSTA standards, CreatiCode platform, or competition research suggest better structures or names, you should **improve on them**, not just copy them.

---

## 1. High-Level Objectives

You must:

1. **Define a classification hierarchy**:
   - A small number of **domains** (roughly aligned to CSTA Topic Areas).
   - **30–50 topics** grouped under those domains.
   - For each topic, a **K–8 skill progression** (skills per grade).

2. **Map everything explicitly**:
   - Each **topic** maps to one or more **CSTA Topic Areas** (Algorithms and Design, Programming, Data and Analysis, Systems and Security, Computing and Society).
   - Each **skill** maps to:
     - a single **topic**,
     - one **grade** (K, 1, 2, …, 8),
     - one or more **CSTA standard codes**,  
     - optional **competition tags**,
     - optional **CSTA pillars** as metadata (Impacts & Ethics, Inclusive Collaboration, Computational Thinking, Human-Centered Design),
     - optional **disposition tags** (creativity, persistence, etc.) as metadata, not taxonomy.

3. **Honor CreatiCode’s uniqueness**:
   - Explicitly include **3D**, **2D physics**, **AI & XO**, and other extensions as **first-class topics**.
   - Start **AI and 3D earlier** than CSTA’s formal HS AI standards, but keep them aligned to the K–8 general CS standards.

4. **Support auto-grading inside CreatiCode**:
   - Every skill must be **a concrete coding challenge** that can be **checked automatically** in the CreatiCode playground.
   - Non-executable “trivia” questions (block recognition, terminology) should be treated as **auxiliary pre-skills**, not core skills.

5. **Be grade-specific, not just grade-banded**:
   - CSTA is in grade bands (K–2, 3–5, 6–8). You must break skills down to **individual grades**.
   - Skills should show a clear **cognitive and technical progression** across grades.

---

## 2. Resources You Must Use

You **must** read and synthesize information from:

1. **CSTA Draft Standards (PDF)**
   - Path: `/mnt/data/Draft-2.0-Revised-PreK-12-CS-Standards.pdf`
   - Extract:
     - The 5 **Topic Areas** and definitions.
     - The detailed standards for **K–8**, with IDs and text.
     - The descriptions of **Pillars** and **Dispositions**.

2. **User’s AI Curriculum (to be attached)**
   - “A Hands-On Introduction to AI” – multiple modules and lessons.
   - Treat this as **authoritative** for how CreatiCode expects students to engage with AI and XO.
   - Extract:
     - Implicit AI topics (prompting, image generation, voice, vision, RAG, tools, XO debugging & planning).
     - Expected skill levels for middle school students.

3. **CreatiCode Platform / Codebase / Docs**
   - Explore the CreatiCode codebase and documentation (as available in the repo).
   - Crawl official CreatiCode docs and site online to learn:
     - Supported block categories.
     - 3D extension APIs (Babylon.js mappings, camera, physics).
     - AI-related blocks (ChatGPT, XO, vision, speech, tools, etc.).
     - Widgets, input methods, and any built-in testing/introspection APIs that can support auto-grading.

4. **External references (online research)**
   - **IXL skill structure** (to understand fine-grained topic/skill patterns and tagging).
   - **Competitions**:
     - ACSL (esp. Elementary / Junior divisions).
     - Scratch Olympiad / International Scratch competitions.
     - Chinese contests: NOC, 全国青少年信息素养大赛, 蓝桥杯青少组, “智慧杯”中小学生计算机程序设计大赛, etc.
     - Project competitions: Games for Change, Congressional App Challenge, ICode Global Hackathon, UnicMinds World Game Coding Competition, Codeavour, etc.
   - Extract from each:
     - Common patterns of tasks and required concepts.
     - Expected **age levels**.
     - Emphasis on planning, debugging, documentation, ethics, etc.

You must **update** and **adjust** the initial topic ideas in this spec based on what you discover.

---

## 3. Conceptual Model & Definitions

### 3.1 Domains

- **Domains** in our system are **aligned to CSTA Topic Areas** (1:1 or 1:many mapping).
- Initial domain set (you may refine/rename):

  1. **Algorithms & Design**  
  2. **Programming**  
  3. **Data & Analysis**  
  4. **Systems & Security**  
  5. **Computing & Society**

- For some UI/teacher-facing purposes, we may also define **pedagogical groupings** like:
  - Core Programming (2D)
  - Games & Interactive Media
  - Stories & Art
  - 3D & Simulation
  - AI & Smart Apps
  - Project Practices / Competition Prep  
  but these are essentially **views** over the domain/topic space.

### 3.2 Topics

- A **topic** is a mid-level concept area:  
  specific enough that we can write a **K–8 skill ladder** for it, but broad enough to have **multiple skills per grade**.
- There should be **30–50 topics total**.
- Examples (starting suggestions, not final):

  **Programming / Algorithms & Design**
  - Events & Sequencing
  - Basic Loops
  - Conditional Logic
  - Variables
  - Lists & Collections
  - Broadcasts & Messaging
  - Clones & Spawn Systems
  - Custom Blocks / Functions
  - Parallelism
  - Debugging Strategies

  **2D Games & Interaction**
  - Player Movement Systems
  - Collision Detection (2D)
  - Scoring & Health
  - Timers & Counters
  - Game Loops & States (start/play/end)
  - UI & Menus
  - Enemy Behavior Patterns
  - Level Progression & Difficulty Scaling

  **Storytelling, Animation & Art**
  - Sprite Design & Costumes
  - Scene Transitions & Camera Moves (2D)
  - Dialog & Narration
  - Character Animation
  - Sound & Music Integration
  - Visual Effects

  **Data & Information**
  - Variables for Tracking
  - Lists as Data Tables
  - Data Collection & Simple Experiments
  - Basic Statistics (min/max/average)
  - Data Visualization in Scratch/CreatiCode
  - Text as Data (parsing, string operations)

  **3D Worlds & Simulation**
  - 3D Coordinate Systems & Spatial Reasoning
  - Creating & Transforming 3D Objects
  - Materials & Lighting
  - 3D Camera & Navigation
  - 3D Collisions & Boundaries
  - 2D/3D Physics & Simulation

  **AI & Smart Apps**
  - AI-Generated Media (Backdrops & Sprites)
  - Prompting & Chatbot Design
  - AI-Based Content Creation (stories, quizzes, books)
  - XO as Coding & Learning Assistant
  - Voice Interfaces (Speech-to-Text / TTS)
  - Vision & Motion Interfaces (camera, pose, hand tracking)
  - LLM Reasoning in Interactive Apps
  - Information Processing & Summarization with AI
  - Tool-Using AI & RAG (semantic search, tools)

  **Project Development & Practices**
  - Reading & Interpreting Specifications
  - Task Decomposition & Planning
  - Storyboarding & UX Flows
  - Testing & Debugging Projects
  - Documentation & In-Project Help
  - Collaboration & Code Ownership
  - Performance & Optimization

  **Systems & Society**
  - Hardware & Software Basics
  - Networks & the Internet (conceptual)
  - Cybersecurity Basics (passwords, privacy)
  - Impacts of Computing on Society
  - Ethics of AI & Data

- For each topic you define, you must:
  - Assign **one primary CSTA Domain** and optional secondary domains.
  - Justify briefly why that topic fits that domain.
  - Mark whether it is:
    - **Core CS** (broadly applicable),
    - **CreatiCode-specific** (3D, XO, particular AI blocks),
    - **Competition-oriented** (primarily for contest prep).

### 3.3 Skills

- A **skill** is the smallest unit in this system and must be:

  1. **Concrete**: A clearly described coding challenge (“Make the sprite move to the right using a loop instead of repeated blocks”).
  2. **Executable**: Implemented inside a CreatiCode project.
  3. **Auto-checkable**: The system can verify correctness via:
     - runtime behavior (positions, scores, state changes),
     - project state (presence of specific sprites/variables),
     - code structure where necessary (loops, broadcasts, etc.).
  4. **Grade-specific**: Exactly one grade (K–8).
  5. **Topic-specific**: Exactly one topic.
  6. **Mappable**: Linked to CSTA standard codes and, optionally, competitions.

- For each skill, define at least the following fields:

  ```jsonc
  {
    "id": "T3.G4.02",               // or any stable ID scheme
    "title": "Use a loop to move 5 times",
    "domain": "Programming",
    "topic": "Basic Loops",
    "grade": 2,
    "description_teacher": "Students replace repeated move blocks with a repeat loop to move a sprite forward 10 steps 5 times.",
    "student_challenge": "Make the cat walk forward 5 times using a repeat block, not by duplicating move blocks.",
    "starter_project_ref": "creaticode://project/...",  // placeholder/format to be agreed later
    "expected_outcome": {
      "behavior": "sprite x-position increases by 50 in 5 equal steps when green flag clicked",
      "constraints": ["must use repeat-style loop block once", "no more than 2 'move 10 steps' blocks"]
    },
    "autograde_strategy": {
      "runtime_checks": [...],
      "static_checks": [...]
    },
    "csta_codes": ["E1-PRO-PF-01"],   // example; use real codes from the draft PDF
    "csta_domains": ["Programming", "Algorithms and Design"],
    "csta_pillars": ["Computational Thinking"],
    "dispositions": ["persistence"],
    "competitions": [
      {
        "name": "Lanqiao Scratch",
        "category": "loops and repetition",
        "relevance": "Required in timed mini-game tasks with repeated movement."
      }
    ],
    "dependencies": ["T1.G1.01"],    // prerequisite skill IDs
    "pre_skills": ["T1.G1.PS01"],    // optional trivia/pre-skill IDs
    "tags": ["2D", "loops", "core"]
  }
````

* **Pre-skills / Trivia**:

  * You **may** define small recognition-type items (e.g., “Identify the repeat block.”), but:

    * Tag them as `"type": "pre-skill"` or similar.
    * Use them primarily for **K–2** and early grade 3.
    * Do **not** treat them as core skills in the main progression.
    * Keep them short and clearly tied to adjacent core skills.

---

## 4. Design Principles You Must Follow

1. **Domains ≈ CSTA Topic Areas**

   * Domains must be easy to map to CSTA’s 5 Topic Areas.
   * This enables direct standards reports and easy teacher communication.

2. **Topics are finer-grained than CSTA Topic Areas**

   * Aim for **30–50 topics** in total.
   * Topics should be coherent and support a clear **K–8 progression**.

3. **Skills are smaller than CSTA Standards**

   * Standards are multi-week, multi-context learning goals.
   * Skills are **concrete mini-challenges** that can be completed in one sitting and auto-graded.

4. **Grade-specific, not band-specific**

   * You must break the progression down to **each grade K–8**.
   * Use CSTA banded expectations to place skills at appropriate grades.

5. **Auto-grading is mandatory for core skills**

   * Design skills with auto-grading in mind.
   * When exploring CreatiCode’s APIs, note any built-in introspection, event hooks, or project-inspection capabilities that help with grading.

6. **3D and AI are not afterthoughts**

   * They must appear in topics and skills **earlier than high school**, leveraging CreatiCode’s strengths.
   * However, they should still reinforce core CSTA K–8 concepts (Programming, Data, Impacts, etc.).

7. **Competition alignment is explicit, not implicit**

   * For each topic, identify:

     * which competitions it’s most relevant to,
     * at which age/grade the topic maps to real competition tasks.
   * For key competition pathways (ACSL, NOC, Lanqiao, G4C, Codeavour, ICode, CAC), identify **skill chains** that form natural prep sequences.

8. **Pillars and dispositions are metadata, not structure**

   * Do **not** turn them into topics.
   * Use them as annotations to flag:

     * Ethics-heavy skills,
     * Collaboration/project skills,
     * Creativity-intensive skills, etc.

9. **IZL-like granularity but coding-appropriate**

   * Keep skills small and specific (as IXL does), but always **artifact-producing**, not multiple-choice-only.
   * Recognition-based items stay as **pre-skills**, especially for early grades.

10. **Treat prior suggestions as baseline, not truth**

    * If your research reveals better naming, grouping, or sequencing, **change it**.
    * Document what you changed and why.

---

## 5. Required Outputs

You must produce at least the following artifacts (filenames can be adjusted, but structure should be clear):

### 5.1 Domain & Topic Definition

**File:** `domains_topics.yaml` (or `.json`)

Structure example:

```yaml
domains:
  - id: D1
    name: "Algorithms & Design"
    description: "Designing and analyzing algorithms and solutions."
    csta_mapping: ["Algorithms and Design"]

  - id: D2
    name: "Programming"
    description: "Writing, testing, and debugging programs."
    csta_mapping: ["Programming"]

  # ... D3–D5 for Data & Analysis, Systems & Security, Computing & Society

topics:
  - id: T01
    name: "Events & Sequencing"
    domain: "D2"
    primary_csta_domain: "Programming"
    secondary_csta_domains: ["Algorithms and Design"]
    description: "Using event blocks and ordered instructions to control program flow."
    type: "core"
    notes: "Covers event blocks, basic sequence, K–5 foundation for most coding tasks."

  - id: T15
    name: "Prompting & Chatbot Design"
    domain: "D2"
    primary_csta_domain: "Programming"
    secondary_csta_domains: ["Algorithms and Design", "Computing and Society"]
    description: "Designing and implementing text-based AI interactions via ChatGPT blocks."
    type: "creaticode_ai"
    notes: "Drawn from AI curriculum Module 2."
```

### 5.2 Skill Catalog

**File:** `skills.csv` or `skills.json`

Each row/object is a skill, including:

* ID, title, domain, topic, grade
* Teacher description, student-facing challenge
* CSTA codes
* CSTA pillar tags (optional)
* Disposition tags (optional)
* Competition tags (optional)
* Dependencies, pre-skills
* Auto-grading hints

### 5.3 Topic-by-Grade Matrix

**File:** `topic_grade_matrix.md` or `.csv`

A simple matrix for humans:

* Rows: topics
* Columns: grades K–8
* Cells: number of skills or a brief label (e.g., “intro”, “developing”, “mastery”).

This should let a human quickly see vertical progression.

### 5.4 Competition Pathways

**File:** `competition_paths.md`

For each major competition:

* Name of the competition
* Age/grade bands
* High-level categories of tasks/problems
* A list of **topics** and **skills** you recommend as a prep path.

Example outline:

```markdown
## ACSL Elementary

### Focus Areas
- Number systems
- Boolean logic
- Graphs
- Basic programming problems

### Relevant Topics
- Variables
- Lists & Collections
- Conditional Logic
- Algorithm Tracing & Debugging
- ...

### Recommended Skill Path (Grades 4–6)
- Txx.G4.03 – ...
- Tyy.G5.01 – ...
- ...
```

---

## 6. Process You Should Follow

1. **Ingest & Summarize**

   * Parse the CSTA PDF for K–8 standards, topic areas, pillars, dispositions.
   * Parse the AI curriculum and cluster its lessons into candidate topics.
   * Extract capabilities and APIs from CreatiCode codebase and docs.
   * Summarize competition requirements.

2. **Propose & Refine Domains/Topics**

   * Start from the domain/topic suggestions in this spec.
   * Adjust based on:

     * CSTA topics and level of detail.
     * CreatiCode-specific capabilities (3D, AI).
     * Competition patterns.

3. **Design Grade-Level Progressions**

   * For each topic, sketch K–8 expectations.
   * Decide which grades each topic is **introduced**, **developed**, and **mastered**.
   * Ensure prerequisites make sense.

4. **Generate Initial Skill Set**

   * For each topic-grade pair, generate multiple concrete skills.
   * Prioritize:

     * Coverage of CSTA standards,
     * Feasibility for auto-grading,
     * Reusability in competition prep and projects.

5. **Tag Skills**

   * Add CSTA codes, domain tags, pillar/disposition annotations.
   * Add competition tags where relevant.
   * Identify pre-skills (trivia) and keep them separate.

6. **Output Files & Short Narrative Summary**

   * Write out `domains_topics.yaml`, `skills.json/csv`, `topic_grade_matrix`, and `competition_paths`.
   * Provide a brief `README.md` summarizing:

     * Key design decisions,
     * Deviations from this spec (with reasons),
     * Known gaps or to-dos.

---

## 7. Quality Criteria

Your output is acceptable if:

* There are **30–50 well-defined topics**.
* Each topic has **multi-grade coverage** where appropriate.
* Every skill is:

  * grade-specific,
  * topic-specific,
  * concrete and auto-checkable,
  * mapped to CSTA codes.
* 3D and AI topics are integrated **throughout** the map, not isolated at the end.
* Competition pathways are plausible and capture the core patterns of the contests.
* The hierarchy can be used as the basis for:

  * a UI skill browser,
  * automatic practice selection,
  * future content generation (example projects, videos, etc.).

If you discover constraints or opportunities in the CreatiCode codebase that suggest better structures or auto-grading strategies, you must **document and leverage them**, even if it means changing topic boundaries or skill granularity.
