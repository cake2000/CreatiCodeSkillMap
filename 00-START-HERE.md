# CreatiCode K–8 Skill Map – START HERE (Working Repo)

This repository is the **working home** for the CreatiCode K–8 Skill Map: all topics, skills, specs, and scripts used to refine the curriculum over multiple iterations.

It now contains both:
- The original **v2 concept-level spec** (≈1,119 skills across 34 topics), and  
- The newer **v5 micro-skill implementation** (≈2,900 IXL-style micro-skills) in `skillsv5/allskills.md`, which is what current scripts edit.

If you are improving skills (manually or via automation), this file explains **which artifacts matter now** and how they fit together.

---

## 1. What You Have Right Now

### Core Design & Specs
- `spec_v2_updated.md` – Updated v2 specification for the K–8 skill map  
  - Defines domains, topics, grade bands, K–2 picture framework, dependencies, gateway skills, AI4K12 alignment, and design principles.  
  - All numeric counts (1,119 skills, 4,167 dependencies, 34 topics) refer to the **concept-level v2 map**, not the expanded micro-skill files.

- `docs/domains_topics_overview.md` – Human-readable overview of **all topics and domains**  
  - Currently lists **36 topics (T01–T36)** from an earlier draft.  
  - The **current optimization loop (skillsv5 + runonebyone.js) only uses T01–T34**.  
  - Treat **T35 Impacts** and **T36 Ethics/Careers** as archived / folded into other topics for now.

- `docs/topic_grade_matrix.md` – Topic × Grade coverage matrix (concept-level view).  
  - Use for a quick sense of which grades each topic spans.  
  - May not reflect the latest micro-skill counts in `skillsv5/allskills.md`, but the structure is still valid.

### Current Canonical Skill File (v5)
- `skillsv5/allskills.md` – **Single source of truth for the current skill map**  
  - Contains **all K–8 skills** in one file, organized by topic headers like `# T09 - Variables & Expressions`.  
  - Uses **micro-skill granularity** (IXL-style steps); each topic often has 80–130 skills.  
  - Includes:
    - `ID:` line (e.g., `ID: T09.G4.05`)  
    - `Topic:` line  
    - `Skill:` line (title)  
    - `Description:` (full student-facing + implementation notes)  
    - Optional `Dependencies:` block listing prerequisite skill IDs.
  - This is the file that **runonebyone.js reads and writes**.

### Platform & Standards References
- `creaticode.md` – Detailed description of the CreatiCode platform:  
  - Scratch-like environment, extensions (3D, physics, AI blocks, widgets, table variables, multiplayer, etc.).  
  - Constraints and capabilities you should respect when designing or editing skills.

- `cstastandard.md` – CSTA K–12 standards reference.  
- `docs/AI-Priorities-for-All-K-12-Students-Report-from-CSTA-AI4K12.md` + `AI4K12_MAPPING.json` – AI4K12 priorities and mapping.  
- `docs/QUICK_REFERENCE.md` and `docs/QUICK_START_GUIDE.md` – Additional high-level summaries of domains, topics, and usage patterns.

### Legacy / Reference Files
These are **reference-only** for historical context; do **not** edit them when working on v5:

- `skillsv1/domains_topics.yaml` – Original machine-readable domain/topic definitions.  
- `skillsv1`, `skillsv3`, `skillsv4` per-topic skill files – Earlier generations of the skill map.  
- `skills_final_enriched.json`, `skills_k8_ai_complete.json` (if present in archive / tools) – Older JSON exports used for comparison and enrichment.

---

## 2. Structural Snapshot (What the System Looks Like)

- **Grades:** K–8 (**9 grade levels**: K, 1, 2, 3, 4, 5, 6, 7, 8).  
- **Topics (current working set):** 34 topics `T01`–`T34` as defined in `docs/domains_topics_overview.md` and `runonebyone.js`.  
  - Older documents sometimes include `T35` and `T36`; these are **not** part of the current v5 optimization loop.
- **Domains (conceptual, from spec_v2_updated):**
  - **D1 – Algorithms & Design** (T01–T05)
  - **D2 – Programming Core** (events, loops, conditionals, variables, lists, functions, organization/debugging)
  - **D3 – Applications & AI** (games, UI, physics, 3D, multiplayer, algorithmic art, AI tools)
  - **D4 – Data & Analysis** (data representation, collection, analysis, chance & simulations, text/NLP)
  - **D5 – Systems & Society** (hardware, internet, cybersecurity, citizenship, history/impacts/ethics)

### Skill IDs

Every skill has a **stable ID**:

- Pattern: `TXX.GY.NN` or `TXX.GY.NN.SS`  
  - `TXX` – Topic code, e.g., `T09` Variables & Expressions  
  - `GY` – Grade code: `GK` for Kindergarten, `G1`–`G8` for grades 1–8  
  - `NN` – Two-digit skill index within that topic+grade  
  - Optional `.SS` – Sub-skill index for micro-steps

Example:
- `T09.G3.01` – First Grade 3 skill in Variables & Expressions  
- `T09.G5.04.02` – Second micro-step under skill `.04` in T09 Grade 5

Dependencies are listed explicitly in `skillsv5/allskills.md` under a `Dependencies:` block as bullet-pointed skill IDs.

---

## 3. K–2 vs 3–8 Model (Critical for Editing)

From `spec_v2_updated.md` and the K–2 framework docs:

- **K–2 (GK–G2):**  
  - No coding required.  
  - Activities are **picture-based**, short (2–5 minutes), and auto-gradable:
    - Drag-drop sequences, sort into categories, match pairs, click-to-select, pattern completion, hot-spot clicks, yes/no sort, picture-based MCQ, counting interactions, path tracing.  
  - Must follow accessibility guidelines (audio support, large touch targets, high contrast, keyboard navigation, screen-reader friendly).

- **Grades 3–8:**  
  - **Block-based coding in CreatiCode.**  
  - Skills describe concrete coding tasks (e.g., “create and use a variable to track score”).  
  - Auto-grading relies on runtime checks, project state, and sometimes code-structure checks.

When editing or creating skills:
- Keep K–2 skills **visual, concrete, and very focused**.  
- Keep G3–8 skills **code-based, precise, and testable** in CreatiCode.

---

## 4. Dependency Philosophy (X–2 Rule)

Dependencies are a core part of this system:

- Each skill lists **direct prerequisites only** (no transitive closure).  
- **X–2 rule:** A Grade X skill may depend only on skills in grades **X, X–1, or X–2**.  
  - Example: A Grade 5 skill can depend on Grade 3, 4, or 5 skills, but **not** on Grade 2 or Grade 6+ skills.  
- Dependency graph must be:
  - **Acyclic** (no cycles)  
  - **Pedagogically meaningful** (only true prerequisites)  
  - **Minimal** (no unnecessary edges)

From the spec:
- Certain skills (e.g., `T06.G3.01` Events, `T07.G3.01` Loops, `T08.G3.01` Conditionals, `T09.G3.01` Variables, `T13.G3.01` Debugging) are **gateway skills** with many dependents.  
- Grade 3 is the **critical transition year** where coding begins and dependencies spike.

When making changes in `skillsv5/allskills.md`:
- Maintain or improve adherence to the X–2 rule.  
- Prefer **adding missing dependencies** over deleting existing ones unless clearly wrong.  
- Preserve cross-topic dependencies unless the run explicitly says you are working on them.

---

## 5. How to Get Oriented Quickly (Human or LLM)

If you want a **fast but solid understanding** before editing:

1. **Read `spec_v2_updated.md` sections 0–5**  
   - Purpose, objectives, domains, topics, K–2 framework, dependency model, gateway skills, learning pathways.  
   - Treat numbers (1,119 skills, 4,167 dependencies) as describing the **original v2 concept-level map**.

2. **Skim `docs/domains_topics_overview.md`**  
   - Focus on T01–T34.  
   - Note that T35–T36 are present but not part of the current v5 optimization loop.

3. **Review `creaticode.md`**  
   - Understand available blocks and features so that skill descriptions and examples are realistic and aligned with the platform.

4. **Open `skillsv5/allskills.md`**  
   - Search for a topic header like `# T09 - Variables & Expressions`.  
   - Inspect a few skills in K, 3, and 5 to see how descriptions, dependencies, and micro-steps are currently structured.

---

## 6. Relationship Between Specs and skillsv5

- `spec_v2_updated.md` is the **design contract**:
  - Domains and topic purposes  
  - K–2 picture-based model  
  - Dependency philosophy and X–2 rule  
  - AI4K12 and CSTA alignment  
  - Gateway skills and learning pathways

- `skillsv5/allskills.md` is the **live implementation**:
  - More granular micro-skills (≈2,900+ IDs)  
  - Per-topic optimization notes in comments at the top of each topic section  
  - In-progress improvements from recent optimization runs

When you find tension between them:
- Follow the **spirit and constraints** in `spec_v2_updated.md`,  
- But treat `skillsv5/allskills.md` as the **source of truth** for what currently exists and what needs to be edited.

---

## 7. For Automation: runonebyone.js Assumptions

Scripts like `runonebyone.js` orchestrate **repeated, autonomous refinement passes** over the skill map.

They assume:

- **Input / output file:**  
  - All changes are made directly to `skillsv5/allskills.md`.  
  - The script makes backups like `skillsv5/allskills_topic_phase_iter*.md` and `allskills_grade_phase_iter*.md` before each major phase.

- **Topics:**  
  - Only topics `T01`–`T34` are processed.  
  - Topic names and order are defined inside `runonebyone.js`.

- **Two-phase optimization loop:**
  1. **Phase 1 – Topic passes**  
     - For each topic, across all grades:  
       - Improve internal coherence and progression.  
       - Split overly broad skills into micro-steps.  
       - Remove duplicates within the topic.  
       - Fix **intra-topic dependencies only** (no cross-topic changes).
  2. **Phase 2 – Grade+Topic passes**  
     - For each grade+topic combination with skills:  
       - Add and clean up **cross-topic dependencies** while respecting the X–2 rule.  
       - Preserve intra-topic structure and focus on dependency correctness.

- **Editing rules (shared across phases):**
  - **Do not delete skills** unless absolutely necessary.  
  - **Do not modify skills from other topics** when a prompt says to stay within one topic.  
  - **Do not break dependencies** for other topics or grades.  
  - Prefer **rewriting, splitting, merging, and re-linking** skills within the allowed scope.

If you are designing new automation or prompts, keep these assumptions and constraints aligned so that all tools operate on a consistent mental model of the skill map.

---

**Status (this file):** Updated for the v5 skill map and current `runonebyone.js` workflow.  
Use this as the human/LLM orientation entry point for any new refinement passes.

