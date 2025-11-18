# Designing Topics in an IXL‑Style Microstep Format

This guide summarizes the key principles we used to take T01 from a coarse v1 spec (≈4 broad skills per grade) to a highly granular v6 spec (many tiny skills, uneven by grade). You can apply the same ideas when redesigning any topic (T02–T36).

The goal is to make each topic feel like **IXL for that concept**: lots of small, focused skills with no big jumps.

---

## 1. Overall Philosophy

- **Microsteps, not bundles:**  
  Each skill should represent one tiny, well‑defined idea. Avoid skills that combine multiple constructs, representations, or practices.

- **Short, finishable tasks:**  
  Design skills so an average student can complete one in a short sitting. This encourages flow and reduces frustration.

- **Progressive refinement:**  
  Within a strand, move from easier to harder in very small increments, so students rarely feel “thrown into the deep end.”

---

## 2. Uneven Distribution Across Grades

- **Do not force symmetry** (e.g., 4 skills per grade).  
  Instead, match density to where the cognitive load and novelty actually are for that topic.

- Typical pattern (adapt as needed per topic):
  - **K–2:** Fewer, concrete skills; primarily conceptual and picture‑based.
  - **3–5:** Heaviest density; many microsteps because formal representations and more abstract reasoning tend to begin here.
  - **6–8:** Focused, higher‑order skills (analysis, tradeoffs, impacts, refinement), but still in small steps.

---

## 3. Use Strands Within Each Grade

Rather than one flat list per grade, organize skills into **strands** that reflect different aspects of the topic. For example, you might have strands like:

- “Recognize & understand”  
- “Apply or build”  
- “Trace or read”  
- “Debug or fix”  
- “Compare or choose”  
- “Extend or explain”

Within each strand, create 3–5 skills that move from easiest to harder in small increments. This makes it clear how students progress within a grade and makes dependency design simpler.

---

## 4. Cover Multiple Roles for Each Idea

For each key idea in a topic, aim to create separate skills for different **roles** students play:

- **Concept‑only:** Understand the idea informally (often with visuals or stories).
- **Read/trace:** Understand what an existing artifact (diagram, table, code, etc.) does.
- **Write/build:** Create an artifact from a plan or template.
- **Refactor/improve:** Make an existing artifact shorter, clearer, more structured, or more efficient.
- **Debug/fix:** Find and correct one specific kind of mistake.
- **Compare/choose:** Decide which of several options is better or more appropriate, and why.

Instead of one big skill that says “understand and write and debug,” make each role its own microstep.

---

## 5. K–2 Principles (Picture‑Based Microsteps)

For K–2 topics, follow these general patterns:

- Prefer **picture‑based interactions** (drag‑drop, click, path tracing) with minimal text; always support audio for instructions.
- Build short ladders of 4–8 skills per big idea:
  - Recognize or identify (e.g., spot something in a picture).
  - Order or group (e.g., put pictures in sequence or categories).
  - Fix one thing (e.g., repair a mixed‑up story).
  - Compare (e.g., choose which option “makes sense”).
- Keep each skill cognitively and motor‑wise simple:
  - Limit items on screen.
  - Avoid multi‑step gestures or text entry.

The aim is to build robust conceptual foundations without introducing formal notation or heavy reading.

**K–2 across all topics must also remain device‑agnostic and non‑coding:**

- Avoid **coding‑specific vocabulary or editor UI references** in K–2 skill text (e.g., no “blocks,” “scripts,” “code,” “green flag,” “start button,” “variables,” etc.).  
- Describe everything using everyday language (steps, instructions, stories, games, jobs, helpers) so that tasks can be completed with paper cards or manipulatives, even if they are ultimately implemented as digital, picture‑based activities.  
- Reserve explicit programming constructs and environment‑specific terms for **Grade 3 and above**, where topics like T06–T13 begin introducing block‑based coding.

---

## 6. 3–5 Principles (Highest Density Years)

For many topics, grades 3–5 are where formal representations, structures, and more complex reasoning begin. Reflect that by:

- Adding **more skills per grade** (often 10–14) in these years.
- Breaking each new construct or representation into several microsteps across roles (concept → read → write → debug → compare).
- Ensuring that each skill still has a **single, narrow objective**, even if there are many skills overall.
- Separating:
  - **Planning vs implementation** (e.g., plan in everyday language vs build artifact from plan), and
  - **Simple vs edge cases** (start with typical cases, then add dedicated skills for edge‑case handling).

