# CreatiCode K–8 Skill Map – Topics & Skills Review

_Last updated by Codex CLI: 2025-11-17_

## 0. Scope and Inputs

- **Primary specs reviewed:** `spec.md` (initial design spec) and `spec_v2_updated.md` (Updated Specification v2.0).
- **Supporting artifacts sampled:** `domains_topics_overview.md`, `domains_topics.yaml`, `SKILL_MAP_FINAL_OVERVIEW.md`, `skills_final_enriched.json`, `competition_paths.md`, and representative topic skill lists (e.g., `skills_T09_variables_expressions.md`).
- **Focus of this review:** Conceptual design and practical implementation of **domains, topics, skills, grade progression, and dependencies**, with emphasis on **issues and concrete improvement suggestions**.

---

## 1. Alignment with the Original Spec (spec.md)

### 1.1 Major Strengths

- **Hierarchy realized as intended:** The implemented map delivers **5 domains, 36 topics, and ~1.1k skills**, which fits the original target of 30–50 topics and a dense K–8 skill catalog.
- **Concrete, auto-gradable skills:** Skills follow the IXL-inspired pattern from `spec.md`: single clear objective, concrete challenge, and auto-grading hooks (even when not fully encoded yet in JSON).
- **CreatiCode-specific capabilities honored:** 3D (T18), physics (T17), multiplayer (T19), widgets/UI (T16), and AI/XO topics (T21–T24) are all present as **first-class topics**, matching the “not generic Scratch” requirement.
- **Explicit dependency graph:** The implemented dependency graph (≈4,200 edges per `SKILL_MAP_FINAL_OVERVIEW.md`) fully delivers on the spec’s call for explicit prerequisites, acyclicity, and grade-respecting dependencies.
- **Competition alignment present:** `competition_paths.md` gives concrete topic/skill recommendations for ACSL, Scratch Olympiad, Chinese contests, and project competitions, matching the “explicit, not implicit” competition alignment goal.

### 1.2 Misalignments and Drift

1. **Kindergarten vs. Grade 1–8 coverage**
   - `spec.md` and `spec_v2_updated.md` describe a **K–8** map with **K–2 picture-based skills**, but `skills_final_enriched.json` currently starts at **Grade 1** (`T01.G1.01`) and contains no grade `K` IDs.
   - `SKILL_MAP_FINAL_OVERVIEW.md` reports **grades 1–8** only.
   - **Impact:** External messaging and the v2 spec over-promise K coverage relative to the current machine-usable catalog.

   **Suggestions**
   - Decide whether Kindergarten is:
     - (a) deferred (1–8 official scope) or
     - (b) still in-scope but not yet implemented.
   - Update `spec_v2_updated.md` and public docs to match reality, or add a clear **“K skills: planned, not yet implemented”** subsection with timelines.
   - If K remains in-scope, reserve ID patterns (e.g., `GK`) and stub entries in the JSON to prevent later schema churn.

2. **CSTA domain mapping at skill level**
   - `spec.md` requires each skill to map to a **domain** and **CSTA code(s)**. In `skills_final_enriched.json`, fields `domain`, `domain_id`, `domain_name`, and `csta_code` are present but typically `null`/`"Unknown"`/empty string for early skills (e.g., `T01.G1.01`–`T01.G2.04`).
   - **Impact:** Downstream reporting (per-domain coverage, CSTA alignment dashboards) cannot be driven solely from the canonical skill JSON.

   **Suggestions**
   - Derive `domain_id` per skill from `topic_id` using `domains_topics.yaml`, and populate `domain`, `domain_name` in a one-time enrichment pass.
   - Back-fill CSTA codes into `csta_code` (and optionally `csta_codes: []`) using the existing mapping work referenced in `FINAL_INTEGRATION_REPORT.md`.
   - Make the enriched file (`skills_final_enriched.json`) the **single source of truth** for domains and CSTA alignment, and update scripts accordingly.

3. **Competition metadata placement**
   - `spec.md`’s example JSON shows a `competitions` field per skill. The current implementation keeps competition mapping primarily in **`competition_paths.md`**, not in the skill JSON.
   - **Impact:** Competition relevance is readable for humans but not queryable at scale from the skill catalog.

   **Suggestions**
   - Either:
     - Add a light-weight `competition_tags: ["ACSL_elem", "Scratch_Olympiad_jr"]` field to skills referenced in `competition_paths.md`, or
     - Maintain a separate machine-readable map (e.g., `skills_competitions.json`) keyed by skill ID, generated from `competition_paths.md`.
   - Clarify in `spec_v2_updated.md` that the authoritative representation of competition alignment is **per-skill metadata or a dedicated mapping file**, not only prose.

