# T26 – Data Collection & Logging: K–8 Skill List (Draft v2)

Topic reference: `T26 Data Collection` in `domains_topics_overview.md`
Domain: Data & Analysis (D3) · CSTA focus: DAA‑DF, DAA‑DP (links to CAS‑ET, PRO‑DH)

Each skill below has:

- a stable **ID** (`T26.G<grade>.<nn>`),
- an IXL-style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** T26 teaches students how to *plan, collect, and organize* data that later flows into representation (T25) and analysis (T27). Grades K–2 stay unplugged/picture-based: noticing data sources, making tallies, and running playful surveys. Grades 3–5 shift into CreatiCode logging (lists, tables, sensors) with emphasis on procedures, fairness, and reproducibility. Grades 6–8 orchestrate larger “data campaigns” including instrumentation, metadata, privacy, and automated pipelines—skills essential for AI topics and UX telemetry (T23 voice/vision, T24 XO logs, T16 widgets). Collection quality determines downstream AI behavior, so AI4K12 priorities (human oversight, bias, transparency) are threaded throughout.

---

## Grade K (PreK–K)

### T26.GK.01 – Notice things you can count or compare

- **Short name:** Find data in the classroom
- **Description:** Students scan a picture of a classroom and point out objects they could count (books, backpacks), building awareness of observable data sources.
- **Challenge format:** Concept, picture hunt. Auto-grading checks highlighted objects and a sentence explaining what to count.
- **CSTA:** EK‑DAA‑DF‑01.

### T26.GK.02 – Use tokens to log repeated events

- **Short name:** Move a bead every time the sprite jumps
- **Description:** Learners watch a simple animation and slide a bead/token each time an event occurs, then count tokens at the end. This is their first “log.”
- **Challenge format:** Interactive. CreatiCode project plays 5–6 events; students tap a counter button to log each one. Auto-grading compares taps to actual events.
- **CSTA:** EK‑DAA‑DF‑01.

### T26.GK.03 – Capture yes/no answers with smile/frown cards

- **Short name:** Two-bin survey
- **Description:** Students ask a peer a yes/no question and place the response card into the correct bin, making a physical tally.
- **Challenge format:** Concept. Learners submit photos or digital recreations; auto-grading checks that both bins are labeled and counts match.
- **CSTA:** EK‑DAA‑DF‑01.

---

## Grade 1

### T26.G1.01 – Run a three-option picture survey

- **Short name:** Ask classmates and mark answers
- **Description:** Students pick a topic (favorite snack) and provide three picture choices. They ask five peers and place stickers on a mini poster to record answers.
- **Challenge format:** Guided survey. Auto-grading expects a photo or digital chart with at least five marks and a short note describing the question.
- **CSTA:** E1‑DAA‑DF‑01.

### T26.G1.02 – Keep observation logs over time

- **Short name:** Morning/afternoon weather chart
- **Description:** Learners observe a daily attribute twice (morning vs afternoon temperature icon) for a week, emphasizing longitudinal collection.
- **Challenge format:** Concept log. Students fill a table with icons; auto-grading checks completeness and a sentence noting a change.
- **CSTA:** E1‑DAA‑DF‑01.

### T26.G1.03 – Follow a simple data-collection checklist

- **Short name:** Steps to ask questions fairly
- **Description:** Students learn to (1) introduce themselves, (2) ask the question the same way, (3) record the answer immediately. They practice on classmates and reflect on why following steps matters.
- **Challenge format:** Concept. Auto-grading checks checklist completion and reflection text referencing fairness/consistency.
- **CSTA:** E1‑DAA‑DF‑01.

---

## Grade 2

### T26.G2.01 – Distinguish observational vs survey data

- **Short name:** Watch vs ask
- **Description:** Students categorize example data statements as “observed” (counting birds) or “asked” (favorite color), reinforcing method selection.
- **Challenge format:** Matching cards with justification. Auto-grading checks answers and reasons.
- **CSTA:** E2‑DAA‑DF‑01.

### T26.G2.02 – Build a two-column record sheet

- **Short name:** Record name + choice
- **Description:** Learners create a simple table to log respondents’ names and answers, showing why we store identifiers alongside data.
- **Challenge format:** Concept. Auto-grading ensures both columns contain data with consistent spelling.
- **CSTA:** E2‑DAA‑DF‑01.

### T26.G2.03 – Use timers to collect duration data

- **Short name:** Time how long the spinner spins
- **Description:** Students run a simple experiment (spin a top) and record each trial’s duration using a timer, highlighting measurement precision.
- **Challenge format:** Concept + analog/digital timer. Auto-grading checks recorded times and that units are consistent.
- **CSTA:** E2‑DAA‑DF‑01.

### T26.G2.04 – Explain why sample size matters