---

## 7. 6–8 Principles (Higher‑Order but Still Small Steps)

For middle school bands, the emphasis often shifts from “what is this?” to:

- How efficient or scalable is it?
- How fair or ethical is it?
- How can it be tested or improved?

Design skills that:

- Break higher‑order tasks into microsteps:
  - Measure or observe (e.g., count steps, inspect behavior).
  - Compare (e.g., decide which is better and why).
  - Modify (e.g., make a targeted improvement).
  - Justify or explain (e.g., defend a choice or change).
- Avoid giant “analyze everything” skills by splitting:
  - “Spot the issue” vs “propose a fix” into separate skills.
  - “Design tests” vs “run tests and find failures” vs “explain failures.”

---

## 8. Microstep Design Checklist for Any Topic

When taking a topic from a v1‑style spec to an IXL‑style v6 spec:

1. **Start from the global spec and standards.**
   - Skim `spec_v2_updated.md` to understand the topic’s role in the overall map, grade expectations, and any gateway skills.
   - Use `cstastandard.md` for CSTA wording and expectations; keep difficulty aligned to the relevant grade band.
2. **List existing skills per grade** and highlight any that bundle multiple ideas, representations, or roles.
3. **Identify the big ideas** in the topic (conceptual anchors, representations, constructs, or practices).
4. For each big idea and grade:
   - Define 3–4 **strands** (e.g., understand, apply, trace, debug, compare, explain).
   - Within each strand, create a **short progression** of skills (3–5 microsteps).
   - Make sure each strand has a clear internal order: concept → read/trace → write/build → debug/fix → compare/explain (not all roles are required every time, but avoid skipping straight from “never seen it” to “debug it”).
5. **Match density to grade band.**
   - Over‑allocate skills to grades 3–5 where constructs/representations are first formalized.
   - Keep K–2 lighter and picture‑based; keep 6–8 focused on analysis, efficiency, fairness, testing, and refinement.
6. Ensure that **each skill**:
   - Has a single, clear objective and one primary “role” (e.g., *trace* or *debug*, not both).
   - Is implementable on the platform (interaction type + auto‑grading behavior) using CreatiCode blocks and/or HTML environments.
   - Feels like a small, manageable step from its prerequisites (IXL‑style “tiny but meaningful” increments).
   - Keeps any new representation or notation in **trace/compare** tasks first, before asking students to write or debug in that representation.
7. Check the **sequence for jumps**:
   - Between adjacent skills in each strand (no sudden jumps from concept‑only to complex debugging).
   - When moving from one grade to the next for the same idea (Grade N+1 skills should feel like a natural extension of Grade N).
8. Add or adjust **dependencies** so that:
   - Earlier microsteps unlock later ones in the same strand.
   - Cross‑topic prerequisites (if any) align with where constructs are first taught (e.g., loops/variables topics before loop/variable‑heavy algorithm skills).
   - Dependencies never point “forward in time” (no grade N skill depending on grade N+1).
9. Sanity‑check **CSTA alignment and difficulty**:
   - Verify that the mapped CSTA code(s) match what students actually do in the skill (ALG‑AF vs ALG‑PS vs ALG‑IM vs PRO‑PF/TR).
   - Check that cognitive demand matches grade level (K–2 conceptual, 3–5 construct mastery, 6–8 analysis/tradeoffs/refinement).
10. Confirm **platform and auto‑grading details**:
    - For coding tasks, ensure behavior and/or code structure can be reliably auto‑checked.
    - For explanation/fairness/justification tasks, favor structured formats (MCQ, multi‑select, drag‑order, choose‑statements) so scoring is robust; optional free text can be supported via XO/AI but should not be required for core grading.

Using this approach, you can systematically transform any topic into a dense, micro‑stepped skill map that supports IXL‑style mastery and is still fully aligned with CSTA, AI4K12, and the CreatiCode platform.

---

## 9. Platform & Format Considerations

When specifying formats for skills, remember that activities can use:

- The **CreatiCode block‑based editor** (Scratch‑style playground) for most coding challenges, including auto‑graded runtime behavior and structure checks.
- **HTML‑based environments** (e.g., custom widgets, interactive diagrams, or small web UIs) for non‑block interactions, visual explanations, or specialized testers.

Design with these principles in mind:

- Choose the simplest format that matches the skill’s objective (drag‑drop, click, trace, code, flowchart, HTML widget, etc.).
- Make sure the chosen format can be implemented with available CreatiCode/HTML tooling and can be **fully auto‑graded** (or rubric‑graded where explicitly acceptable, such as some flowchart or pseudocode tasks).
- Keep K–2 skills picture‑based with standard interactive patterns; use the CreatiCode playground or HTML primarily from Grade 3 onward for coding and richer simulations.

---

## 10. Cross‑Topic Roles & Grade‑Band Boundaries (T01–T09, T25)

As we refined T01–T05 and T07–T09, a few structural patterns emerged that any future topic redesign should respect.

- **K–2 vs 3–8 division:**
  - Use **D1/D3 topics** (e.g., T01–T05, T25) plus **early organization topics like T12** for **K–2 conceptual foundations**:
    - Everyday sequences, if/then rules, repeating patterns, simple data types, “things that change,” and basic planning notions like “what starts an activity” and “who does which job when.”
    - These should remain picture‑based and non‑coding (drag‑drop, click, match, trace), and should **not** mention editor‑ or language‑specific ideas such as blocks, scripts, variables, or green flags.
  - Use **D2 Programming Core topics** (T06–T09) for **Grade 3–8 coding constructs**:
    - T06 Events & Sequences, T07 Loops, T08 Conditions & Logic, T09 Variables & Expressions.
    - In v3, these start at **Grade 3**, not K–2. Do not add new K–2 skills under T06–T09; anchor early ideas in T01–T05/T12/T25 instead, and when refactoring legacy K–2 skills out of T06–T09 (as we did for early T06 K–2 event skills), **re‑home or merge them into D1/D3/T12** rather than discarding them.

- **Roles of T01–T05 (D1) vs T06–T09 (D2):**
  - **T01 Everyday Algorithms:** Real‑world tasks and project algorithms (mazes, routines, simple games). Focus: *What algorithm solves this?* Notation is incidental.
  - **T02 Algorithm Diagrams:** Representations and tracing (strips, box diagrams, flowcharts, pseudocode, trace tables, code tracing). Focus: *How is this algorithm represented and followed?*
    - For flowcharts/diagrams, use the **CreatiCode Diagrams tab** as the default implementation surface.
  - **T03 Problem Decomposition:** Breaking problems into subtasks, planning features/milestones, and organizing work across grades. Focus: *What are the parts and in what order?* K–2 leans on T01/T02 to see parts and subtasks; 3–5 plans features before coding in T06–T09; 6–8 extends to architecture, milestones, risk/scope, and refactoring plans.
  - **T04 Algorithm Patterns:** Reusable solution shapes (repeats, counter/accumulator/search/filter patterns, bounce‑on‑edge, etc.). Focus: *What pattern is this? Which pattern should we use?*
  - **T05 Human‑Centered Design & Simulation Planning:** Users, accessibility, feedback, and “what to model/measure” in simulations. Focus: *Who are we building for? What should the simulation represent and test?* Acts as a planning bridge into simulation‑coding topics (e.g., T17, T25–T28) rather than a place to introduce new coding constructs.
  - **T06–T09 Programming Core:** Concrete constructs implemented in code:
    - T06: Events & sequences in scripts.
    - T07: Loops (G3–8 only).
    - T08: Conditions & logic (G3–8 only).
    - T09: Variables & expressions (G3–8 only).
    - These topics **assume** K–2 conceptual work from T01–T05/T25 and should not re‑teach it at K–2.

- **Pattern‑first, then coding for big constructs (loops/conditions/variables):**
  - **Concept & pattern stage (K–2, early 3):**
    - Repetition, “do it again,” and repeat‑units live in **T01/T04**.
    - Everyday if/then and simple choices live in **T01/T05**, with patterns like “bounce on edge” introduced in **T04**.
    - “Things that change,” counting, and more/less/same live in **T01/T04/T25**.
  - **Coding stage (G3+ in T06–T09):**
    - T07/T08/T09 then introduce the **blocks** (repeat/forever, if/else, variables & expressions) and apply the patterns in real CreatiCode projects.
  - When designing microsteps:
    - Put **early conceptual/pattern microsteps** in T01–T05/T25.
    - Put **first code‑level microsteps** in T06–T09 (starting at G3).
    - Avoid duplicating concept‑only work inside T06–T09; instead, depend on T01/T04/T25 skills.