---

## 2. Domains and Topics Structure

### 2.1 Observations

- **Domains as in data (`domains_topics.yaml`):**
  - `D1` Algorithms and Design (T01–T05)
  - `D2` Programming (T06–T24, including applications and AI)
  - `D3` Data and Analysis (T25–T29)
  - `D4` Systems and Security (T30–T33)
  - `D5` Computing and Society (T34–T36)
- **Topics (36)** match the structure described in `domains_topics_overview.md` and are well-named, teacher-friendly, and consistently scoped (each supports a K–8 ladder or 1–8 ladder where coding is needed).
- `SKILL_MAP_FINAL_OVERVIEW.md` reports **19 programming topics (T06–T24)** with **649 skills (~56%)**, confirming the centrality of programming and applications.

### 2.2 Inconsistencies and Issues

1. **Spec v2 domain narrative vs. actual domain IDs**
   - `spec_v2_updated.md` (Section 3.1) describes:
     - **D2: Programming Core (T06–T13)** and
     - **D3: Applications & AI (T14–T24)**.
   - In `domains_topics.yaml`, topics **T14–T24** are all assigned to **`D2` Programming**, and **`D3` is Data and Analysis** (T25–T29).
   - `SKILL_MAP_FINAL_OVERVIEW.md` also treats T06–T24 as one large Programming domain.
   - **Impact:** There are effectively **two competing domain models**:
     - A CSTA-aligned 5-domain model (Algorithms, Programming, Data, Systems, Society) implemented in data.
     - A pedagogical “Applications & AI” grouping described as a domain in the v2 text.

   **Suggestions**
   - Treat “Applications & AI (T14–T24)” as a **pedagogical grouping / pathway**, not a new domain:
     - Rename that section in `spec_v2_updated.md` from “Domains (5)” to “Domains & Topic Clusters”, and explicitly flag “Applications & AI” as a **cluster over D2+D5**.
   - Alternatively, if you want a true **third domain** for Applications & AI:
     - Update `domains_topics.yaml` to assign T14–T24 to `D3` with `name: "Applications & AI"`, and add an explicit **CSTA multi-domain mapping** for that domain (Programming + Data + Computing & Society).
   - Whichever option you choose, ensure that:
     - `spec_v2_updated.md`, `domains_topics_overview.md`, `domains_topics.yaml`, and `SKILL_MAP_FINAL_OVERVIEW.md` all use **the same domain definitions and percentages**.

2. **Metric discrepancies for topics/domains**
   - `spec_v2_updated.md` (Section 3.1) reports, for example, **D2: 232 skills (20.7%)** and **D3: 295 skills (26.4%)** under the “Programming Core” / “Applications & AI” framing.
   - `SKILL_MAP_FINAL_OVERVIEW.md` reports **Programming: 649 skills (56.2%)** and **Data & Analysis: 167 skills (14.5%)**, based on the CSTA-aligned domain IDs.
   - **Impact:** Readers cannot easily determine which numbers are authoritative; downstream planning (e.g., how much time to allocate to each domain) may be skewed depending on which table they consult.

   **Suggestions**
   - Choose a **single canonical statistics source** (likely driven directly from `skills_final_enriched.json` and `domains_topics.yaml`) and regenerate:
     - The domain/percent tables in `spec_v2_updated.md`.
     - The metrics in `SKILL_MAP_FINAL_OVERVIEW.md`.
   - Where alternate groupings (e.g., “Programming Core vs. Applications & AI”) are used, represent them explicitly as **derived views** with their own tables, separate from CSTA domains.

3. **Several topics function as cross-domain bridges without being tagged as such**
   - Example: **T20 Algorithmic Art & Creative Coding** naturally bridges Programming, Data & Analysis (visualization), and Computing & Society (expression/ethics), but is stored solely under Programming.
   - Similarly, **T21–T24** (AI topics) and **T35–T36** (impacts, ethics) are central to AI4K12 but only associated with Programming or Society at the domain level.
   - **Impact:** The domain model under-represents cross-domain topics when reporting by CSTA area.

   **Suggestions**
   - Add optional fields at the topic level (e.g., in `domains_topics.yaml` and `domains_topics_overview.md`):
     - `primary_csta_domain` (already implied) and `secondary_csta_domains: []`.
   - Use these for reporting **cross-domain coverage**, especially for AI, ethics, and data-related topics.

