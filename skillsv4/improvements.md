# CreatiCode K–8 Skill Map v4 – Improvement Plan (IXL-Style)

This document summarizes concrete ways to strengthen the `skillsv4` set so it feels like “IXL for coding on CreatiCode,” aligned with the v2 spec, CSTA draft, and AI4K12 priorities.

---

## 1. Global Design Improvements

- **[G1] Restore explicit Kindergarten coverage and ID consistency**
  - Current `skillsv4/allskills.md` IDs start at `G1`; there are no `K`/`G0` skill IDs even though the spec describes K–2 coverage.
  - Action:
    - Decide the canonical naming for Kindergarten (e.g., `GK` or `G0`) and ensure **every topic that claims K coverage** in the spec has corresponding K-grade skills.
    - Either (a) surface existing K skills into `allskills.md` with consistent IDs or (b) backfill missing K skills by downshifting the easiest G1 conceptual microsteps where appropriate.

- **[G2] Enforce the “no coding in K–2” rule**
  - K–2 skills in the sampled topics generally avoid blocks, but we should make this a hard constraint.
  - Action:
    - Audit all `G1`/`G2` skills in `allskills.md` for words like `block`, `script`, `code`, `green flag`, `ChatGPT`, `XO`, `variable`, or specific CreatiCode UI names.
    - For any K–2 skill that slips into environment-specific language, rewrite the `Skill` and `Description` to use everyday terms (steps, choices, stories, helpers, machines) so the activity can be run unplugged or with generic manipulatives.

- **[G3] Separate student-facing wording from editor notes**
  - Many `Description:` entries mix student-friendly behavior with editor-facing notes and cross-topic references (e.g., “building on T04.G2.x …”).
  - Action:
    - Introduce a distinct “Notes” or “Editor notes” field in the source data (even if it is not yet visible in `allskills.md`) and move:
      - Cross-topic references (e.g., “bridging to T04.G1–G3”),
      - Implementation hints (“use CreatiCode table blocks…”),
      - CSTA/AI4K12 tags.
    - Keep `Skill:` as a short IXL-style learning objective and `Description:` as a one-paragraph, student-centered description (what the learner does and understands), without internal IDs.

- **[G4] Standardize microstep strands and ordering within each grade**
  - The best-designed topics (T01, T02, T05, T06, T25–T27) implicitly follow strands like “recognize → trace → build → debug → compare/explain,” but this is not fully consistent across all topics.
  - Action:
    - For each topic and grade, reorder skills so they follow a consistent pattern:
      1. Concept/recognize (informal, often picture-based),
      2. Read/trace an existing artifact,
      3. Build/write a small artifact,
      4. Debug/fix a single type of mistake,
      5. Compare/choose/explain.
    - Where a skill currently mixes roles (e.g., “understand and write and debug”), split it into multiple microsteps.

- **[G5] Rebalance Grade 3 cognitive load**
  - Grade 3 is the gateway year; currently multiple topics introduce several constructs at once (events, loops, conditionals, variables, lists, sometimes data tools).
  - Action:
    - For each core programming topic (T06–T10, T13), label each G3 skill as **“first exposure” vs “extension”** and ensure:
      - Per construct, there is at least one **pure read/trace** microstep before a “build from scratch” task.
      - The total number of simultaneously new constructs per G3 student is limited (events + one or two constructs at a time), pushing more advanced variants into G4–G5.
    - Where needed, move the most complex G3 skills down to G4 (see concrete proposals under T08/T09/T10).

- **[G6] Make AI4K12 coverage explicit and trackable at the skill level**
  - AI-related skills clearly touch AI4K12 categories, but this metadata is currently in narrative text rather than as structured tags in `allskills.md`.
  - Action:
    - Add `ai4k12_category` and `ai4k12_subtopic` metadata (from the spec JSON model) to the underlying data for every AI-relevant skill (T21–T24, portions of T25–T29, T35–T36).
    - Run a coverage check to verify that “Perception” and “Agents & Environments” subtopics are still thin and prioritize backfill (see T23/T28 suggestions).

---

## 2. Algorithms & Design (T01–T05)

- **[A1] Make recursion in T01 explicitly “concept-only”**
  - T01.G8.04–G8.05 introduce base/recursive steps and tracing recursive algorithms.
  - Action:
    - Confirm these are framed in conceptual, diagram, or natural-language form (no Scratch-style recursive blocks at G8).
    - If any code-level recursion slips into T01, move it into a high-school extension or clearly mark it as “conceptual only” with small, bounded examples.

