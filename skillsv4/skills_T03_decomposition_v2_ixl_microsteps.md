# T03 – Problem Decomposition: K–8 Skill List (v2, IXL‑Style Microsteps)

Topic reference: `T03 Problem Decomposition` in `domains_topics_overview.md`  
Domain: Algorithms & Design (D1) · Primary CSTA focus: ALG‑PS, PRO‑PM (with links to ALG‑AF, PRO‑TR)

This v2 version upgrades the original draft (`skills_T03_decomposition.md`) into an **IXL‑style microstep design**:

- **Role of T03:** Focused on *breaking problems down*, *planning projects*, and *organizing work* (routines, programs, and CreatiCode projects). It assumes everyday algorithm familiarity from **T01** and representation/tracing fluency from **T02**, and turns those into concrete plans and task breakdowns.  
- **Microsteps:** Each skill targets one narrow role (identify parts, group/subtasks, plan sequence, use checklists, track progress, refactor into modules, estimate scope), rather than bundling multiple practices. Within each strand, skills move in IXL‑style tiny steps from “notice parts” → “group” → “sequence” → “revise,” with no large jumps.  
- **Uneven density:** Heaviest coverage in **grades 3–6**, where students begin independent coding projects and need explicit scaffolds for planning and decomposition.  
- **Implementability:** All skills can be implemented with picture‑based K–2 activities, CreatiCode starter projects, block‑based coding, and simple planning UIs (lists of subproblems, checklists, drag‑drop grouping, etc.).

## Teacher Guidance & Sequencing

- **K–2:** Use T03 alongside T01/T02 to talk about “parts” and “steps” in everyday contexts. Keep prompts concrete and visual (objects, scenes, short routines), and avoid formal project‑management language with students.  
- **Grades 3–5:** Treat T03 as the planning companion for early coding topics (T06–T13) and application topics (T14–T20). Within a grade, start with identifying features and subtasks, then move to ordering tasks, assigning owners, and updating plans after feedback.  
- **Grades 6–8:** Use T03 to support larger projects and competitions: architecture sketches, milestones, risk/scope tradeoffs, and refactoring plans. XO‑related skills (`T03.G6.05`, `T03.G8.02`) can be framed as “AI‑assisted planning” where students *critically select and edit* AI suggestions.  
- **Cross‑topic:** Pair T03 with:
  - **T01/T02** when turning algorithms and diagrams into project tasks.  
  - **T05** when emphasizing user needs, accessibility, and simulation design.  
  - **T25–T27** when planning data‑heavy projects that require explicit decisions about what to collect and analyze.  
  - **T21–T24/T35–T36** when planning or critiquing AI‑related projects that need clear decomposition and documentation.

IDs follow `T03.G<grade>.<nn>`. v1 IDs are preserved conceptually; additional microsteps use higher `<nn>` values and can be wired into the JSON maps in a later data pass.

---

## Grade K (PreK–K) – Parts and Steps in Everyday Routines

Strands: **K‑A See parts of a whole**, **K‑B Simple step breakdowns**

### K‑A: See parts of a whole

**T03.GK.01 – Identify parts that make up a whole**  
Students look at familiar objects or scenes (e.g., playground, classroom, robot) and tap pictures of individual parts (slide, swings, door, wheels).  
_Format:_ Picture hotspot/click‑select; auto‑graded by matching labeled parts. · _CSTA:_ EK‑ALG‑PS‑03.

**T03.GK.02 – Match parts to whole objects**  
Students match close‑up pictures of parts (e.g., wheel, keyboard) to the whole object they belong to (car, computer).  
_Format:_ Drag part onto whole; auto‑graded by correct pairings. · _CSTA:_ EK‑ALG‑PS‑03.

### K‑B: Simple step breakdowns

**T03.GK.03 – Order 3–4 pictures to show steps in a routine**  
Students arrange 3–4 pictures to show steps in a classroom or home routine (e.g., wash hands) specifically as a *plan* for getting the task done, building on the sequence sense learned in T01.  
_Format:_ Drag‑drop sequence into a simple “plan strip”; auto‑graded by final order. · _CSTA:_ EK‑PRO‑PM‑05.

**T03.GK.04 – Choose the missing middle step in a routine**  
Students see the first and last steps of a 3‑step routine and choose the picture that fits in the middle so the *plan* for the task makes sense.  
_Format:_ MCQ picture choice; auto‑graded. · _CSTA:_ EK‑PRO‑PM‑05.