### 2.3 Topic-Level Suggestions

These are not blocking issues, but potential refinements:

- **T30 Devices, Hardware, Physical Computing & Software**
  - Consider splitting into:
    - A pure **concept track** (devices, hardware, software) and
    - A **physical computing track** (robots/micro:bit/Arduino) that can be optional depending on hardware availability.
- **T32 Cybersecurity & Safe Online Behavior**
  - If skill counts are high, consider distinguishing:
    - Personal digital safety (passwords, privacy, scams) and
    - Technical security concepts (encryption, authentication, network security) to better align with CSTA subdomains and allow differing depth by grade.
- **T29 Text Data & Introductory NLP**
  - Make its **AI4K12 connections explicit** (especially Representation & Reasoning and Societal Impacts) to avoid it being seen as “just another data topic”.

---

## 3. Skills, Progression, and Dependencies

### 3.1 Observations

- Final metrics from `SKILL_MAP_FINAL_OVERVIEW.md` and `domains_topics.yaml`:
  - **1,155 skills** across **36 topics** and **5 domains**.
  - Skills per topic: **28–40**, with T09 (Variables & Expressions) largest (~40).
  - Skills per grade: **133–149** (Grades 1–8) with **balanced distribution**.
  - Dependencies: **4,220 edges**, average **3.65 dependencies per skill**, zero cycles, and no forward-grade edges.
- **Gateway/hub skills (27)** with 5+ dependents have been identified; both v2 spec and the executive summary emphasize their importance.
- Grade 3 is empirically a **dependency spike** and transition from unplugged to coding.

### 3.2 Issues and Risks

1. **Skill count mismatch between specs**
   - `spec_v2_updated.md` reports **1,119 skills and 4,167 dependencies**, whereas `SKILL_MAP_FINAL_OVERVIEW.md` and `domains_topics.yaml` report **1,155 skills and 4,220 dependencies**.
   - **Impact:** The v2 spec undercounts compared to the final data; external readers may question which numbers to trust.

   **Suggestions**
   - Regenerate and update the numbers in `spec_v2_updated.md` from the current canonical JSON and dependency graph.
   - In the v2 spec, consider adding a short **“Data snapshot”** table that explicitly states the date and data source used for metrics.

2. **High-degree gateway skills create potential bottlenecks**
   - Some gateway skills (e.g., `T09.G3.01` Variables basics) have **very high dependent counts** (197–297 dependents per `spec_v2_updated.md`), making them single points of failure.
   - **Impact:** If a student stalls on one gateway, a very large portion of the map becomes unavailable, and minor misplacement of that gateway can have disproportionate effects.

   **Suggestions**
   - For each gateway with >150 dependents:
     - Review whether **all dependents genuinely require that skill** vs. a looser prerequisite (e.g., any “variables intro” skill).
     - Consider **splitting** the gateway into two or more smaller, more focused skills (e.g., “create and initialize variable” vs. “use variable in expressions”) and distributing dependencies accordingly.
     - Introduce **alternative prerequisite chains** where appropriate (e.g., some media or art skills might only need read-only use of variables, not full variable logic).
   - In the platform, design **targeted remediation experiences** around gateway skills (mini-sequences of 3–5 focused practice skills).

3. **Late-joining students and placement**
   - The dependency system assumes students have progressed from Grade 1 upward in this map. For students entering in Grade 5+ with no prior CreatiCode experience, the current dependency strictness may make large portions of the map appear “locked.”

   **Suggestions**
   - Define a **placement/diagnostic mode**:
     - Allow students to attempt higher-grade “probe” skills; success can auto-mark earlier prerequisites as mastered.
     - Provide teachers with override tools to mark prerequisite mastery based on external evidence.
   - Document in `spec_v2_updated.md` how late entry is intended to work (e.g., uses of diagnostic skills or teacher overrides).

4. **Skill granularity and teacher cognitive load**
   - 1,155 skills is appropriate for auto-grading and adaptive systems, but can be overwhelming for teachers if presented as a flat list.

   **Suggestions**
   - Create **teacher-facing macro-skill bundles** per topic and grade (e.g., “T06.G3 Core Event Handling (4 skills)”).
   - In `topic_grade_matrix.md`, add a column or legend that marks:
     - **Priority skills** (including gateways),
     - **Enrichment skills**, and
     - **Optional/competition-focused skills**.

---