- **Short name:** Compare small vs larger surveys
- **Description:** Learners see two surveys (3 responses vs 10) and explain why the larger one may be more reliable.
- **Challenge format:** Concept explanation. Auto-grading looks for mention of variety or fairness.
- **CSTA:** E2‑DAA‑DF‑01.

---

## Grade 3

### T26.G3.01 – Script a CreatiCode survey loop

- **Short name:** Use `ask and wait` to log answers
- **Description:** Students write a script that repeats `ask` five times, storing each answer in a list variable (linking T26 to T25 representations).
- **Challenge format:** Coding. Auto-grading runs the script with sample answers and checks the list contents.
- **CSTA:** E3‑PRO‑DH‑02.

### T26.G3.02 – Design unbiased multiple-choice options

- **Short name:** Avoid leading answers
- **Description:** Learners critique sample questions (“Don’t you love cats?”) and rewrite them with neutral wording and balanced choices.
- **Challenge format:** Concept editing. Auto-grading ensures rewrites include neutral phrasing and symmetrical options.
- **CSTA:** E3‑DAA‑DF‑01, CAS‑ET.

### T26.G3.03 – Log sensor-style events with counters

- **Short name:** Count button presses automatically
- **Description:** Students build a script where a sprite increments a counter each time a key is pressed, simulating telemetry collection.
- **Challenge format:** Coding. Auto-grading simulates presses and checks the counter variable.
- **CSTA:** E3‑PRO‑PF‑01.

### T26.G3.04 – Separate raw data from summary data

- **Short name:** Keep an untouched log list
- **Description:** Learners maintain two structures: a raw list of answers and a summary list of counts, emphasizing why we never overwrite raw data.
- **Challenge format:** Coding + explanation. Auto-grading checks both lists exist and reflections mention backup/raw data.
- **CSTA:** E3‑DAA‑DF‑01.

---

## Grade 4

### T26.G4.01 – Create collection protocols for partners

- **Short name:** Write survey instructions others can follow
- **Description:** Students draft multi-step protocols (who to ask, how many people, what to say) so teammates can collect consistent data.
- **Challenge format:** Documentation. Auto-grading checks for required fields (audience, script, stopping condition).
- **CSTA:** E4‑PRO‑PM‑05.

### T26.G4.02 – Use tables to log multi-attribute events

- **Short name:** Record timestamp + event type
- **Description:** Learners capture gameplay telemetry in a table with columns (time, event, player). This mirrors logging for CreatiCode games.
- **Challenge format:** Coding. Auto-grading ensures each row has all columns filled and times are increasing.
- **CSTA:** E4‑PRO‑DH‑02.

### T26.G4.03 – Track missing/invalid data with flags

- **Short name:** Mark blank responses as “N/A”
- **Description:** Students add a column to note when data is missing or suspect, preparing them for cleaning in T27.
- **Challenge format:** Concept + coding. Auto-grading checks that invalid entries are labeled and not silently discarded.
- **CSTA:** E4‑DAA‑DF‑01.

### T26.G4.04 – Reflect on privacy in collection

- **Short name:** Decide what to collect and why
- **Description:** Learners evaluate a proposed survey (asking for full names + addresses) and suggest safer alternatives, aligning with AI4K12 ethics.
- **Challenge format:** Concept reflection. Auto-grading expects students to identify sensitive data and propose adjustments.
- **CSTA:** CAS‑ET‑02.

---

## Grade 5

### T26.G5.01 – Instrument a project with runtime logs

- **Short name:** Add logging blocks to key events
- **Description:** Students insert scripts that append event descriptions to a list whenever certain actions occur (level start, damage taken), enabling post-play analysis.
- **Challenge format:** Coding. Auto-grading runs test events and verifies log entries include timestamps or counters.
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DP.

### T26.G5.02 – Plan sampling strategies

- **Short name:** Decide who/when to collect from
- **Description:** Learners compare convenience, random, and stratified sampling for a class poll and document which they’ll use and why.
- **Challenge format:** Concept writing. Auto-grading checks selection along with rationale referencing fairness/bias.
- **CSTA:** E5‑DAA‑DF‑01.

### T26.G5.03 – Validate data entry with error checks

- **Short name:** Use conditionals to reject bad inputs
- **Description:** Students add checks (e.g., reject scores <0 or >100) during collection to ensure data quality upstream.
- **Challenge format:** Coding. Auto-grading submits invalid inputs and ensures the program prompts for re-entry.
- **CSTA:** E5‑PRO‑PF‑01.

### T26.G5.04 – Store logs in CreatiCode tables for export

- **Short name:** Build table-based audit trails
- **Description:** Learners push collected events into table variables with named columns, prepping for CSV export to T27.
- **Challenge format:** Coding. Auto-grading checks that columns exist and entries append correctly.
- **CSTA:** E5‑PRO‑DH‑02.

---

## Grade 6

### T26.G6.01 – Map stakeholder questions to data requirements