---

## Grade 1 – Decomposing Simple Tasks and Scenes

Strands: **1‑A Parts & roles**, **1‑B Break tasks into steps**

### 1‑A: Parts & roles

**T03.G1.01 – Describe what one part of a system does**  
Students select a part in a picture (e.g., wheels, door, button) and choose what it does from options.  
_Format:_ Click part → MCQ function; auto‑graded by correct pairing. · _CSTA:_ E1‑ALG‑PS‑03.

**T03.G1.02 – Group related parts into categories**  
Students drag parts into groups such as “input,” “movement,” or “decoration” for a simple object (e.g., robot or game scene).  
_Format:_ Sort‑into‑buckets; auto‑graded by category. · _CSTA:_ E1‑ALG‑PS‑03.

### 1‑B: Break tasks into steps

**T03.G1.03 – List steps for a simple classroom routine**  
Students build a 3–4 step plan for a familiar routine (e.g., “line up for recess”) using picture or word cards in order.  
_Format:_ Drag cards to numbered slots; auto‑graded by order. · _CSTA:_ E1‑PRO‑PM‑05.

**T03.G1.04 – Match steps to parts of a tiny story or game**  
Students see a tiny story or game idea (e.g., “A cat says hello, then dances”) and match which step goes with each character or scene.  
_Format:_ Drag step labels onto characters/scenes; auto‑graded by mapping. · _CSTA:_ E1‑PRO‑PM‑05.

---

## Grade 2 – From Routines to Subtasks and Simple Plans

Strands: **2‑A Break problems into subtasks**, **2‑B Use checklists and simple plans**

### 2‑A: Break problems into subtasks

**T03.G2.01 – Choose subtasks for a simple project idea**  
Students read or hear a small project idea (e.g., “Make a greeting card project”) and select which subtasks are needed (e.g., “draw background,” “add message,” “add sound”).  
_Format:_ MCQ multi‑select; auto‑graded by needed subtasks. · _CSTA:_ E2‑ALG‑PS‑03.

**T03.G2.02 – Group similar subtasks together**  
Students drag subtasks into groups like “art,” “words,” “sound” for a small project.  
_Format:_ Sort‑into‑categories; auto‑graded. · _CSTA:_ E2‑ALG‑PS‑03.

### 2‑B: Use checklists and simple plans

**T03.G2.03 – Arrange subtasks into a reasonable order**  
Students take 4–5 subtasks and order them into a simple plan (e.g., plan → create → try it out).  
_Format:_ Drag‑drop ordering; auto‑graded by acceptable sequences. · _CSTA:_ E2‑PRO‑PM‑05.

**T03.G2.04 – Use a checklist to track progress on a mini‑project**  
Students see a mini‑project checklist and must mark which subtasks are done based on a short story (“We already drew the characters and added sounds.”).  
_Format:_ Click‑to‑check items; auto‑graded by story. · _CSTA:_ E2‑PRO‑PM‑05.

---

## Grade 3 – Decomposing First Real Projects

Strands: **3‑A Break coding tasks into features**, **3‑B Storyboards & scene plans**, **3‑C Plan‑then‑build**

### 3‑A: Break coding tasks into features

**T03.G3.01 – Identify features in a small game description**  
Students read a short game description and highlight or select each distinct feature (e.g., player controls, scoring, win/lose screen).  
_Format:_ Highlight or multi‑select; auto‑graded by feature list. · _CSTA:_ E3‑ALG‑PS‑03.

**T03.G3.02 – Group features into “must‑have” vs “nice‑to‑have”**  
Students drag feature cards into two buckets: essential vs extra.  
_Format:_ Sort‑into‑two‑buckets; auto‑graded. · _CSTA:_ E3‑PRO‑PM‑05.

### 3‑B: Storyboards & scene plans

**T03.G3.03 – Create a 3‑panel storyboard for a project**  
Students arrange 3 pictures showing beginning, middle, and end of a simple animation or game level.  
_Format:_ Drag panels into order; optional captions; auto‑graded by structure. · _CSTA:_ E3‑PRO‑PM‑05.

**T03.G3.04 – Match storyboard panels to CreatiCode scenes**  
Students match each storyboard panel to a scene or backdrop in a starter CreatiCode project.  
_Format:_ Drag labels or panels onto scene thumbnails; auto‑graded. · _CSTA:_ E3‑PRO‑PM‑05.