- **T02 + Diagrams tab (representations):**
  - T02 should be the primary home for:
    - **Algorithm strips/box diagrams** (K–2).
    - **Flowcharts and decision diagrams** (G3–8), implemented in the **Diagrams tab**.
    - **Pseudocode ↔ flowchart ↔ code conversions** and trace tables.
  - Other topics may *use* diagrams (e.g., T01/T03/T05), but should:
    - Treat T02 as the place where students learn the notation mechanics.
    - Depend on T02 microsteps rather than re‑teaching flowchart syntax or trace‑table skills.

- **T25 vs T09 (data meaning vs coding construct):**
  - **T25 Data Representation:** Focus on what the data *means* and how it’s shaped:
    - Numbers vs categories vs text; simple tables and records; precision and granularity.
    - Local vs shared/cloud‑backed variables and table variables as data structures.
  - **T09 Variables & Expressions:** Focus on using variables/expressions in **code**:
    - Patterns for initialization, update, counters, timers, aggregate calculations, and formulas.
  - When adding variable‑related skills:
    - Put “what type of data is this?” and “how is it stored/encoded?” in **T25**.
    - Put “how do we use this variable/expression in code?” in **T09** (G3+).

  - **Dependency design across topics:**
	  - For Grade 3 entry skills in T06–T09, assume completion of relevant K–2 skills in:
	    - T01–T04 (sequences, patterns, if/then), T02 (simple diagrams), T25 (basic data types, counting/comparison).
	  - Encode this by:
	    - Pointing Grade 3 coding microsteps in T06–T09 to earlier T01–T05/T25 microsteps instead of adding duplicate K–2 coding skills.
	    - Using clear notes in each topic file (as we did for T01–T05 and T07–T09) so future editors know where to put new skills.

---

## 11. Status & Next‑Step Checklist (as of latest T01–T05, T07–T09, T25 pass)

This section captures the current state of the redesign work and what a future editor should do next.

- **Current progress & structural decisions**
  - T01–T05 and T25 have been reviewed so their roles are clearly separated:
    - T01: everyday/project algorithms; T02: representations & tracing; T03: planning & decomposition; T04: reusable patterns; T05: human‑centered design & simulation planning; T25: data meaning & structure.
  - T02 is the primary home for algorithm representations/tracing (strips, diagrams, flowcharts, pseudocode, trace tables) and explicitly uses the CreatiCode **Diagrams** tab for flowchart/diagram tasks.
  - T07/T08/T09 are now **Grade 3–8 only**, focused on block‑coding constructs (loops, conditions/logic, variables/expressions). All K–2 conceptual work for those ideas lives in T01–T05/T25.
  - T01 and T04 are aligned so that K–2 and early Grade 3 focus on pattern‑first thinking (repetition, if/then, things that change) before students see the corresponding blocks in T06–T09.

- **Platform & interaction assumptions**
  - K–2 skills stay picture‑based with simple interactions; coding starts in Grade 3 using the CreatiCode block editor.
  - Diagram‑centric skills (especially in T02, but also when other topics need flowcharts/box diagrams) should use the CreatiCode **Diagrams** tab rather than ad‑hoc HTML tools.

- **Next steps for future topic work**
  - For remaining topics (starting with T06 and T10+):
    - Decide whether the topic should be K–2 + 3–8, or 3–8 only (like T07–T09) and move any pure K–2 conceptual work into T01–T05/T25 where appropriate.
    - Apply the IXL microstep rules from Sections 1–9 and the cross‑topic role rules from Section 10.
    - Ensure each topic intro clearly states its scope (which grades) and its role relative to T01–T05/T25 and T06–T09.
  - Update JSON dependency maps (e.g., in `archive/analysis/dependencies_*.json` or any current dependency files) to reflect:
    - T07–T09 starting at Grade 3.
    - T02 as the representation/diagram prerequisite.
    - T04 as the pattern prerequisite for loops/conditions/variables.
    - T25 as the data‑meaning prerequisite for T09/T10/T26.
  - Run a consistency pass over high‑level docs (e.g., `docs/domains_topics_overview.md`, `docs/topic_grade_matrix.md`, `docs/QUICK_REFERENCE.md`) so they:
    - No longer show K–2 content for T07–T09.
    - Match the clarified roles of T01–T05/T25 vs T06–T09.