## 4. Early Grades and K–2 / 1–2 Design

### 4.1 Observations

- `spec_v2_updated.md` describes a **two-tier model**:
  - **K–2:** Picture-based, unplugged/light-digital, WCAG 2.1 AA accessible.
  - **3–8:** Block-based coding.
- The spec also enumerates:
  - 10 **K–2 activity types** (drag-drop sequence, sort categories, match pairs, etc.).
  - 11 **visual themes** and clear accessibility requirements.
- Actual JSON (`skills_final_enriched.json`) currently begins at **Grade 1** and records skills mainly as **description + dependencies**, without `activity_type`, `visual_theme`, or `accessibility` fields.

### 4.2 Issues

1. **Picture-based framework not yet encoded in the canonical data**
   - The K–2 (or 1–2) skills are conceptually aligned with picture-based or unplugged activities, but the **activity type, auto-grade rules, and accessibility flags** specified in `spec_v2_updated.md` are not present in `skills_final_enriched.json`.

   **Suggestions**
   - Extend the skill schema (or maintain a parallel file) with:
     - `skill_type` (e.g., `picture_based_digital`, `unplugged`, `coding`),
     - `activity_type` (one of the 10 K–2 types),
     - `visual_theme`,
     - `auto_grade_rules` (type + parameters),
     - `accessibility` flags.
   - Generate these fields at least for K–2 (or Grades 1–2 if Kindergarten is postponed), even if some fields are initially coarse-grained (e.g., default activity type per topic-grade cluster).

2. **Spec language vs. actual Grade 1–2 coding**
   - Some draft topic docs (e.g., `skills_T09_variables_expressions.md`) include **coding activities starting in Grade 1**, which conflicts with the stricter “no coding in K–2” message in v2.
   - While these drafts may predate v2, they are in the repo and can confuse future authors.

   **Suggestions**
   - Either:
     - Update early-grade draft docs to match the **picture-based first** philosophy, or
     - Relax the v2 spec language slightly to allow **very light coding in Grade 2**, while keeping the main K–2 experience picture-based.
   - Clearly document the **intended first full coding grade** (3 vs. 2) and which early-grade skills (if any) may involve block manipulation.

---

## 5. AI Integration and AI4K12 Alignment

### 5.1 Observations

- `spec_v2_updated.md` reports:
  - ~87.5% AI4K12 coverage (14 of 16 subtopics).
  - 33 dedicated AI4K12-aligned skills added across two phases.
  - Clear mapping of AI4K12 categories A–E onto topics **T21–T24** and **T35–T36**.
- Files such as `skills_k8_ai_complete.json`, `ai_skills_new_phase1.json`, and `ai_skills_new_phase2.json` show **explicit `ai4k12_category` metadata** for AI-focused skills.

### 5.2 Issues

1. **AI4K12 metadata not visible in the main skill catalog**
   - AI4K12 fields (`ai4k12_category`, `ai4k12_subtopic`) appear in the AI-focused subsets, but not in `skills_final_enriched.json`.
   - **Impact:** A consumer of the canonical skill file cannot easily compute AI4K12 coverage or filter for AI-related skills.

   **Suggestions**
   - Merge AI metadata into `skills_final_enriched.json` for all relevant skills (not just AI-only files).
   - In the v2 spec, explicitly state which file is the **authoritative AI4K12 mapping** and how it is kept in sync with the main catalog.

2. **Partial coverage for “Perception” and “Agents & Environments”**
   - v2 already flags partially covered subtopics:
     - Machine Learning: Perception
     - Machine Learning: Agents and Environments

   **Suggestions**
   - For **Perception**:
     - Add more skills in **T23** that focus on **interpreting sensor/vision outputs** (e.g., comparing noisy vs. clean signals, limitations of detection).
   - For **Agents & Environments**:
     - Use simple grid-world or game examples in T14/T17/T18 where an AI-controlled sprite behaves as an “agent” with rewards and rules.
     - Tie these skills explicitly to AI4K12’s agent/environment subtopic and annotate them accordingly.

3. **AI topics largely clustered, less woven through core topics**
   - AI appears strongly in **T21–T24** and **T35–T36**. While some other topics naturally intersect with AI (e.g., T25–T29 for data, T01–T05 for algorithms), those intersections are not always explicit.

   **Suggestions**
   - Annotate non-AI topics that **support AI understanding** (e.g., data topics used for training sets, algorithm topics used to design AI behaviors) with AI4K12 categories where appropriate.
   - Create 1–2 **cross-topic mini-pathways** (e.g., “From data tables (T25/T27) to training a simple classifier (T23/T29)”) to demonstrate AI4K12 coherence beyond the “AI topics”.