### 3‑C: Plan‑then‑build

**T03.G3.05 – Choose a step‑by‑step plan for a small project**  
Students see 2–3 alternative project plans and select which plan is more reasonable (e.g., “draw → code → test” vs “test → code → draw”).  
_Format:_ Plan comparison MCQ; auto‑graded. · _CSTA:_ E3‑PRO‑PM‑05.

**T03.G3.06 – Link each subtask to a specific sprite or script**  
Students assign subtasks (e.g., “make cat jump on space key”) to a sprite and script in a starter project.  
_Format:_ Drag subtasks onto sprite/script slots; auto‑graded by mapping. · _CSTA:_ E3‑PRO‑PM‑05.

---

## Grade 4 – Feature Decomposition, Roles, and Iteration

Strands: **4‑A Break bigger ideas into components**, **4‑B Plan responsibilities & collaboration**, **4‑C Iterate on plans**

### 4‑A: Break bigger ideas into components

**T03.G4.01 – Break a medium‑size project into components**  
Students are given a description of a project (e.g., “quiz game with levels”) and identify components like “question bank,” “score tracker,” “level manager,” “UI.”  
_Format:_ Feature/component selection; auto‑graded. · _CSTA:_ E4‑ALG‑PS‑03.

**T03.G4.02 – Group related components into modules**  
Students drag components into higher‑level modules (e.g., “game logic,” “user interface,” “data”).  
_Format:_ Sort‑into‑modules; auto‑graded. · _CSTA:_ E4‑ALG‑PS‑03.

### 4‑B: Plan responsibilities & collaboration

**T03.G4.03 – Assign project tasks to team roles**  
Students match tasks (e.g., “design sprites,” “write score code”) to team roles (e.g., artist, programmer, tester).  
_Format:_ Drag‑drop task‑to‑role mapping; auto‑graded. · _CSTA:_ E4‑PRO‑PM‑05.

**T03.G4.04 – Create a simple task list with owners and order**  
Students build a table listing task, owner, and “do first/next/last” for a small team project.  
_Format:_ Fill‑in table using dropdowns; auto‑graded by dependencies. · _CSTA:_ E4‑PRO‑PM‑05.

### 4‑C: Iterate on plans

**T03.G4.05 – Spot a missing or unnecessary task in a plan**  
Students read a short project plan and identify one missing critical task or one clearly unnecessary task.  
_Format:_ MCQ identify “missing” or “extra”; auto‑graded. · _CSTA:_ E4‑ALG‑PS‑03, E4‑PRO‑PM‑05.

**T03.G4.06 – Update a plan after testing feedback**  
Students see test feedback (“The game crashes when score is 0”) and choose which new tasks should be added to the plan.  
_Format:_ Multi‑select tasks; auto‑graded. · _CSTA:_ E4‑PRO‑PM‑05, E4‑PRO‑TR‑09.

---

## Grade 5 – Structured Project Planning and Risk Awareness

Strands: **5‑A Structured decomposition artifacts**, **5‑B Dependencies & risks**, **5‑C Plan comparison**

### 5‑A: Structured decomposition artifacts

**T03.G5.01 – Create a feature list and subtask breakdown**  
Students read a project pitch and produce a structured list: main features with 2–3 subtasks each.  
_Format:_ Simple outlining tool; auto‑graded by coverage and structure. · _CSTA:_ E5‑ALG‑PS‑03, E5‑PRO‑PM‑05.

**T03.G5.02 – Draw a high‑level project map**  
Students create a simple diagram showing how key screens/levels or components connect (e.g., “menu → level 1 → level 2 → game over”), focusing on *project structure* (screens/modules), not algorithm branching (which is covered in T02).  
_Format:_ Node‑and‑arrow diagram for screens/components; auto‑graded by connectivity and labels. · _CSTA:_ E5‑PRO‑PM‑05.

### 5‑B: Dependencies & risks

**T03.G5.03 – Identify task dependencies in a project plan**  
Students examine a list of tasks and mark which ones must be done before others (e.g., “draw sprites before code movement”).  
_Format:_ Check dependency arrows or ordering; auto‑graded. · _CSTA:_ E5‑PRO‑PM‑05.

**T03.G5.04 – Flag high‑risk or unclear tasks**  
Students highlight tasks that are vague or risky (e.g., “make AI for enemies” with no details) and choose clarifying sub‑tasks.  
_Format:_ Highlight + MCQ clarifications; auto‑graded. · _CSTA:_ E5‑PRO‑PM‑05.

