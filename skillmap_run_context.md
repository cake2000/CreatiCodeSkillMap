# CreatiCode K–8 Skill Map – Context for Automated Skill Refinement

This file is the **single context document** used by automation scripts (for example, `runonebyone.js`) when refining skills in `skillsv5/allskills.md`.

It summarizes the **data model, constraints, and quality goals** that every autonomous pass must respect.

---

## 1. Big Picture

- The CreatiCode K–8 Skill Map covers **computer science and AI** for grades **K–8**.  
- Skills are organized into:
  - **5 domains** (Algorithms & Design, Programming Core, Applications & AI, Data & Analysis, Systems & Society).  
  - **Topics** (`T01`–`T34`) within each domain.  
  - **Skills** at specific grades (K, 1–8) inside each topic.
- The **current working file** is `skillsv5/allskills.md`, which stores all skills in one place with IXL-style **micro-step granularity**.

Other documents:
- `00-START-HERE.md` – working-repo overview (human + LLM orientation).  
- `spec_v2_updated.md` – design contract (domains, topics, K–2 framework, dependency philosophy, AI4K12/CSTA alignment, gateway skills).  
- `creaticode.md` – platform and blocks reference (what is actually possible in CreatiCode).

Automation should treat:
- `skillsv5/allskills.md` as the **source of truth** for current skills and dependencies.  
- `spec_v2_updated.md` + this file as the **rules and intent** that edits must follow.

---

## 2. Data Model & File Structure

### 2.1 Topics and Grades

- Topics are identified by codes `T01`–`T34` (e.g., `T09` = Variables & Expressions, `T18` = 3D Worlds & Games).  
- Grades:
  - `GK` = Kindergarten  
  - `G1`–`G8` = Grades 1–8  
- Each topic section in `skillsv5/allskills.md` begins with a header like:
  - `# T09 - Variables & Expressions (…notes…)`

### 2.2 Skill IDs

Each skill has a unique ID on a line like:

`ID: T09.G4.05` or `ID: T09.G4.05.02`

Parts:
- `T09` – topic code  
- `G4` – grade  
- `05` – skill index within topic+grade  
- Optional `.02` – micro-step index under that skill

Immediately after the ID, each skill block contains:
- `Topic:` – topic name  
- `Skill:` – short, active-verb title  
- `Description:` – full student task and implementation notes  
- Optional `Dependencies:` block listing prerequisite skill IDs as `* Txx.Gy.nn` bullets

---

## 3. Pedagogical Model (K–2 vs 3–8)

### 3.1 Grades K–2

- **No coding required.**  
- Activities are **picture-based** and auto-gradable in 2–5 minutes.  
- Allowed interaction types (examples):
  - Drag-drop sequence  
  - Sort into categories  
  - Match pairs  
  - Click-to-select correct items  
  - Pattern completion  
  - Hot-spot click on an image  
  - Yes/No or safe/unsafe sort  
  - Visual multiple-choice  
  - Counting interactions  
  - Simple grid/maze path tracing
- Accessibility (WCAG 2.1 AA mindset):
  - Text-to-speech for instructions  
  - Large tap targets  
  - High contrast, clear visuals  
  - Keyboard navigation and screen reader compatibility

When editing K–2 skills:
- Keep tasks **visual, concrete, and developmentally appropriate**.  
- Make sure each skill is a **single, small conceptual step**, not a project.

### 3.2 Grades 3–8

- **Block-based programming in CreatiCode.**  
- Skills are **coding tasks** that can be auto-graded via:
  - Project state (sprites, variables, lists, tables, blocks present)  
- Each skill must describe:
  - A specific behavior the student’s project should exhibit, **and**  
  - Enough implementation detail for an auto-grader to check it.

When editing Grade 3–8 skills:
- Use **active verbs**: “Create…”, “Use…”, “Debug…”, “Explain…”, “Trace…”, “Predict…”, “Refactor…”.  
- Avoid vague verbs like “Understand” or “Learn about”.  
- Tie tasks to realistic use of CreatiCode features (3D, physics, AI blocks, widgets, multiplayer, table variables, etc.) when appropriate.

---