---

## 6. Competition Alignment

### 6.1 Observations

- `competition_paths.md` gives well-structured mappings from competitions to:
  - Topics and grade bands.
  - Representative skill IDs (e.g., `T07.G4.02`, `T14.G4.01`).
- The pathways align sensibly with the topic architecture:
  - ACSL → Algorithms, loops, conditionals, data.
  - Scratch Olympiad → Games, animation, UI.
  - NOC, Lanqiao → Algorithms, data structures, game dev.
  - Project competitions → Planning, UI, data, ethics, AI.

### 6.2 Issues and Suggestions

1. **Coverage depth not explicit**
   - The competition mappings list **recommended skills** but not whether these cover all relevant skills or just a minimal baseline.

   **Suggestions**
   - For each competition, add brief labels for skills or ranges, e.g., “Core set (must-have)” vs. “Stretch/advanced”.
   - Optionally generate a **competition readiness checklist** per grade that aggregates all referenced skills.

2. **No direct link from skills to competitions**

   - As noted earlier, the flow is **competition → skills**, but not **skill → competitions**.

   **Suggestions**
   - Add a `competition_tags` field per skill (or a lookup map), so teachers can filter skills by relevant competition when planning.

---

## 7. Metadata and Implementation Gaps

Beyond conceptual design, several practical gaps in the current JSON make it harder to operationalize the spec:

1. **Domain/CSTA metadata missing in skills JSON**
   - Covered in Section 1.2 above; high priority if dashboards and reports depend on the JSON.

2. **Lack of fields for activity type, difficulty, and estimated time**
   - v2 spec provides implicit guidance (2–5 minutes for early skills, 10–30 minutes for coding skills) but these are not encoded.

   **Suggestions**
   - Add optional fields:
     - `difficulty` (e.g., 1–5 or “intro/developing/proficient/advanced”),
     - `estimated_minutes`,
     - `is_gateway`, `is_capstone` (already present), and possibly `is_enrichment`.

3. **Potential duplication of “final” skill files**
   - There are multiple skill files (`skills_final.json`, `skills_final_enriched.json`, `skills_k8_ai_complete.json`, etc.), some with overlapping information.

   **Suggestions**
   - Designate a **single canonical file** (likely `skills_final_enriched.json`) and treat others as derived views.
   - Add a short `DATA_README.md` or extend `FILE_MANIFEST.md` to explain the role of each skills file and which fields are guaranteed to be present.

---

## 8. Recommended Next Steps (Prioritized)

1. **Unify domain and metric definitions**
   - Align `spec_v2_updated.md`, `domains_topics.yaml`, `domains_topics_overview.md`, and `SKILL_MAP_FINAL_OVERVIEW.md` on:
     - Domain IDs and names.
     - Topic-to-domain assignments.
     - Skill counts and dependency totals.

2. **Enrich the canonical skills JSON**
   - Populate `domain_id`/`domain_name` and `csta_code(s)` for all skills from existing mappings.
   - Merge AI4K12 metadata into the main skill file for all AI-related skills.
   - Introduce early-grade fields (`skill_type`, `activity_type`, `auto_grade_rules`, `accessibility`) at least for Grades 1–2.

3. **Clarify K vs. Grade 1–8 scope**
   - Decide whether Kindergarten is in scope for the production map:
     - If not, update specs to “Grades 1–8” consistently.
     - If yes, add stub K skills and timelines for completion.

4. **Refine gateway skills and remediation strategy**
   - Audit the highest-degree gateways; split or loosen prerequisites where warranted.
   - Design short remedial micro-pathways around each gateway for adaptive support.

5. **Strengthen AI4K12 coverage in “Perception” and “Agents & Environments”**
   - Add a small number (4–6) of targeted skills in T14/T17/T18/T23 to move from “partial” to “strong” coverage.

6. **Tighten documentation and file-role clarity**
   - Mark `spec.md` as **historical v1** and clearly point new contributors to `spec_v2_updated.md` plus the canonical data files.
   - Add a brief data architecture note linking **spec → topics/skills JSON → reports**.

Taken together, these changes would preserve the strong conceptual design while making the **topics and skills** easier to maintain, analyze, and implement at scale, and would remove confusion between the original spec, the v2 implementation spec, and the actual data in the repo.