- **[A2] Tighten division of labor between T01 and T02**
  - T01 uses flowcharts and pseudocode as tools; T02 is the “representations” home per the guide.
  - Action:
    - For T01 skills that explicitly *teach* diagram notation (symbols, arrow conventions, trace tables), move that instruction into T02 and turn the T01 skill into “apply diagrams to everyday/project algorithms,” with a dependency on the corresponding T02 microstep.
    - Example: keep `T01.G5.01–G5.03` but rewrite descriptions to assume students already know flowchart/pseudocode syntax from T02; focus them on **matching representations to tasks** rather than learning diagram grammar.

- **[A3] Align simulation planning in T03/T05 with downstream topics**
  - Simulation-related HCD microsteps in T05 (e.g., G2.03–G2.04, G3.04–G3.05, G5.04–G5.06, G8.03–G8.04) set up later physics/data/AI simulations.
  - Action:
    - Ensure each major simulation-heavy topic (T17 physics, T18 3D, T28 chance, AI modeling skills in T23/T28–T29) explicitly depends on the relevant T05 planning microsteps instead of re-teaching “what to model” and “what to measure.”
    - Where later topics still include planning text in their descriptions, factor that out into shared HCD skills and simplify the downstream skills to “implement the planned model in code.”

---

## 3. Programming Core (T06–T13)

- **[P1] Events (T06) – add 1–2 bridge microsteps at G3**
  - T06.G3 already has a good mix of “build” and “trace,” but G3 students hit multi-script reasoning quickly.
  - Action:
    - Add a **pure code-reading** microstep before T06.G3.04, e.g., “T06.G3.xx – Match scenarios to events” where students decide which script runs given a description, without editing code.
    - Add a **mis-trigger debugging** microstep that focuses only on swapping event types (`when green flag` vs `when key pressed`) from a menu, before asking learners to create longer scripts.

- **[P2] Loops (T07) – smooth introduction of loop types**
  - Grade 3 currently introduces `repeat until`, `forever`, and fixed-count `repeat` loops in a single year.
  - Action:
    - Reorder G3 microsteps as: (1) fixed-count `repeat`, (2) trace `repeat`, (3) add `forever` for controls, (4) finally introduce `repeat until`.
    - Consider moving the **most complex game-loop behavior** (current T07.G3.02) to Grade 4 and replacing it at G3 with a simpler “trace a forever loop for continuous behavior” microstep.
    - Add at least one dedicated **debugging microstep** at G3 for off-by-one loop counts or misplaced loop bodies, instead of only refactor-style tasks.

- **[P3] Conditionals & Logic (T08) – delay heavy compound logic**
  - T08.G3.02–G3.03 already require students to build AND/OR expressions in code; T08.G3.04 traces if/else with compound conditions.
  - Action:
    - Redesign G3 to focus on:
      - T08.G3.01: single `if` (keep).
      - New G3 skill(s): **recognize scenarios needing AND/OR** and **choose among given conditional blocks**, without constructing multi-part expressions from scratch.
    - Move explicit **AND/OR coding** (current T08.G3.02–G3.03) into Grade 4 and treat them as refinements after students are solid on single conditions.
    - Ensure G4 includes both **refactor** and **trace** microsteps for nested/compound conditionals before students are expected to design multi-condition logic in projects.

- **[P4] Variables & Expressions (T09) – lighten Grade 3, deepen Grade 4–5**
  - G3 currently includes both simple counters and multi-operator expressions.
  - Action:
    - Restrict Grade 3 to:
      - T09.G3.01 (basic numeric variable for score/count),
      - T09.G3.02 (variable in simple comparison),
      - T09.G3.05 (trace variable changes).
    - Move **T09.G3.03–G3.04 (multiplication/division and multi-step expressions)** to Grade 4, aligning with math progression and reducing G3 overload.
    - Add a **G3 debugging microstep** (“fix uninitialized or never-updated variable”) so gateway skill T09.G3.01 has read/trace/debug coverage, not just “build from scratch.”

- **[P5] Lists & Tables (T10) – ensure K–2 foundations live in T25**
  - The spec says conceptual list/table ideas belong in T25 for K–2, with T10 focusing on coding constructs G3–G8.
  - Action:
    - Audit T10.G3 skills: confirm they depend on T25.G1–G2 (tallies, picture tables, basic tables) rather than re-teaching representations.
    - For any K–2-like skills still in T10 (if present), move them to T25 and reframe T10 G3 skills as “how to use lists/tables in code” (e.g., add/iterate/filter).