### 5‑C: Plan comparison

**T03.G5.05 – Compare two project plans for the same idea**  
Students compare two project plans and choose which is more realistic or better organized, citing specific differences (e.g., clear subtasks, dependencies).  
_Format:_ MCQ + short justification; auto‑graded by key phrases. · _CSTA:_ E5‑ALG‑PS‑03, E5‑PRO‑PM‑05.

---

## Grade 6 – Modular Design and Iterative Planning

Strands: **6‑A Modular design & refactoring**, **6‑B Iterative milestones**, **6‑C Planning with XO**

### 6‑A: Modular design & refactoring

**T03.G6.01 – Propose modules for a medium CreatiCode project**  
Students read about an existing project and propose modules (e.g., “player control,” “enemy behavior,” “scoring”), grouping related sprites and scripts.  
_Format:_ Drag sprites/scripts into module boxes; auto‑graded. · _CSTA:_ MS‑ALG‑PS‑06.

**T03.G6.02 – Refactor a messy script into helper blocks**  
Students see an overlong script and choose which pieces could be turned into custom blocks (e.g., “check collision,” “reset level”), then label those blocks.  
_Format:_ Highlight code segments + name custom blocks; auto‑graded by coverage. · _CSTA:_ MS‑ALG‑PS‑06, MS‑PRO‑PM‑16.

### 6‑B: Iterative milestones

**T03.G6.03 – Break a project into milestones (v1/v2/v3)**  
Students organize tasks into “first version,” “improvements,” and “stretch goals” columns.  
_Format:_ Kanban‑style drag‑drop; auto‑graded by reasonable ordering. · _CSTA:_ MS‑PRO‑PM‑16.

**T03.G6.04 – Adjust milestones after discovering a constraint**  
Students read that a feature is harder than expected and adjust milestones (e.g., moving it from v1 to v2 and adding simpler fallback tasks).  
_Format:_ Edit milestone board; auto‑graded by changes. · _CSTA:_ MS‑PRO‑PM‑16.

### 6‑C: Planning with XO

**T03.G6.05 – Use XO to expand a basic idea into subtasks**  
Students start with a short idea, ask XO for subtasks, and then select which suggestions to keep, modify, or discard.  
_Format:_ XO‑assisted planning prompt + selection; auto‑graded by coverage and edits. · _CSTA:_ MS‑PRO‑PM‑16.

---

## Grade 7 – Architecture, Tradeoffs, and Testing Plans

Strands: **7‑A Architecture sketches**, **7‑B Tradeoffs & alternatives**, **7‑C Testing and refinement plans**

### 7‑A: Architecture sketches

**T03.G7.01 – Draw an architecture diagram for a multi‑sprite game**  
Students create a diagram showing main sprites, key data (variables/lists), and message flows for a multi‑sprite game, treating it as a *high‑level architecture view* of components and their communication rather than a detailed step‑by‑step algorithm (which lives in T02).  
_Format:_ Node‑and‑arrow editor; auto‑graded by presence of required nodes/links. · _CSTA:_ MS‑ALG‑PS‑07, MS‑PRO‑PM‑16.

**T03.G7.02 – Map code modules to architecture components**  
Students match existing CreatiCode scripts/custom blocks to components in an architecture diagram.  
_Format:_ Drag scripts onto component boxes; auto‑graded. · _CSTA:_ MS‑ALG‑PS‑07.

### 7‑B: Tradeoffs & alternatives

**T03.G7.03 – Compare two decompositions of the same project**  
Students compare two architecture sketches or task breakdowns and decide which is better in terms of clarity, reuse, and ease of change.  
_Format:_ MCQ + justification; auto‑graded by key reasoning. · _CSTA:_ MS‑ALG‑PS‑06.

**T03.G7.04 – Propose an alternative decomposition to fix a planning problem**  
Students are given a project suffering from duplicated code or tangled scripts and propose a new module breakdown to fix it.  
_Format:_ Short structured response; auto‑graded with rubric keywords. · _CSTA:_ MS‑ALG‑PS‑06, MS‑PRO‑PM‑16.

### 7‑C: Testing and refinement plans

**T03.G7.05 – Design a test plan based on a project breakdown**  
Students list test cases for each major feature/module (e.g., “test enemy movement,” “test scoring”).  
_Format:_ Table with feature → test cases; auto‑graded by coverage. · _CSTA:_ MS‑PRO‑PM‑16, MS‑PRO‑TR‑14.