- **Short name:** Translate research questions into fields
- **Description:** Students receive stakeholder questions (“Which level is hardest?”) and specify what data to collect (attempt count, completion time), aligning collection with analysis goals.
- **Challenge format:** Concept table. Auto-grading checks that each question has corresponding fields and measurement units.
- **CSTA:** MS‑DAA‑DF‑03.

### T26.G6.02 – Automate multi-sensor logging (voice + pose)

- **Short name:** Collect voice transcripts and pose frames together
- **Description:** Learners combine T23 blocks to record speech text and pose coordinates simultaneously, ensuring synchronized logs.
- **Challenge format:** Coding. Auto-grading feeds sample inputs and checks both logs update with matching timestamps.
- **CSTA:** MS‑PRO‑PF‑02.

### T26.G6.03 – Create consent and opt-out workflows

- **Short name:** Ask users before logging data
- **Description:** Students implement dialog widgets that explain what will be collected, gather consent, and disable logging when declined.
- **Challenge format:** Coding + ethics. Auto-grading toggles consent responses to ensure logging obeys settings.
- **CSTA:** MS‑CAS‑ET‑06.

### T26.G6.04 – Capture measurement error estimates

- **Short name:** Log +/- tolerance alongside values
- **Description:** Learners add extra columns (value ± error) when recording measurements, teaching them to note uncertainty.
- **Challenge format:** Concept + coding. Auto-grading checks tables for error columns and reflections about why uncertainty matters.
- **CSTA:** MS‑DAA‑DF‑03.

---

## Grade 7

### T26.G7.01 – Build reusable data collection modules

- **Short name:** Package logging as custom blocks
- **Description:** Students wrap logging behavior into custom blocks (e.g., `logEvent type message data`) so multiple sprites can call the same routine.
- **Challenge format:** Coding. Auto-grading verifies the custom block exists and writes consistent rows regardless of caller.
- **CSTA:** MS‑PRO‑PD‑08.

### T26.G7.02 – Monitor data quality in real time

- **Short name:** Add dashboards that show missing or extreme values
- **Description:** Learners build HUD widgets indicating percentage of responses collected, number of nulls, or out-of-range counts to catch issues while collecting.
- **Challenge format:** Coding + UI. Auto-grading manipulates inputs and checks that indicators update.
- **CSTA:** MS‑PRO‑PF‑02, DAA‑DF.

### T26.G7.03 – Document provenance for external datasets

- **Short name:** Track source, license, and refresh schedule
- **Description:** Students import an open dataset (weather, public CSV) and log metadata (where it came from, license, when to refresh), reinforcing responsible use.
- **Challenge format:** Concept + documentation. Auto-grading checks metadata fields are filled and references a real source.
- **CSTA:** MS‑CAS‑ET‑05.

### T26.G7.04 – Evaluate bias risks introduced during collection

- **Short name:** Audit sampling coverage
- **Description:** Learners compare planned participants vs actual participants and highlight underrepresented groups, proposing corrective actions.
- **Challenge format:** Concept analysis. Auto-grading requires referencing actual counts and a concrete mitigation plan.
- **CSTA:** MS‑CAS‑ET‑05, DAA‑DF.

---

## Grade 8

### T26.G8.01 – Design end-to-end telemetry pipelines

- **Short name:** Diagram sources → processing → storage → export
- **Description:** Students draw a pipeline for a multi-level game (client logs → cleaning script → storage table → CSV export), emphasizing interfaces between steps.
- **Challenge format:** Concept diagram + explanation. Auto-grading checks for all four stages and data formats at each handoff.
- **CSTA:** MS‑PRO‑PM‑03.

### T26.G8.02 – Implement scheduled data exports and resets

- **Short name:** Rotate logs automatically
- **Description:** Learners script timed routines that export a table to file (or display) and then clear/reset logs, mirroring production data rotation.
- **Challenge format:** Coding + scheduler logic. Auto-grading simulates timer events and checks for safe export before clearing.
- **CSTA:** MS‑PRO‑PF‑02.

### T26.G8.03 – Integrate XO guidance into data scripts

- **Short name:** Use XO to critique collection plans
- **Description:** Students send their collection protocol to XO (T24) for review, then document accepted and rejected suggestions, showing human oversight of AI advice.
- **Challenge format:** Concept + reflection. Auto-grading checks for XO transcript snippet and final decisions referencing evidence.
- **CSTA:** MS‑CAS‑ET‑06.

### T26.G8.04 – Publish data privacy agreements for peers

- **Short name:** Write a classroom data-sharing policy
- **Description:** Learners author a short agreement describing what data will be collected, how it’s stored, who can access it, and deletion timelines, tying back to AI4K12’s societal-impact focus.
- **Challenge format:** Policy writing. Rubric-based auto-grading checks for required sections (purpose, retention, opt-out, contact info).
- **CSTA:** MS‑CAS‑ET‑06, MS‑CAS‑HC‑02.

---