- **[P6] Functions & Procedures (T11) – add clearer ladder from “reuse” to “abstraction”**
  - Functions are often under-specified; v1 draft likely has broad, multi-part skills.
  - Action:
    - Introduce a consistent ladder across grades 3–8:
      - G3: Recognize and call pre-made helper blocks; trace what they do.
      - G4–5: Define simple parameterless helpers; then add 1–2 parameter blocks and trace parameter passing.
      - G6–8: Refactor duplicate code into helpers; design and document APIs; reason about contracts.
    - Split any broad skill that combines defining, calling, and debugging functions into smaller microsteps aligned with this ladder.

- **[P7] Program Organization & Testing (T12–T13) – emphasize debugging/test microsteps earlier**
  - T13 testing and T12 organization should support gateway topics (events/loops/vars/conditions) rather than appear only as advanced skills.
  - Action:
    - Ensure Grade 3–4 in T12–T13 include:
      - Reading/understanding simple test cases or check scripts.
      - Adding a single additional test for a known edge case.
      - Reordering scripts or grouping blocks into labeled sections.
    - Cross-link high-leverage debugging skills (like T01.G3.13–G3.15, T06/T07/T08/T09 debugging microsteps) to T13 rather than duplicating debugging descriptions in each topic.

---

## 4. Applications & AI Topics (T14–T24)

- **[APP1] Games/Stories/UI/Physics/3D (T14–T20) – separate “engine skills” from “creative goals”**
  - Some application skills implicitly bundle both engine mechanics (physics, camera, multiplayer) and creative outcomes (story, art direction).
  - Action:
    - For each application topic, carve out **engine-centric microsteps** (e.g., “configure gravity and collision correctly”) separate from **creative microsteps** (e.g., “choose camera angles to tell a story”).
    - This makes dependencies clearer (engine skills can serve multiple pathways) and keeps IXL-style tasks more focused.

- **[AI1] AI Media (T21) & Chatbots (T22) – introduce earlier “concept-only” AI skills**
  - T21 and T22 currently start at Grade 6 with fairly advanced workflows (prompt templating, RAG, multi-agent).
  - Action:
    - Add **Grade 3–5 concept-only AI skills** in either T21/T22 or in D5 topics that:
      - Show AI as “a helper that follows instructions but can make mistakes,” using pre-built CreatiCode projects.
      - Have students **classify AI vs non-AI behavior**, or choose good vs bad prompts, without touching API parameters.
    - Mark these early AI skills with AI4K12 category tags (A: Humans & AI; C: Machine Learning) and keep them unplugged or picture-based for G3 where possible.

- **[AI2] Perception (T23) – backfill K–5 sensing and perception skills**
  - The spec highlights new K–2 sensing ideas (eyes→camera, ears→microphone), but `allskills.md` currently has only G6–G8 T23 skills.
  - Action:
    - Add K–2 and 3–5 T23 skills such as:
      - G1–2: Identify sensors on everyday devices (camera, microphone, touch) and match them to human senses.
      - G3–4: Explain how a camera image is turned into pixels; how a microphone signal becomes “sound data.”
      - G5: Compare “what a human sees/hears” vs “what an AI model receives,” emphasizing limits and errors.
    - Keep all K–2 skills picture-based and non-technical, and all G3–5 skills conceptual or code-reading rather than sensor-block heavy.

- **[AI3] XO & AI Practices (T24) – add guardrail microsteps earlier**
  - T24 G5–G8 cover XO workflows strongly; some guardrail and ethics skills appear only at higher grades.
  - Action:
    - Add G5–G6 microsteps where students:
      - Practice **rejecting XO suggestions** that conflict with rubric/specs.
      - Label prompts as “good” vs “risky” (e.g., sharing private info, copying whole solutions).
    - Ensure each T24 grade has at least one **explicit AI4K12 Category D/E** skill (ethical system design, societal impacts) so XO use is always framed with human oversight.

---

## 5. Data & Analysis Topics (T25–T29)

- **[D1] Data Representation (T25) – enforce its role as the “data meaning” home**
  - T25 is already strong; the main risk is other topics re-teaching its content.
  - Action:
    - For any skill in T09, T27, T28, or T29 that includes schema design, units, encoding/normalization, or JSON-like structures, ensure T25 has the primary “teach” microstep and other topics reference it as a dependency.
    - Example: keep `T25.G6.03` (nest structures) as the canonical place to introduce nested records; downstream topics should say “use nested records as in T25.G6.03” rather than re-explaining.