**T03.G7.06 – Update a project plan after test results**  
Students read test results and insert new tasks (e.g., “fix bug,” “add edge‑case handling”) into the plan in reasonable places.  
_Format:_ Edit task list; auto‑graded by placement. · _CSTA:_ MS‑PRO‑PM‑16, MS‑PRO‑TR‑14.

---

## Grade 8 – Large‑Scale Planning, Documentation, and Realistic Scope

Strands: **8‑A Large‑scale planning & specs**, **8‑B Scope & effort**, **8‑C Refactoring large codebases**

### 8‑A: Large‑scale planning & specs

**T03.G8.01 – Outline a formal project specification**  
Students fill in a structured template (Overview, Features, Data, UI, Testing) for a substantial project, focusing on clear decomposition into sections and subsections.  
_Format:_ Template completion; auto‑graded by presence and structure. · _CSTA:_ MS‑PRO‑PM‑16, MS‑ALG‑PS‑07.

**T03.G8.02 – Use XO to refine and check a project spec**  
Students provide a draft spec to XO, ask for missing pieces or risks, and then integrate selected suggestions into their spec.  
_Format:_ XO interaction + spec edits; auto‑graded by incorporation of new subtasks/risks. · _CSTA:_ MS‑PRO‑PM‑16.

### 8‑B: Scope & effort

**T03.G8.03 – Rank project ideas by complexity and timeline**  
Students compare several project ideas and rank them from quickest to most ambitious, giving reasons tied to features, dependencies, and unknowns.  
_Format:_ Ordering + explanation; auto‑graded by ranking and rationale. · _CSTA:_ MS‑ALG‑PS‑05, MS‑PRO‑PM‑16.

**T03.G8.04 – Identify over‑scoped plans and suggest right‑sizing**  
Students analyze a too‑ambitious plan and suggest ways to trim scope or phase features over time.  
_Format:_ MCQ + short answer; auto‑graded by key phrases. · _CSTA:_ MS‑PRO‑PM‑16.

### 8‑C: Refactoring large codebases

**T03.G8.05 – Propose a refactoring plan for a complex project**  
Students review a description of a messy but working multi‑sprite project and propose a high‑level plan to reorganize it into modules, custom blocks, and clearer scripts.  
_Format:_ Structured outline; auto‑graded by presence of core refactoring ideas. · _CSTA:_ MS‑PRO‑PM‑16, MS‑ALG‑PS‑07.

**T03.G8.06 – Map refactoring tasks to future milestones**  
Students take a list of refactoring tasks and assign them to future releases (e.g., “v1.1 bugfixes,” “v1.2 architecture cleanup”).  
_Format:_ Milestone board drag‑drop; auto‑graded. · _CSTA:_ MS‑PRO‑PM‑16.

---

### Notes on Dependencies and Alignment

- K–2 T03 skills depend primarily on T01 (everyday algorithms) and T02 K–2 (representing/tracing basic sequences). Kindergarten and Grade 1 T03 “routine planning” skills assume students can already order and fix sequences from T01, and shift the focus to seeing *parts and subtasks* of bigger tasks.  
- G3–5 T03 skills depend on core coding topics (especially T06 Events and T07 Loops) and on T02’s diagram/tracing fluency. They build planning capacity for gateway skills and early projects by moving in small steps from identifying features → grouping into components → ordering tasks, always in the context of real CreatiCode projects.  
- G6–8 T03 skills assume solid programming core (T06–T13), earlier T03 decomposition habits, and T02’s algorithm‑diagram skills. They focus on architecture, milestones, risk/scope, and refactoring plans; they should not serve as prerequisites for learning core constructs, but rather as supports for larger projects and competition‑style work.  
- XO‑assisted skills (`T03.G6.05`, `T03.G8.02`) should be aligned in metadata with AI4K12 priorities around ethical AI system design and human–AI collaboration (categories D/E), with an emphasis on students critiquing and refining AI output rather than accepting it wholesale.  
- This design aligns with CSTA ALG‑PS and PRO‑PM/PRO‑TR progressions while keeping each skill small, clear, and CreatiCode‑implementable and making the roles of T01 (everyday algorithms), T02 (algorithm diagrams & tracing), and T03 (planning/decomposition) complementary with no major duplication.