## 4. Dependencies & Learning Pathways

Dependencies are **central** to the skill map and must be preserved or improved, not ignored.

### 4.1 X–2 Rule

For any skill at grade **X**:
- It may depend only on skills in **grades X, X–1, or X–2**.  
  - Example: Grade 5 skills → allowed dependencies in **G3, G4, G5**.  
  - K and Grade 1 have limited backward options (GK depends mostly on GK; G1 on GK/G1).

### 4.2 Principles

- Dependencies should be:
  - **Direct** (no long chains of redundant prerequisites)  
  - **Acyclic** (no cycles)  
  - **Pedagogically real** prerequisites (true “need this first” relationships)
- Certain “gateway” skills (e.g., Grade 3 events, loops, conditionals, variables, debugging) unlock many later skills; they should not be weakened or skipped.

When editing dependencies:
- **Do not delete** a dependency unless it is clearly wrong.  
- Prefer **adding missing** but necessary dependencies.  
- Always verify the X–2 rule and remove / adjust any violations you create.  
- Never introduce cycles.

---

## 5. Goals for Automated Refinement Passes

Automation runs in two main modes (mirroring the prompts in `runonebyone.js`):

### 5.1 Topic-Focused Passes (Phase 1)

Scope: **One topic across all grades (K–8)**.

Goals:
- **Internal coherence & progression**
  - Ensure skills within a topic form a clear ladder from foundational to advanced.  
  - Fix ordering issues and clarify Grade K–2 → Grade 3 → upper-grade progressions.

- **Granularity & micro-steps**
  - Split overly broad skills into smaller micro-steps where helpful.  
  - Use sub-IDs like `T09.G4.05.01`, `T09.G4.05.02` for multi-step skills.  
  - Avoid duplicate or overlapping skills within the same topic.

- **Skill quality**
  - Rewrite titles and descriptions for clarity and specificity.  
  - Ensure tasks are auto-gradable, with clear student actions and expected outcomes.  
  - Reference CreatiCode blocks and features realistically (check `creaticode.md`).

- **Intra-topic dependencies only**
  - Fix missing or incorrect dependencies **inside this topic**.  
  - Respect the X–2 rule.  
  - **Do not change cross-topic dependencies** during Phase 1.

### 5.2 Grade + Topic Passes (Phase 2)

Scope: **One grade + one topic**, and only if that combination has skills.

Goals:
- **Cross-topic dependencies**
  - Add missing dependencies to other topics when a skill clearly requires them.  
  - Examples:
    - Cybersecurity/Digital Citizenship topics supporting Connected Services/Multiplayer.  
    - Math-heavy skills (variables, probability) feeding into Data Science topics.  
    - UI-related skills supporting app-style projects elsewhere.

- **Grade-level coherence within the grade**
  - Ensure that for a given grade, foundational skills are in place before advanced applications.  
  - Add dependencies inside the same grade and topic when one skill obviously builds on another.

Rules:
- Only modify **Grade X skills** in the current topic when the prompt says so.  
- Preserve intra-topic structure from Phase 1; focus on inter-topic links and grade-level coherence.  
- Respect the X–2 rule and avoid cycles.

---

## 6. Editing Rules & Priorities

Across all automated passes:

- **Do not delete skills** unless the prompt explicitly allows it and the skill is clearly redundant or harmful.  
- **Do not edit skills in other topics or grades** beyond the current scope (topic vs grade+topic) defined in the prompt.  
- **Do not break or weaken gateway skills** (`T06.G3.01`, `T07.G3.01`, `T08.G3.01`, `T09.G3.01`, `T13.G3.01`, etc.).  
- Always keep:
  - K–2 picture-based vs 3–8 coding distinction  
  - Auto-grading feasibility  
  - CSTA and AI4K12 alignment in mind (see `spec_v2_updated.md` and related docs for details).

When in doubt:
- Prefer **clearer, more concrete skill descriptions**.  
- Prefer **more explicit and correct dependencies** rather than fewer.  
- Keep the skill map **structured, teachable, and realistic** for actual students using CreatiCode.

---

Use this file as the **single reference** for how the skill map works and what good edits look like when running autonomous refinement scripts.