- **[D2] Data Analysis & Storytelling (T27) – decouple math load from coding load**
  - Many T27 skills require both statistical reasoning and CreatiCode coding.
  - Action:
    - For each grade 3–8 microstep, tag whether the primary novelty is **math/stats** or **coding/UI** and try to avoid introducing both at once in a single skill.
    - Where necessary, split skills like “build interactive dashboards with widgets” into:
      - One skill: build the widget-driven dashboard (coding focus),
      - A separate skill: interpret and communicate findings with that dashboard (analysis/storytelling focus).

- **[D3] Chance & Simulations (T28) – fill AI4K12 “agents & environments” gap**
  - T28 already covers chance, Monte Carlo, and tuning; this topic is a natural home to address AI agents & environments.
  - Action:
    - Add explicit microsteps (probably G6–G8) such as:
      - Designing simple agent rules in a grid world (agent, environment, reward/goal).
      - Tracing how agents learn or adapt over simulated episodes (conceptual, no formal RL math).
      - Discussing how environment design can bias agent behavior (AI4K12 “Agents & Environments”).
    - Ensure at least one skill explicitly tags AI4K12 “Machine Learning: Agents and Environments.”

- **[D4] Text Data & NLP (T29) – strengthen K–5 conceptual ramp**
  - T29 currently begins at G3 and jumps fairly quickly into tokenization and frequency counting.
  - Action:
    - Add or emphasize G3–4 microsteps that:
      - Treat text as just another data type (stories, chat logs, commands) and practice **sorting and grouping** text manually.
      - Use **purely unplugged or UI-driven** tasks (highlighting words, counting occurrences in printed text) before implementing tokenization and cleaning in code.
    - Delay code-heavy tasks (e.g., “store sentences in lists and access words”) until students have 1–2 pure tracing or UI-only microsteps at the same grade.

---

## 6. Systems & Society (T30–T36)

- **[S1] Hardware & Internet (T30–T31) – foreground AI and data dependencies**
  - T30/T31 skills already mention AI hardware and bandwidth/latency.
  - Action:
    - Add explicit cross-topic dependencies from high-level AI and data skills (T21–T23, T25–T28) to the relevant T30/T31 skills, so students understand that **sensing, models, and data flows depend on devices and networks.**
    - Where T30/T31 skills currently include long narrative explanations, trim the `Skill` line to a crisp objective and leave rationale in descriptions.

- **[S2] Impacts, Ethics & Careers (T34–T36) – integrate AI4K12 categories D & E more systematically**
  - T34–T36 have strong narrative skills about history, impacts, and ethics, but their connections to AI topics are sometimes implicit.
  - Action:
    - For each AI-intensive topic (T21–T24, T25–T29), ensure there is a **paired T35/T36 microstep** that:
      - Uses data or logs from those projects to reason about fairness, bias, access, or environmental impact.
      - References AI4K12 categories D (Ethical AI system design & programming) and E (Societal impacts).
    - Example: Pair T21.G7.03 (audit AI imagery for representation) with a T35/T36 microstep that generalizes those findings into a broader reflection or mini policy.

- **[S3] Younger-grade ethics skills – keep them concrete and story-based**
  - G1–G2 skills in T34–T36 are nicely picture-based, but a few later skills may assume more reading than some students can manage.
  - Action:
    - Revisit G1–G3 ethics/impacts skills and ensure:
      - Any scenarios can be presented as short audio-backed comics or picture sequences.
      - Choices are always small and concrete (e.g., “Which choice is more fair?” with 2–3 options), not abstract essay questions.
    - Move long text-heavy reflections (multi-sentence written explanations) into G4+ where reading and writing expectations align better.

---

## 7. Implementation Notes

- Prioritize **Grade 3 gateway skills** (T06.G3.01, T07.G3.01, T08.G3.01, T09.G3.01, T13.G3.01 and immediate neighbors) for the earliest refinement:
  - Apply [G2], [G4], [G5], [P2], [P3], and [P4] changes there first.
- Use the per-topic files in `skillsv4/skills_Txx_*.md` as the canonical place to edit microsteps; regenerate `skillsv4/allskills.md` from those sources to keep them in sync.
- After changes, run a dependency and AI4K12 coverage pass to confirm:
  - No topic re-teaches concepts that belong in T01–T05/T25.
  - AI4K12 “Perception” and “Agents & Environments” are now covered at least once in the 3–8 band.

