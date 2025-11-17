# Skill Dependency & Grade Alignment Workflow (Draft)

This document describes how to design, relate, and grade‑place CreatiCode K–8 skills so that:

- dependencies between skills are explicit and acyclic, and  
- every skill’s prerequisites appear at the **same or earlier grade**.

The process separates **“what skills exist”** from **“when they are taught”**, and uses a graph‑based pass to enforce consistency.

---

## Step 1 – Design Skills by Topic (Band‑First, Not Grade‑First)

For each topic (e.g., `T07 Loops & Repetition`):

- Draft a **ladder of skills** from first exposure to advanced middle‑school use.
- For each skill, record at least:
  - a stable **ID** (e.g., `T07.G?.01` while grade is undecided),
  - a short **name** (IXL style),
  - a **description** and typical **challenge format**,
  - one or more **CSTA codes**,
  - a broad **grade band hint**: `K–2`, `3–5`, or `6–8` based on CSTA expectations and cognitive demand.
- **Do not** fix the exact grade yet. Focus on content coherence within the topic.

Result: each topic has a rich, internally ordered list of skills roughly grouped into bands, but grade assignments are still flexible.

---

## Step 2 – Add Explicit Prerequisites (Build the Dependency Graph)

Treat each skill as a node in a graph and make dependencies explicit:

- For every skill, list **prerequisite skills** by ID:
  - within the same topic (e.g., basic loop use before nested loops),
  - across topics (e.g., loops and variables before list iteration).
- Distinguish:
  - **required prereqs** (must be mastered first),
  - optional or **recommended prereqs** (helpful but not strictly required).

This gives a directed graph:  
`prereq_skill → dependent_skill`.

Constraint: the graph should be **acyclic** (no cycles). If a cycle appears, split or reorder skills until it disappears.

---

## Step 3 – Assign Grade Bands, Then Individual Grades

Use CSTA as the baseline:

- Start by mapping each skill to a **grade band**:
  - If it primarily serves EK/E1/E2 standards → band `K–2`.
  - If it primarily serves E3–E5 → band `3–5`.
  - If it primarily serves MS → band `6–8`.

Then assign **specific grades** within each band:

- For skills in `K–2`, decide whether they best fit K, 1, or 2; similarly split `3–5` into 3/4/5 and `6–8` into 6/7/8.
- Use these heuristics:
  - earlier grades in a band get **foundational prereqs**,
  - later grades get **more abstract or multi‑concept skills**,
  - balance the number of “new big ideas” per grade so no single year is overloaded.

At this stage, every skill has a draft `grade` field but dependency consistency has not yet been enforced.

---

## Step 4 – Run a “Prereq Linter” to Check Grade Constraints

Treat the skills and prerequisites as data (e.g., JSON) and run a simple check:

For each skill `S` with grade `g`:

- For every **required** prereq `P`:
  - If `grade(P) > grade(S)`, flag a **dependency violation**:
    - this means students are expected to know `P` only after they encounter `S`.

The linter should also:

- detect **cycles** (if any still exist), and  
- optionally flag unrealistic grade jumps where a skill’s cognitive demand is far above a typical grade‑level expectation, even if dependencies are formally satisfied.

The output is a list of skills and dependencies that break grade ordering.

---

## Step 5 – Fix Violations by Adjusting Grades and/or Skills

For each violation (a skill depends on something at a higher grade), choose one or more of these fixes:

1. **Move the dependent skill up**  
   - If its content is still age‑appropriate one grade higher, assign it to a higher grade.

2. **Move the prerequisite down**  
   - If the prereq is simple enough to introduce earlier, lower its grade.

3. **Split the skill into two**  
   - Create an easier “precursor” skill at an earlier grade and keep the original, more advanced version at a later grade.
   - Adjust dependencies so the later skill depends on the precursor.

4. **Relax the dependency**  
   - If the dependency was “nice to have” rather than essential, mark it as **recommended** instead of required so it no longer blocks grade placement.

After each adjustment, rerun the linter until no required prereq has a higher grade than its dependents and the graph remains acyclic.

---

## Step 6 – Handle Cross‑Topic Dependencies Explicitly

Some skills naturally span topics (e.g., list iteration uses loops, variables, and lists). For these:

- Put the skill in the **most natural topic** (e.g., list iteration in the Lists/Data topic).
- Add **cross‑topic prereqs**:
  - e.g., a list‑iteration skill in `T10` depends on loop‑reading skills in `T07` and variable basics in `T09`.
- Ensure these prereqs live in:
  - the **same grade** or  
  - an **earlier grade**.

The dependency graph and linter treat cross‑topic and within‑topic dependencies the same way.

---

## Step 7 – Iterate: Topic‑Local Then Global Refinement

Use an iterative approach:

1. **Topic‑local design**  
   - For each topic, refine its internal skill ladder and prereqs until it’s coherent on its own.

2. **Global dependency/grade sweep**  
   - Run the prereq linter across all topics.
   - Fix grade violations and cycles, possibly adjusting multiple topics.

3. **Repeat once or twice**  
   - Continue until:
     - no dependency violations remain,
     - grades per topic feel balanced and age‑appropriate,
     - cross‑topic skill chains (e.g., from basic loops → list iteration → data analysis) form smooth progressions.

---

## Step 8 – Lock the “Golden” Skill Map and Expose Dependencies

Once the dependency graph and grade assignments are stable:

- Freeze a **versioned snapshot** of the skill catalog (e.g., `skills_v1.json`) including:
  - skill IDs, topics, grades, bands,
  - descriptions and challenge formats,
  - CSTA mappings,
  - required and recommended prereqs.
- Expose dependencies in teacher tools:
  - show “prerequisite skills” and “next skills” for each skill,
  - allow auto‑suggested assignments that respect the dependency graph.

This versioned, dependency‑checked map becomes the “golden standard” used by all students and teachers, with future updates going through the same workflow.

